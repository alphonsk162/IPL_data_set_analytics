import csv

import matplotlib.pyplot as plt

with open('ipl_data/deliveries.csv',mode='r') as deliveries:
    deliveries_file=csv.DictReader(deliveries)

    '''
    for ball in deliveries_file:
        if ball['batting_team'] in teams:
            continue
        else:
            teams[ball['batting_team']]=True'''
    '''{'match_id': '1', 'inning': '1', 'batting_team': 'Sunrisers Hyderabad', 'bowling_team': 'Royal Challengers Bangalore', 
    'over': '1', 'ball': '1', 'batsman': 'DA Warner', 'non_striker': 'S Dhawan', 'bowler': 'TS Mills', 
    'is_super_over': '0', 'wide_runs': '0', 'bye_runs': '0', 'legbye_runs': '0', 'noball_runs': '0', 'penalty_runs': '0', 
    'batsman_runs': '0', 'extra_runs': '0', 'total_runs': '0', 'player_dismissed': '', 'dismissal_kind': '', 'fielder': ''}'''
    def runs_by_rcbbatsman():
        rcb_batsman={}
        for ball in deliveries_file:
            if ball['batting_team']=='Royal Challengers Bangalore':
                if ball['batsman'] in rcb_batsman:
                    rcb_batsman[ball['batsman']]=rcb_batsman[ball['batsman']]+int(ball['batsman_runs'])
                else:
                    rcb_batsman[ball['batsman']]=int(ball['batsman_runs'])

        return rcb_batsman
    runs_by_rcbbatsman=runs_by_rcbbatsman()
    def find_top_10(runs_by_rcbbatsman):
        rcb_batsman=[]
        runs_by_batter=[]
        for batter in runs_by_rcbbatsman:
            rcb_batsman.append(batter)
            runs_by_batter.append(runs_by_rcbbatsman[batter])
        for i in range(0,len(runs_by_batter)-1):            
            for j in range(i+1,len(runs_by_batter)):
                if runs_by_batter[i]<runs_by_batter[j]:
                    rcb_batsman[i],rcb_batsman[j]=rcb_batsman[j],rcb_batsman[i]
                    runs_by_batter[i],runs_by_batter[j]=runs_by_batter[j],runs_by_batter[i]
        return rcb_batsman[:10],runs_by_batter[:10]

    top_10_batters,runs_by_top_10=find_top_10(runs_by_rcbbatsman)
    def plot():
        plt.bar(top_10_batters, runs_by_top_10)

        # Customize the plot
        plt.title("Players with most runs for RCB")
        plt.xlabel("Player")
        plt.ylabel("Runs")
        plt.xticks(rotation=20, ha='right', fontsize=10)

        # Display the plot
        plt.show()
    def execute():
        plot()
execute()
        
        
