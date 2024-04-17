# File for helpful functions in this project

from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamdetails, commonteamroster
from nba_api.stats.endpoints import leaguestandings 


from PIL import Image

import json

def get_team_id_from_abbrev(abbrev):
    return teams.find_team_by_abbreviation(abbrev).get("id")

def basic_team_info(abbrev):
    team_info = teams.find_team_by_abbreviation(abbrev)
    return team_info['full_name'], team_info['city'], team_info['state'], team_info['year_founded']

def detailed_team_info(abbrev):
    team_id = get_team_id_from_abbrev(abbrev)
    return teamdetails.TeamDetails(team_id).team_background.get_data_frame()

def get_team_championships(abbrev):
    team_id = get_team_id_from_abbrev(abbrev)
    return teamdetails.TeamDetails(team_id).team_awards_championships.get_data_frame()

def get_top_left_pixel_color(image_path):
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        pixel_color = img.getpixel((0, 0))  # (0, 0) is the top-left corner
        hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel_color)  # convert color into hex
    return hex_color

def get_team_roster(abbrev):
    team_id = get_team_id_from_abbrev(abbrev)
    roster_df = commonteamroster.CommonTeamRoster(team_id=team_id).common_team_roster.get_data_frame()
    
    selected_columns = ['PLAYER', 'NUM', 'POSITION', 'HEIGHT', 'BIRTH_DATE', 'AGE', 'SCHOOL']
    roster_filtered = roster_df.loc[:, selected_columns]
    
    return roster_filtered

def get_social_media_links(abbrev):
    team_id = get_team_id_from_abbrev(abbrev)
    social_df = teamdetails.TeamDetails(team_id).team_social_sites.get_data_frame()
    social_df.set_index('ACCOUNTTYPE', inplace=True)
    return social_df.loc['Facebook', 'WEBSITE_LINK'], social_df.loc['Twitter', 'WEBSITE_LINK'], social_df.loc['Instagram', 'WEBSITE_LINK']

def get_league_standings():
    standings_data = leaguestandings.LeagueStandings(season='2023-24').standings.get_data_frame()
    return standings_data