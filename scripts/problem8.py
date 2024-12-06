import matplotlib.pyplot as plt
import csv
with open('ipl_data/matches.csv',mode='r') as matches:
    matches_file=csv.DictReader(matches)
    def matches_2015(matches_file):
        match_id={}
        for match in matches_file:
            if match['season']=='2015':
                match_id[match['id']]=True
        return match_id
    match_id=matches_2015(matches_file)
with open('ipl_data/deliveries.csv',mode='r') as deliveries:
    deliveries_file=csv.DictReader(deliveries)
    bowlers={}

    def economical_bowlers_2015(deliveries_file):
        for deliveries in deliveries_file:
            if deliveries['match_id'] in match_id:
                if deliveries['bowler'] in bowlers:
                    if deliveries['wide_runs']=='0' and deliveries['noball_runs']=='0':
                        bowlers[deliveries['bowler']][0]=bowlers[deliveries['bowler']][0]+1
                        bowlers[deliveries['bowler']][1]=bowlers[deliveries['bowler']][1]+int(deliveries['batsman_runs'])
                    else:
                        bowlers[deliveries['bowler']][1]=bowlers[deliveries['bowler']][1]+int(deliveries['batsman_runs'])+int(deliveries['wide_runs'])+int(deliveries['noball_runs'])
                    
                else:
                    bowlers[deliveries['bowler']]=[0,0]
                    if deliveries['wide_runs']=='0' and deliveries['noball_runs']=='0':
                        bowlers[deliveries['bowler']][0]=bowlers[deliveries['bowler']][0]+1
                        bowlers[deliveries['bowler']][1]=bowlers[deliveries['bowler']][1]+int(deliveries['batsman_runs'])
                    else:
                        bowlers[deliveries['bowler']][1]=bowlers[deliveries['bowler']][1]+int(deliveries['batsman_runs'])+int(deliveries['wide_runs'])+int(deliveries['noball_runs'])
        bowlers_name=list(bowlers.keys())
        economy=[]
        for name in bowlers_name:
            economy.append((bowlers[name][1]*6)/bowlers[name][0])
        for i in range(0,len(economy)-1):
            for j in range(i+1,len(economy)):
                if economy[i]>economy[j]:
                    economy[i],economy[j]=economy[j],economy[i]
                    bowlers_name[i],bowlers_name[j]=bowlers_name[j],bowlers_name[i]
        return bowlers_name[:10],economy[:10]
    economical_bowlers,economy=economical_bowlers_2015(deliveries_file)
    def plot():
        plt.bar(economical_bowlers,economy)
        plt.title("Economical Bowlers in the Year 2015")
        plt.xlabel("Bowlers")
        plt.ylabel("Economy")
        plt.xticks(rotation=30)
        plt.show()
    def execute():
        plot()
    execute()