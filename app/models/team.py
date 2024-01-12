from pydantic import BaseModel

class Team(BaseModel):
    name: str
    nationality: str
    place_in_group: int
    group: str
    pair: str = "Brak"