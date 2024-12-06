import matplotlib.pyplot as plt
import csv
'''{'Sunrisers Hyderabad': True, 'Royal Challengers Bangalore': True, 'Mumbai Indians': True, 
     'Rising Pune Supergiant': True, 'Gujarat Lions': True, 'Kolkata Knight Riders': True,
       'Kings XI Punjab': True, 'Delhi Daredevils': True, 'Chennai Super Kings': True, 'Rajasthan Royals': True,
         'Deccan Chargers': True, 'Kochi Tuskers Kerala': True, 'Pune Warriors': True, 'Rising Pune Supergiants': True}'''
with open('ipl_data/matches.csv',mode='r') as matches:
    matches_file=csv.DictReader(matches)

    index={}
    index['Royal Challengers Bangalore']=0
    index['Sunrisers Hyderabad']=1
    index['Mumbai Indians']=2
    index['Rising Pune Supergiant']=3
    index['Gujarat Lions']=4
    index['Kolkata Knight Riders']=5
    index['Kings XI Punjab']=6
    index['Chennai Super Kings']=7
    index['Rajasthan Royals']=8
    index['Kochi Tuskers Kerala']=9
    index['Pune Warriors']=10
    index['Delhi Daredevils']=11
    index['Deccan Chargers']=12
    index['Rising Pune Supergiants']=3
    teams=['Royal Challengers Bangalore','Sunrisers Hyderabad','Mumbai Indians','Rising Pune Supergiant','Gujarat Lions',
        'Kolkata Knight Riders','Kings XI Punjab','Chennai Super Kings','Rajasthan Royals','Kochi Tuskers Kerala','Pune Warriors','Delhi Daredevils',
        'Deccan Chargers']
    
    def match_data(matches_file):
        matches=[0]*10
        data=[]
        for season in range(0,13):
            data.append(matches[:])
        
        
        for matches in matches_file:
            data[index[matches['team1']]][int(matches['season'])-2008]=data[index[matches['team1']]][int(matches['season'])-2008]+1
            data[index[matches['team2']]][int(matches['season'])-2008]=data[index[matches['team2']]][int(matches['season'])-2008]+1

        return data
    def plot():
        data=match_data(matches_file)
 
        color={}
        color[0]='#B22222'
        color[1]='#FFA500'
        color[2]="#4169E1"
        color[3]="#9370DB"
        color[4]="#FF7F24"
        color[5]="#6A5ACD"
        color[6]="#FF2400"
        color[7]="#FFD300"
        color[8]="#0F52BA"
        color[9]="#E34234"
        color[10]="#008080"
        color[11]="#DC143C"
        color[12]="#8A8A8A"


        season=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
        bottom=[0,0,0,0,0,0,0,0,0,0]
        for i in range(0,len(data)):
            plt.bar(season,data[i],label=teams[i],bottom=bottom,color=color[i])
            for j in range(0,len(bottom)):
                bottom[j]=bottom[j]+data[i][j]
        plt.legend(loc='upper left', fontsize='small', bbox_to_anchor=(1, 1), title="Teams")
        plt.title("Matches Played by Team by Season")
        plt.xlabel("Season")
        plt.ylabel("Matches Played")
        plt.show()
    plot()