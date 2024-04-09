# File for helpful functions in this project

from nba_api.stats.static import teams

def get_team_id_from_abbrev(abbrev):
    return teams.find_team_by_abbreviation(abbrev)[0].get("id")

def basic_team_info(abbrev):
    team_info = teams.find_team_by_abbreviation(abbrev)[0]
    return team_info['full_name'], team_info['city'], team_info['state'], team_info['year_founded']