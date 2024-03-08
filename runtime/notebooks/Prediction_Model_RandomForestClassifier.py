import pandas as pd
from sklearn.model_selection import train_test_split

team_statistics = pd.read_csv("nba_games_runtime.csv", index_col=0)

