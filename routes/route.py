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