import time

import requests
import calendar
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import pandas as pd

nba_teams = [
    {"team": "Atlanta Hawks", "abbreviation": "ATL"},
    {"team": "Boston Celtics", "abbreviation": "BOS"},
    {"team": "Brooklyn Nets", "abbreviation": "BRK"},
    {"team": "Charlotte Hornets", "abbreviation": "CHO"},
    {"team": "Chicago Bulls", "abbreviation": "CHI"},
    {"team": "Cleveland Cavaliers", "abbreviation": "CLE"},
    {"team": "Dallas Mavericks", "abbreviation": "DAL"},
    {"team": "Denver Nuggets", "abbreviation": "DEN"},
    {"team": "Detroit Pistons", "abbreviation": "DET"},
    {"team": "Golden State Warriors", "abbreviation": "GSW"},
    {"team": "Houston Rockets", "abbreviation": "HOU"},
    {"team": "Indiana Pacers", "abbreviation": "IND"},
    {"team": "Los Angeles Clippers", "abbreviation": "LAC"},
    {"team": "Los Angeles Lakers", "abbreviation": "LAL"},
    {"team": "Memphis Grizzlies", "abbreviation": "MEM"},
    {"team": "Miami Heat", "abbreviation": "MIA"},
    {"team": "Milwaukee Bucks", "abbreviation": "MIL"},
    {"team": "Minnesota Timberwolves", "abbreviation": "MIN"},
    {"team": "New Orleans Pelicans", "abbreviation": "NOP"},
    {"team": "New York Knicks", "abbreviation": "NYK"},
    {"team": "Oklahoma City Thunder", "abbreviation": "OKC"},
    {"team": "Orlando Magic", "abbreviation": "ORL"},
    {"team": "Philadelphia 76ers", "abbreviation": "PHI"},
    {"team": "Phoenix Suns", "abbreviation": "PHO"},
    {"team": "Portland Trail Blazers", "abbreviation": "POR"},
    {"team": "Sacramento Kings", "abbreviation": "SAC"},
    {"team": "San Antonio Spurs", "abbreviation": "SAS"},
    {"team": "Toronto Raptors", "abbreviation": "TOR"},
    {"team": "Utah Jazz", "abbreviation": "UTA"},
    {"team": "Washington Wizards", "abbreviation": "WAS"}
]

def scrape_team_specific_schedule(team_abbreviation):
    year = datetime.now().year
    url = f"https://www.basketball-reference.com/teams/{team_abbreviation}/{year}_games.html#games_link"
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the table containing the schedule
        schedule_table = soup.find("table")
        # Check if the table was found
        if schedule_table:
            # Extract the rows of the table (each row represents a game)
            rows = schedule_table.find_all("tr")
            # Initialize a list to store game information
            games = []
            for row in rows[1:]:
                column = row.findAll("td")
                if len(column) >= 6:
                    game_date = column[0].text.strip()
                    game_time = column[1].text.strip()
                    team = team_abbreviation
                    for team_info in nba_teams:
                        if team_info["abbreviation"] == team:
                            team = team_info["team"]
                    team_opp = column[5].text.strip()
                    home = 1
                    if column[4].text.strip() == "@":
                        home = 0
                    games.append(
                        {"Team": team, "Opponent": team_opp, "Date": game_date, "Time": game_time, "Home": home})
            # Convert the list of dictionaries into a DataFrame
            schedule_df = pd.DataFrame(games)
            # convert with most recent games first
            schedule_df = schedule_df[::-1]
            if schedule_df.empty:
                schedule_df = "This team has no schedule lol"
            return schedule_df
        else:
            print("table not found")
    else:
        print(f"Failed to retrieve NBA schedule. Status code: {response.status_code}")

# def main():
#     for team_info in nba_teams:
#         print(team_info["team"])
#         print(scrape_team_specific_schedule(team_info["abbreviation"]))
#         time.sleep(3)
#
# if __name__ == "__main__":
#     main()




