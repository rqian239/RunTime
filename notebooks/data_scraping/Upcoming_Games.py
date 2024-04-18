import requests
import calendar
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import pandas as pd

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
                        away_team = name_column[1].text.strip()
                        game_time = name_column[0].text.strip() if name_column[0].text.strip() else "(No time has been set yet...)"
                        games.append({"Home Team": home_team, "Visitor Team": away_team, "Date": game_date, "Time": game_time})

            # Convert the list of dictionaries into a DataFrame
            schedule_df = pd.DataFrame(games)
            if schedule_df.empty:
                schedule_df = "No Games for the week"
            return schedule_df
        else:
            print("No schedule table found on the page.")
    else:
        print(f"Failed to retrieve NBA schedule. Status code: {response.status_code}")

# def main():
#     print(scrape_upcoming_nba_schedule())
#
# if __name__ == "__main__":
#     main()