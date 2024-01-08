from fastapi import APIRouter
from models.team import Team
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_teams():
    teams = list_serial(collection_name.find())
    return teams

@router.post("/")
async def post_team(team: Team):
    collection_name.insert_one(dict(team))

@router.put("/{id}")
async def put_team(id: str, team: Team):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(team)})

@router.delete("/")
async def delete_teams():
    collection_name.delete_many({})

@router.delete("/{id}")
async def delete_team(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})