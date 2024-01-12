def individual_serial(team) -> dict:
    return{
        "id": str(team["_id"]),
        "name": team["name"],
        "nationality": team["nationality"],
        "place_in_group": team["place_in_group"],
        "group": team["group"],
        "pair": team["pair"]
    }

def list_serial(teams) -> list:
    return[individual_serial(team) for team in teams]
