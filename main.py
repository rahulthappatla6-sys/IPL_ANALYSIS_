import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries Imported Successfully")

matches = pd.read_csv("dataset/matches.csv")
deliveries = pd.read_csv("dataset/deliveries.csv")
'''
print("===== MATCHES DATA (FIRST 5 ROWS) =====")
print(matches.head())

print("\n===== DELIVERIES DATA (FIRST 5 ROWS) =====")
print(deliveries.head())

print("\n===== MATCHES DATA (LAST 5 ROWS) =====")
print(matches.tail())

print("\n===== DELIVERIES DATA (LAST 5 ROWS) =====")
print(deliveries.tail())

print("\n===== DATASET SHAPE =====")

print("Matches Shape:", matches.shape)
print("Deliveries Shape:", deliveries.shape)

print("\n===== MATCHES COLUMNS =====")
print(matches.columns.tolist())

print("\n===== DELIVERIES COLUMNS =====")
print(deliveries.columns.tolist())

print("\n===== MATCHES NUMERICAL COLUMNS =====")
print(matches.select_dtypes(include=np.number).columns.tolist())

print("\n===== MATCHES CATEGORICAL COLUMNS =====")
print(matches.select_dtypes(include='object').columns.tolist())

print("\n===== DELIVERIES NUMERICAL COLUMNS =====")
print(deliveries.select_dtypes(include=np.number).columns.tolist())

print("\n===== DELIVERIES CATEGORICAL COLUMNS =====")
print(deliveries.select_dtypes(include='object').columns.tolist())

print("\n===== MATCHES DATA TYPES =====")
print(matches.dtypes)

print("\n===== DELIVERIES DATA TYPES =====")
print(deliveries.dtypes)

print("\n===== MATCHES STATISTICS =====")
print(matches.describe())

print("\n===== DELIVERIES STATISTICS =====")
print(deliveries.describe())

print("\n===== MISSING VALUES IN MATCHES =====")
print(matches.isnull().sum())

print("\n===== MISSING VALUES IN DELIVERIES =====")
print(deliveries.isnull().sum())

print("\nMatches Duplicates:", matches.duplicated().sum())
print("Deliveries Duplicates:", deliveries.duplicated().sum())

matches = matches.drop_duplicates()
deliveries = deliveries.drop_duplicates()

print("\nMatches Shape After Cleaning:", matches.shape)
print("Deliveries Shape After Cleaning:", deliveries.shape)

print(matches.isnull().sum())
print(deliveries.isnull().sum())

print("Matches Duplicates:", matches.duplicated().sum())
print("Deliveries Duplicates:", deliveries.duplicated().sum())

#Standardization

print(matches['team1'].unique())
print(matches['winner'].unique())
matches['winner'].value_counts()
print(matches['venue'].unique())

matches['date'] = pd.to_datetime(matches['date'])
matches['year'] = matches['date'].dt.year

matches.columns.tolist()
deliveries.columns.tolist()


#Team Mapping

team_mapping = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
    "Rising Pune Supergiants": "Rising Pune Supergiant"
}

# Matches table
for col in ["team1", "team2", "toss_winner", "winner"]:
    matches[col] = matches[col].replace(team_mapping)

# Deliveries table
deliveries["batting_team"] = deliveries["batting_team"].replace(team_mapping)
deliveries["bowling_team"] = deliveries["bowling_team"].replace(team_mapping)

print(sorted(deliveries["batting_team"].unique()))

print("Team names standardized successfully!")
print(matches['winner'].unique())


print("Total Matches:", matches['id'].nunique())

matches_per_season = matches['season'].value_counts().sort_index()
print(matches_per_season)

team_wins = matches['winner'].value_counts()
print(team_wins)

print("Team with Highest Wins:")
print(team_wins.idxmax())
print("Wins:", team_wins.max())

print("Team with Lowest Wins:")
print(team_wins.idxmin())
print("Wins:", team_wins.min())

player_awards = matches['player_of_match'].value_counts()
print(player_awards.head(10))

venue_count = matches['venue'].value_counts()
print(venue_count.head(10))

print(matches['toss_decision'].value_counts())


matches["toss_match_win"] = np.where(
    matches["toss_winner"] == matches["winner"],
    "Yes",
    "No"
)
print(matches["toss_match_win"].value_counts())

#Calculate Percentage
toss_win_pct = (
    (matches["toss_match_win"] == "Yes").sum()
    / len(matches)
) * 100

print(f"Toss Advantage Percentage: {toss_win_pct:.2f}%")

#Highest Winning Margin by Runs
runs_wins = matches[matches["result"] == "runs"]

highest_runs_win = runs_wins.loc[
    runs_wins["result_margin"].idxmax()
]

print(highest_runs_win[
    ["winner", "result_margin"]
])

#Highest Winning Margin by Wickets
wicket_wins = matches[matches["result"] == "wickets"]

highest_wicket_win = wicket_wins.loc[
    wicket_wins["result_margin"].idxmax()
]

print(highest_wicket_win[
    ["winner", "result_margin"]
])

#Highest Run Scorer
batsman_runs = deliveries.groupby(
    "batter"
)["batsman_runs"].sum()

print(batsman_runs.idxmax())
print(batsman_runs.max())

#Highest Wicket Taker
bowler_wickets = deliveries.groupby(
    "bowler"
)["is_wicket"].sum()

print(bowler_wickets.idxmax())
print(bowler_wickets.max())


#Top 10 Batsmen
top_batsmen = (
    deliveries.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_batsmen)

#Top 10 Bowlers
top_bowlers = (
    deliveries.groupby("bowler")["is_wicket"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_bowlers)

#Season-wise Total Runs

match_season = matches[["id", "season"]]

season_runs = deliveries.merge(
    match_season,
    left_on="match_id",
    right_on="id"
)

season_runs = season_runs.groupby(
    "season"
)["total_runs"].sum()

print(season_runs)

#Team-wise Average Runs
team_avg_runs = (
    deliveries.groupby("batting_team")["total_runs"]
    .mean()
    .sort_values(ascending=False)
)

print(team_avg_runs)

#Data Visualization

matches_per_season = matches['season'].value_counts().sort_index()

plt.figure(figsize=(12,6))

matches_per_season.plot(kind='bar')

plt.title("Matches Played by Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


team_wins = matches['winner'].value_counts()

plt.figure(figsize=(12,6))

team_wins.plot(kind='bar')

plt.title("Matches Won by Team")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

#Top 10 Run Scorers

top_batsmen = (
    deliveries.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

top_batsmen.sort_values().plot(kind='barh')

plt.title("Top 10 Run Scorers in IPL")
plt.xlabel("Runs")
plt.ylabel("Batsman")

plt.tight_layout()
plt.show()


#Top 10 Wicket Takers
top_bowlers = (
    deliveries.groupby("bowler")["is_wicket"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

top_bowlers.sort_values().plot(kind='barh')

plt.title("Top 10 Wicket Takers in IPL")
plt.xlabel("Wickets")
plt.ylabel("Bowler")

plt.tight_layout()
plt.show()


#Top 10 Player of the Match Award Winners
top_pom = (
    matches["player_of_match"]
    .value_counts()
    .head(10)
)

print(top_pom)
plt.figure(figsize=(10,6))

top_pom.sort_values().plot(kind='barh')

plt.title("Top 10 Player of the Match Award Winners")
plt.xlabel("Number of Awards")
plt.ylabel("Player")

plt.tight_layout()
plt.show()

#Toss Decision Distribution
toss_decision_count = matches["toss_decision"].value_counts()

print(toss_decision_count)

plt.figure(figsize=(8,5))

toss_decision_count.plot(kind="bar")

plt.title("Toss Decision Distribution in IPL")
plt.xlabel("Toss Decision")
plt.ylabel("Count")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

#Toss Decision Distribution in Pie Chart
plt.figure(figsize=(6,6))

toss_decision_count.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Toss Decision Distribution in IPL")
plt.ylabel("")

plt.show()

#Toss Winner vs Match Winner
matches["toss_match_win"] = np.where(
    matches["toss_winner"] == matches["winner"],
    "Yes",
    "No"
)
toss_match_win_count = matches["toss_match_win"].value_counts()

print(toss_match_win_count)
plt.figure(figsize=(8,5))

toss_match_win_count.plot(kind="bar")

plt.title("Matches Won After Winning Toss")
plt.xlabel("Won Toss and Match?")
plt.ylabel("Number of Matches")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

#Season-wise Total Runs
season_runs = deliveries.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id"
)

season_runs = season_runs.groupby(
    "season"
)["total_runs"].sum()

plt.figure(figsize=(12,6))

season_runs.plot(
    kind="line",
    marker="o"
)

plt.title("Season-wise Total Runs in IPL")
plt.xlabel("Season")
plt.ylabel("Total Runs")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

#Season-wise Wickets
season_wickets = deliveries.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id"
)

season_wickets = season_wickets.groupby(
    "season"
)["is_wicket"].sum()

print(season_wickets)
plt.figure(figsize=(12,6))

season_wickets.plot(
    kind="line",
    marker="o"
)

plt.title("Season-wise Wickets in IPL")
plt.xlabel("Season")
plt.ylabel("Total Wickets")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


#Venue-wise Match Count
top_venues = (
    matches["venue"]
    .value_counts()
    .head(10)
)

print(top_venues)
plt.figure(figsize=(12,6))

top_venues.sort_values().plot(kind="barh")

plt.title("Top 10 IPL Venues by Match Count")
plt.xlabel("Number of Matches")
plt.ylabel("Venue")

plt.tight_layout()
plt.show()


#Runs Distribution
plt.figure(figsize=(10,6))

plt.hist(
    deliveries["total_runs"],
    bins=8
)

plt.title("Distribution of Runs per Ball")
plt.xlabel("Runs Scored on a Ball")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

#Team Performance Comparison
team_avg_runs = (
    deliveries.groupby("batting_team")["total_runs"]
    .mean()
    .sort_values(ascending=False)
)
plt.figure(figsize=(12,6))

team_avg_runs.sort_values().plot(kind="barh")

plt.title("Average Runs per Ball by Team")
plt.xlabel("Average Runs")
plt.ylabel("Team")

plt.tight_layout()
plt.show()
'''
#Runs vs Wickets
season_stats = deliveries.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id"
)

season_stats = season_stats.groupby("season").agg({
    "total_runs": "sum",
    "is_wicket": "sum"
})

plt.figure(figsize=(10,6))

plt.scatter(
    season_stats["total_runs"],
    season_stats["is_wicket"]
)

plt.title("Runs vs Wickets by Season")
plt.xlabel("Total Runs")
plt.ylabel("Total Wickets")

plt.tight_layout()
plt.show()

#Correlation Heatmap
import seaborn as sns

numeric_cols = deliveries[
    ["batsman_runs", "extra_runs", "total_runs", "is_wicket"]
]

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_cols.corr(),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()

