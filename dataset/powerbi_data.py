import pandas as pd

# ==========================
# LOAD DATASETS
# ==========================

matches = pd.read_csv("dataset/matches.csv")
deliveries = pd.read_csv("dataset/deliveries.csv")

print("Datasets Loaded Successfully!")

# ==========================
# TEAM WINS
# ==========================

team_wins = matches["winner"].value_counts().reset_index()
team_wins.columns = ["Team", "Wins"]

team_wins.to_csv("team_wins.csv", index=False)

# ==========================
# TOP BATSMEN
# ==========================

top_batsmen = (
    deliveries.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

top_batsmen.columns = ["Batter", "Runs"]

top_batsmen.to_csv("top_batsmen.csv", index=False)

# ==========================
# TOP BOWLERS
# ==========================

top_bowlers = (
    deliveries.groupby("bowler")["is_wicket"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

top_bowlers.columns = ["Bowler", "Wickets"]

top_bowlers.to_csv("top_bowlers.csv", index=False)

# ==========================
# PLAYER OF THE MATCH
# ==========================

player_of_match = (
    matches["player_of_match"]
    .value_counts()
    .reset_index()
)

player_of_match.columns = ["Player", "Awards"]

player_of_match.to_csv("player_of_match.csv", index=False)

# ==========================
# VENUE ANALYSIS
# ==========================

venue_matches = (
    matches["venue"]
    .value_counts()
    .reset_index()
)

venue_matches.columns = ["Venue", "Matches"]

venue_matches.to_csv("venue_matches.csv", index=False)

# ==========================
# SEASON-WISE RUNS
# ==========================

season_runs = (
    deliveries.merge(
        matches[["id", "season"]],
        left_on="match_id",
        right_on="id"
    )
    .groupby("season")["total_runs"]
    .sum()
    .reset_index()
)

season_runs.columns = ["Season", "Total_Runs"]

season_runs.to_csv("season_runs.csv", index=False)

# ==========================
# SEASON-WISE WICKETS
# ==========================

season_wickets = (
    deliveries.merge(
        matches[["id", "season"]],
        left_on="match_id",
        right_on="id"
    )
    .groupby("season")["is_wicket"]
    .sum()
    .reset_index()
)

season_wickets.columns = ["Season", "Total_Wickets"]

season_wickets.to_csv("season_wickets.csv", index=False)

# ==========================
# TEAM AVERAGE RUNS
# ==========================

team_avg_runs = (
    deliveries.groupby("batting_team")["total_runs"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

team_avg_runs.columns = ["Team", "Average_Runs"]

team_avg_runs.to_csv("team_avg_runs.csv", index=False)

# ==========================
# KPI DATA
# ==========================

total_matches = matches.shape[0]
total_runs = deliveries["total_runs"].sum()
total_wickets = deliveries["is_wicket"].sum()
total_teams = matches["winner"].dropna().nunique()

kpi = pd.DataFrame({
    "Total_Matches": [total_matches],
    "Total_Runs": [total_runs],
    "Total_Wickets": [total_wickets],
    "Total_Teams": [total_teams]
})

kpi.to_csv("kpi.csv", index=False)

# ==========================
# SUCCESS MESSAGE
# ==========================

print("\nAll Power BI files exported successfully!")
print("Generated Files:")
print("- team_wins.csv")
print("- top_batsmen.csv")
print("- top_bowlers.csv")
print("- player_of_match.csv")
print("- venue_matches.csv")
print("- season_runs.csv")
print("- season_wickets.csv")
print("- team_avg_runs.csv")
print("- kpi.csv")