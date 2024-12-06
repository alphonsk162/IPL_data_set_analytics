import matplotlib.pyplot as plt
import csv
'''{'match_id': '1', 'inning': '1', 'batting_team': 'Sunrisers Hyderabad', 'bowling_team': 'Royal Challengers Bangalore',
 'over': '1', 'ball': '1', 'batsman': 'DA Warner', 'non_striker': 'S Dhawan', 'bowler': 'TS Mills', 'is_super_over': '0', 
 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 
 'batsman_runs': '0', 'extra_runs': '0', 'total_runs': '0', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}'''
with open('ipl_data/matches.csv',mode='r') as matches:
    match_details=csv.DictReader(matches)
    def find_2016_matches(match_):
        match_ids={}
        for match in match_details: 
            if match['season']=='2016':
                match_ids[match['id']]=True
        return match_ids
    match_ids=find_2016_matches(match_details)
with open('ipl_data/deliveries.csv',mode='r') as deliveries:
    deliveries_data=csv.DictReader(deliveries)


    def calculate_extra_runs_conceded_2016(deliveries_data):
        extra_runs_conceded={}
        for deliveries in deliveries_data:
            if deliveries['match_id'] in match_ids:
                if deliveries['bowling_team'] in extra_runs_conceded:
                    extra_runs_conceded[deliveries['bowling_team']]=extra_runs_conceded[deliveries['bowling_team']]+int(deliveries['extra_runs'])
                else:
                    extra_runs_conceded[deliveries['bowling_team']]=int(deliveries['extra_runs'])
        teams=list(extra_runs_conceded.keys())
        extra_runs=[]
        for team in teams:
            extra_runs.append(extra_runs_conceded[team])
        return teams,extra_runs
    teams,extra_runs=calculate_extra_runs_conceded_2016(deliveries_data)
    def plot():
        plt.bar(teams,extra_runs)
        plt.title("Extra_Runs_conceded_by_Teams_in_2016")
        plt.xlabel("Teams")
        plt.ylabel("Extra_Runs_Conceded")
        plt.xticks(rotation=20)
        plt.show()
    def execute():
        plot()
    execute()