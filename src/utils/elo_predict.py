# Import statements
import pandas as pd
from nba_api.stats.endpoints import teamgamelogs


# Get the entire season of data
teamGameLogs = teamgamelogs.TeamGameLogs(season_nullable='2023-24', season_type_nullable='Regular Season')
regular_season_df = teamGameLogs.get_data_frames()[0]
teamGameLogs = teamgamelogs.TeamGameLogs(season_nullable='2023-24', season_type_nullable='Playoffs')
playoff_season_df = teamGameLogs.get_data_frames()[0]
df = pd.concat([playoff_season_df, regular_season_df], axis=0)
# Freeing up these dataframes
del regular_season_df
del playoff_season_df

# Set initial Elo ratings manually

initial_elo = dict()  # Create a dictionary to hold initial elos

# ELO RATINGS AT START OF 2023-24 SEASON
initial_elo["ATL"] = 1525
initial_elo["BKN"] = 1495
initial_elo["BOS"] = 1624
initial_elo["CHA"] = 1416
initial_elo["CHI"] = 1534
initial_elo["CLE"] = 1554
initial_elo["DAL"] = 1458
initial_elo["DEN"] = 1640
initial_elo["DET"] = 1328
initial_elo["GSW"] = 1569
initial_elo["HOU"] = 1372
initial_elo["IND"] = 1426
initial_elo["LAC"] = 1519
initial_elo["LAL"] = 1570
initial_elo["MEM"] = 1553
initial_elo["MIA"] = 1580
initial_elo["MIL"] = 1547
initial_elo["MIN"] = 1516
initial_elo["NOP"] = 1524
initial_elo["NYK"] = 1573
initial_elo["OKC"] = 1514
initial_elo["ORL"] = 1463
initial_elo["PHI"] = 1606
initial_elo["PHX"] = 1544
initial_elo["POR"] = 1359
initial_elo["SAC"] = 1529
initial_elo["SAS"] = 1373
initial_elo["TOR"] = 1546
initial_elo["UTA"] = 1437
initial_elo["WAS"] = 1454

#Sort games by date
df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
df = df.sort_values("GAME_DATE")
df = df.reset_index(drop=True)

# Define the data types for the columns in the DataFrame
dtype = {
    'date': str,
    'season': str,
    'team': str,
    'team_opp': str,
    'team_elo_before': float,
    'team_opp_elo_before': float,
    'team_elo_after': float,
    'team_opp_elo_after': float,
    'home': bool  # Assuming this column represents whether the team is playing at home
}

# Create DataFrames to store elo calculations for each game and elos for each team
elo_df = pd.DataFrame(columns=dtype.keys()).astype(dtype)


def team_opponent(game_id, team_we_know):
    # this function should spew out the opposing team
    df_opponent = df[(df['GAME_ID'] == game_id) & (df['TEAM_ABBREVIATION'] != team_we_know)]
    opponent = df_opponent['TEAM_ABBREVIATION'].iloc[0]
    return opponent


def are_they_home(matchup):
    if "@" in matchup:
        return 0
    else:
        return 1


def team_opponent_pts(game_id, team_we_know):
    df_opponent = df[(df['GAME_ID'] == game_id) & (df['TEAM_ABBREVIATION'] != team_we_know)]
    team_pts = df_opponent['PTS'].iloc[0]
    return team_pts

# retrieve the previous elo
def get_prev_elo(team, date, season, stats_df, elo_df):
    # Get row of previous game
    prev_game = \
    stats_df[(stats_df["GAME_DATE"] < date) & (stats_df["TEAM_ABBREVIATION"] == team)].sort_values(by="GAME_DATE").tail(
        1).iloc[0]

    # Extract the elo from that game
    elo_rating = elo_df[
        (elo_df["date"] == prev_game["GAME_DATE"]) & (elo_df["team"] == prev_game['TEAM_ABBREVIATION']) & (
                    elo_df["team_opp"] == team_opponent(prev_game["GAME_ID"], prev_game["TEAM_ABBREVIATION"]))][
        'team_elo_after'].values[0]

    if prev_game["SEASON_YEAR"] != season:
        return (0.75 * elo_rating) + (0.25 * 1505)  # This is how elo ratings are carried over to next season
    else:
        return elo_rating
def calculate_expected_win_probability(team_elo_rating, team_opp_elo_rating):
    E_team = 1. / (1 + 10 ** ((team_opp_elo_rating - team_elo_rating) / (400.)))
    return E_team

def S_var(team_pts, opp_pts):
    S_team, S_opp = 0, 0

    if team_pts > opp_pts:
        S_team = 1
    elif opp_pts > team_pts:
        S_opp = 1
    else:
        S_team, S_opp = 0.5, 0.5

    return S_team, S_opp

# Compute the moving K constant from Silver's formula
def K_constant(MOV, elo_diff):
    K_0 = 20

    if MOV > 0:  # if "team" is the winner
        multiplier = ((MOV + 3) ** (0.8)) / (7.5 + 0.006 * (elo_diff))
    else:  # if "team_opp" is the winner
        multiplier = ((-MOV + 3) ** (0.8)) / (
                    7.5 + 0.006 * (-elo_diff))  # note how we have to flip the elo_diff and make MOV positive

    return K_0 * multiplier
