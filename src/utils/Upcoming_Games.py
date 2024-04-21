import requests
import calendar
from utils.Elo_Predictor import get_winner
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import pandas as pd

pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_columns', None)  # None means unlimited
nba_teams = [
    {"team": "Atlanta Hawks", "abbreviation": "ATL"},
    {"team": "Boston Celtics", "abbreviation": "BOS"},
    {"team": "Brooklyn Nets", "abbreviation": "BKN"},
    {"team": "Charlotte Hornets", "abbreviation": "CHA"},
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
    {"team": "Phoenix Suns", "abbreviation": "PHX"},
    {"team": "Portland Trail Blazers", "abbreviation": "POR"},
    {"team": "Sacramento Kings", "abbreviation": "SAC"},
    {"team": "San Antonio Spurs", "abbreviation": "SAS"},
    {"team": "Toronto Raptors", "abbreviation": "TOR"},
    {"team": "Utah Jazz", "abbreviation": "UTA"},
    {"team": "Washington Wizards", "abbreviation": "WAS"}
]

def scrape_upcoming_nba_schedule():
    # Get today's date
    today = date.today()
    month = calendar.month_abbr[datetime.now().month]
    month_url = today.strftime("%B").lower()
    day = today.strftime("%d")
    one_week = today + timedelta(days=7)
    # Construct the URL based on today's date
    url = f"https://www.basketball-reference.com/leagues/NBA_{today.year}_games-{month_url}.html"
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
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
                columns = row.find_all("th")
                game_date = columns[0].text.strip()
                game_date_obj = datetime.strptime(game_date, "%a, %b %d, %Y").date()
                if today <= game_date_obj <= one_week:
                    name_column = row.find_all("td")
                    if name_column[1].text != "":
                        home_team = name_column[3].text.strip()
                        home_abbr = home_team
                        for team_info in nba_teams:
                            if team_info["team"] == home_abbr:
                                home_abbr = team_info["abbreviation"]
                        away_team = name_column[1].text.strip()
                        away_abbr = away_team
                        for team_info in nba_teams:
                            if team_info["team"] == away_abbr:
                                away_abbr = team_info["abbreviation"]
                        game_time = name_column[0].text.strip() if name_column[0].text.strip() else "(No time has been set yet...)"
                        winner_df = get_winner(home_abbr, away_abbr)
                        predicted_winner = winner_df.iloc[0, 2]
                        winner_probability = winner_df.iloc[0, 3]
                        games.append({"Home Team": home_team, "Visitor Team": away_team, "Date": game_date, "Time": game_time, "Predicted Winner": predicted_winner,
                                      "Winner Probability": winner_probability})

            # Convert the list of dictionaries into a DataFrame
            schedule_df = pd.DataFrame(games)
            if schedule_df.empty:
                schedule_df = "No Games for the week"
            return schedule_df
        else:
            print("No schedule table found on the page.")
    else:
        print(f"Failed to retrieve NBA schedule. Status code: {response.status_code}")

def main():
    print(scrape_upcoming_nba_schedule())

if __name__ == "__main__":
    main()