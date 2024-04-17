import requests
import calendar
from bs4 import BeautifulSoup
from datetime import date, datetime

def scrape_nba_schedule():
    # Get today's date
    today = date.today()
    month = calendar.month_abbr[datetime.now().month]
    month_url = today.strftime("%B").lower()
    day = today.strftime("%d")
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
            # Print the schedule for today
            print(f"Upcoming Games (Including Today): \n")
            key = 0
            for row in rows[1:]:
                columns = row.find_all("th")
                game_date = columns[0].text.strip()
                if day in game_date and month in game_date:
                    key = 1
                if key == 1:
                    name_column = row.find_all("td")
                    if name_column[1].text != "":
                        print(game_date)
                        home_team = name_column[3].text.strip()
                        away_team = name_column[1].text.strip()
                        print(f"{away_team} vs {home_team} @ {name_column[0].text.strip()}\n")

        else:
            print("No schedule table found on the page.")
    else:
        print(f"Failed to retrieve NBA schedule. Status code: {response.status_code}")

def main():
    scrape_nba_schedule()

if __name__ == "__main__":
    main()
