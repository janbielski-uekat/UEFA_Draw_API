from typing import List
from models.team import Team

def is_valid(teamA, teamB):
    return (
        teamA.name != teamB.name and
        teamA.nationality != teamB.nationality and
        teamA.group != teamB.group and
        teamA.place_in_group != teamB.place_in_group and
        teamA.pair == "Brak" and teamB.pair == "Brak"
    )

def draw_teams(teams: List[Team]):

    winners = [t for t in teams if t.place_in_group == 1 and t.pair == "Brak"]
    runners_up = [t for t in teams if t.place_in_group == 2 and t.pair == "Brak"]

    def draw(runner_up_index, winners):

        if runner_up_index == len(runners_up):
            return []
        
        for i, winner in enumerate(winners):
            if is_valid(winner, runners_up[runner_up_index]):
                result = draw(runner_up_index + 1, winners[:i] + winners[i+1:])
                if result is not None:
                    return [(runners_up[runner_up_index].name, winner.name)] + result
        return None

    return draw(0, winners)

def get_valid_pairings(runner_up: Team, teams: List[Team]):

    valid_parings = []    
    possiple_pairs = [t for t in teams if is_valid(runner_up, t)]

    for possible_pair in possiple_pairs:
        temp_teams = teams.copy()

        for team in temp_teams:
            if team.name == runner_up.name:
                team.pair = possible_pair.name

        if draw_teams(temp_teams) != None:
            valid_parings.append(possible_pair.name)

    return valid_parings
