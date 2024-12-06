import matplotlib.pyplot as plt
import csv
with open('ipl_data/matches.csv',mode='r') as matches:
    matches_file=csv.DictReader(matches)
    def matches_per_year(matches_file):
        seasons=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
        matches_played=[0,0,0,0,0,0,0,0,0,0]
        for match in matches_file:
            matches_played[int(match['season'])-2008]=matches_played[int(match['season'])-2008]+1
        return seasons,matches_played
    def plot():
        seasons,matches_played=matches_per_year(matches_file)
        plt.bar(seasons,matches_played)
        plt.title("Total Number of Matches Played Per Year")
        plt.xlabel("Seasons")
        plt.ylabel("Total Matches Played")        
        plt.show()
    def execute():
        plot()
    execute()