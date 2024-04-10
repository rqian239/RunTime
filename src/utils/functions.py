# File for helpful functions in this project

from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamdetails

import json

def get_team_id_from_abbrev(abbrev):
    return teams.find_team_by_abbreviation(abbrev).get("id")

def basic_team_info(abbrev):
    team_info = teams.find_team_by_abbreviation(abbrev)
    return team_info['full_name'], team_info['city'], team_info['state'], team_info['year_founded']

def detailed_team_info(abbrev):
    team_id = get_team_id_from_abbrev(abbrev)
    return teamdetails.TeamDetails(team_id).team_background.get_data_frame()
