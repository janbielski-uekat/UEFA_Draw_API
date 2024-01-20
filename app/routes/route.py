from typing import List
from fastapi import APIRouter
from models.team import Team
from services.draw_logic import get_valid_pairings
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_teams():
    teams = list_serial(collection_name.find())
    return teams

@router.post("/")
async def post_teams(teams: List[Team]):
    teams_dict = [team.model_dump() for team in teams]
    collection_name.insert_many(teams_dict)

@router.delete("/")
async def delete_teams():
    collection_name.delete_many({})

@router.get("/{id}")
async def get_valid_pairs(id: str):
    runner_up = Team(**collection_name.find_one({"_id": ObjectId(id)}))
    teams = []
    for team in collection_name.find():
        teams.append(Team(**team))

    return get_valid_pairings(runner_up, teams)

@router.put("/{teamA_id}/{teamB_id}")
async def put_pair(teamA_id: str, teamB_id: str):
    teamA = individual_serial(collection_name.find_one({"_id": ObjectId(teamA_id)}))
    teamB = individual_serial(collection_name.find_one({"_id": ObjectId(teamB_id)}))

    teamA["pair"] = teamB["name"]
    teamB["pair"] = teamA["name"]

    collection_name.find_one_and_update({"_id": ObjectId(teamA_id)}, {"$set": teamA})
    collection_name.find_one_and_update({"_id": ObjectId(teamB_id)}, {"$set": teamB})


