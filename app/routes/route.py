from typing import List
from fastapi import APIRouter, HTTPException
from models.team import Team
from services.draw_logic import get_valid_pairings
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()


@router.get("/", description="Zwraca listę wszystkich zespołów znajdujących się aktualnie w bazie")
async def get_teams():
    teams = list_serial(collection_name.find())
    return teams


@router.post("/", description="Dodaje do bazy listę zespołów")
async def post_teams(teams: List[Team]):
    teams_dict = [team.model_dump() for team in teams]
    collection_name.insert_many(teams_dict)


@router.delete("/", description="Usuwa wszystkie zespoły z bazy")
async def delete_teams():
    collection_name.delete_many({})


@router.get("/{id}", description="Zwraca nazwy wszystkich zespołów z którymi można sparować wskazany")
async def get_valid_pairs(id: str):
    runner_up_data = collection_name.find_one({"_id": ObjectId(id)})

    if runner_up_data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Team with id {id} does not exist"
        )

    runner_up = Team(**runner_up_data)

    if runner_up.place_in_group != 2:
        raise HTTPException(
            status_code=400,
            detail=f"Team with id {id} is not a runner up"
        )

    if runner_up.pair != "Brak":
        raise HTTPException(
            status_code=400,
            detail=f"Team with id {id} is already paired"
        )

    teams = []
    for team in collection_name.find():
        teams.append(Team(**team))

    valid_pairings = get_valid_pairings(runner_up, teams)

    if len(valid_pairings) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Team with ID {id} has no valid pairings!"
        )

    return get_valid_pairings(runner_up, teams)


@router.put("/{teamA_id}/{teamB_id}", description="Łączy wskazane zespoły w parę")
async def put_pair(teamA_id: str, teamB_id: str):
    teams = []
    for team in collection_name.find():
        teams.append(Team(**team))

    teamA_data = collection_name.find_one({"_id": ObjectId(teamA_id)})
    teamB_data = collection_name.find_one({"_id": ObjectId(teamB_id)})

    if teamA_data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Team with id {teamA_id} does not exist"
        )
    if teamB_data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Team with id {teamB_id} does not exist"
        )

    teamA = Team(**teamA_data)
    teamB = Team(**teamB_data)

    if teamA.place_in_group == 2:
        runner_up = teamA
        winner = teamB
    else:
        runner_up = teamB
        winner = teamA

    if winner.name in get_valid_pairings(runner_up, teams):
        teamA.pair = teamB.name
        teamB.pair = teamA.name
        collection_name.find_one_and_update({"_id": ObjectId(teamA_id)}, {"$set": teamA.model_dump()},
                                            return_document=True)
        collection_name.find_one_and_update({"_id": ObjectId(teamB_id)}, {"$set": teamA.model_dump()},
                                            return_document=True)
    else:
        raise HTTPException(
            status_code=400,
            detail=f"This pairing is invalid."
        )