def update_elo(team_pts, opp_pts, team_elo_before, team_opp_elo_before, home):
    # In Silver's elo calculations, home advantage is accounted for by increasing the home team elo rating by 100 for the E and K calculations
    home_court_advantage = 100

    # Add the home court advantage (we will need to remove this later)
    if home == 1:
        team_elo_before += home_court_advantage
    else:
        team_opp_elo_before += home_court_advantage

    E_team = calculate_expected_win_probability(team_elo_before, team_opp_elo_before)
    E_team_opp = 1 - E_team

    elo_diff = team_elo_before - team_opp_elo_before

    # MOV = Margin of Victory
    MOV = team_pts - opp_pts

    # S variable in Silver's equation, value for was the winner
    S_team, S_opp = S_var(team_pts, opp_pts)

    # K constant
    K = K_constant(MOV, elo_diff)

    # Remove the home court advantage (we are done calculating the different variables, revert to true elo)
    if home == 1:
        team_elo_before -= home_court_advantage
    else:
        team_opp_elo_before -= home_court_advantage

    # Calculate the elos (which is a recursive formula)
    team_elo_after = team_elo_before + K * (S_team - E_team)
    team_opp_elo_after = team_opp_elo_before + K * (S_opp - E_team_opp)

    return team_elo_after, team_opp_elo_after


# ----------------------------- compute_all_elos_for_the_season -----------------------------
row_count = 0

for index, row in df.iterrows():
    game_date = row["GAME_DATE"]
    season = row["SEASON_YEAR"]
    team = row["TEAM_ABBREVIATION"]

    team_opp = team_opponent(row["GAME_ID"], row[
        "TEAM_ABBREVIATION"])
    is_this_team_home = are_they_home(
        row["MATCHUP"])

    team_pts = row["PTS"]
    opp_pts = team_opponent_pts(row["GAME_ID"],
                                row["TEAM_ABBREVIATION"])

    # Check if we need to initialize the elo
    if (team not in elo_df["team"].values):
        team_starting_elo = initial_elo[team]
        team_elo_before = team_starting_elo
    else:
        team_elo_before = get_prev_elo(team, game_date, season, df, elo_df)

    if (team_opp not in elo_df["team_opp"].values):
        team_opp_starting_elo = initial_elo[team_opp]
        team_opp_elo_before = team_opp_starting_elo
    else:
        team_opp_elo_before = get_prev_elo(team_opp, game_date, season, df, elo_df)

    team_elo_after, team_opp_elo_after = update_elo(team_pts, opp_pts, team_elo_before, team_opp_elo_before,
                                                    is_this_team_home)

    new_row_in_elo_df = {
        "date": game_date,
        "season": season,
        "team": team,
        "team_opp": team_opp,
        "team_elo_before": team_elo_before,
        "team_opp_elo_before": team_opp_elo_before,
        "team_elo_after": team_elo_after,
        "team_opp_elo_after": team_opp_elo_after,
        "home": is_this_team_home
    }

    new_row = pd.DataFrame([new_row_in_elo_df])

    # Assuming elo_df is the DataFrame you're concatenating with new_row
    # Check for empty or all-NA entries in elo_df
    non_empty_columns = elo_df.dropna(axis=1, how='all').columns

    # Concatenate only with non-empty columns
    elo_df = pd.concat([elo_df[non_empty_columns], new_row], ignore_index=True)

    row_count += 1

# ----------------------------- ----------------------------- -----------------------------

# Functions to calculate and retrieve elos
def get_recent_elo(team_abbv):
    # Ensure the 'date' column is in the correct datetime format (if not already)
    elo_df['date'] = pd.to_datetime(elo_df['date'])

    # Filter the DataFrame for rows matching the specific team
    team_data = elo_df[elo_df["team"] == team_abbv]

    # Find the most recent date in the filtered DataFrame
    most_recent_date = team_data['date'].max()

    # Filter the DataFrame again for rows that match the most recent date for the team
    elo_df_now = team_data[team_data["date"] == most_recent_date]

    # Return the 'team_elo_after' value for the most recent date
    # Using .iloc[-1] to ensure we get the last (or only) record if there are multiple games on the most recent date
    return elo_df_now["team_elo_after"].iloc[0]


# Silver's point spread formula
def point_spread(team_elo, opp_elo):
    elo_diff = team_elo - opp_elo
    return elo_diff / 28.


# Formula for season wins from polynomial regression
def project_season_wins(elo):
    return (-0.000000185006724245061 * (elo ** 3) + 0.000835470379387845 * (elo ** 2) - 1.15355230436639 * (
        elo) + 515.526317931045)



# spews dataframe of 1 row with stats that include: teams, winner, point differential, what percantage they have of winning per team
# function for fantasy games
def get_winner(home_team_abbrev, away_team_abbrev):
    team_elo_1 = get_recent_elo(home_team_abbrev) + 100
    team_elo_2 = get_recent_elo(away_team_abbrev)
    winner = home_team_abbrev
    if team_elo_1 < team_elo_2:
        winner = away_team_abbrev
    if winner == home_team_abbrev:
        win_prob = calculate_expected_win_probability(team_elo_1, team_elo_2)
        point_spread_new = point_spread(team_elo_1, team_elo_2)
    else:
        win_prob = calculate_expected_win_probability(team_elo_2, team_elo_1)
        point_spread_new = point_spread(team_elo_2, team_elo_1)
    data = {'Home': [home_team_abbrev], 'Away': [away_team_abbrev], 'Expected_Winner': [winner], 'Winner_Probability': [win_prob],
            'Point_Spread': [point_spread_new]}
    new_df = pd.DataFrame(data)
    return new_df

# Free these up, we don't need them anymore
del df
del initial_elo

def main():
    print(elo_df)
    print(get_winner("MIN", "PHX"))
    print(get_winner("TOR", "DET"))

if __name__ == "__main__":
    main()


