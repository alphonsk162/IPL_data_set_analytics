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
    '''{'Sunrisers Hyderabad': True, 'Royal Challengers Bangalore': True, 'Mumbai Indians': True, 
     'Rising Pune Supergiant': True, 'Gujarat Lions': True, 'Kolkata Knight Riders': True,
       'Kings XI Punjab': True, 'Delhi Daredevils': True, 'Chennai Super Kings': True, 'Rajasthan Royals': True,
         'Deccan Chargers': True, 'Kochi Tuskers Kerala': True, 'Pune Warriors': True, 'Rising Pune Supergiants': True}'''
    def calculate_total_runs():
        rcb_total_runs=0
        srh_total_runs=0
        mi_total_runs=0
        rps_total_runs=0
        gl_total_runs=0
        kkr_total_runs=0
        kxip_total_runs=0
        csk_total_runs=0
        rr_total_runs=0
        kt_total_runs=0
        pw_total_runs=0
        dd_total_runs=0
        dc_total_runs=0

    
        for ball in deliveries_file:
            if ball['batting_team']=='Royal Challengers Bangalore':
                rcb_total_runs=rcb_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Sunrisers Hyderabad':
                srh_total_runs=srh_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Mumbai Indians':
                mi_total_runs=mi_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Rising Pune Supergiant' or ball['batting_team']=='Rising Pune Supergiants':
                rps_total_runs=rps_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Gujarat Lions':
                gl_total_runs=gl_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Kolkata Knight Riders':
                kkr_total_runs=kkr_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Kings XI Punjab':
                kxip_total_runs=kxip_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Delhi Daredevils':
                dd_total_runs=dd_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Chennai Super Kings':
                csk_total_runs=csk_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Rajasthan Royals':
                rr_total_runs=rr_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Kochi Tuskers Kerala':
                kt_total_runs=kt_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Pune Warriors':
                pw_total_runs=pw_total_runs+int(ball['total_runs'])
            elif ball['batting_team']=='Deccan Chargers':
                dc_total_runs=dc_total_runs+int(ball['total_runs'])
        runs_by_each_team=[srh_total_runs,rcb_total_runs,mi_total_runs,
                rps_total_runs,gl_total_runs,kkr_total_runs,
                kxip_total_runs,dd_total_runs,csk_total_runs,rr_total_runs,
                dc_total_runs,kt_total_runs,pw_total_runs]
        return runs_by_each_team
    def plot():
        teams=['Sunrisers Hyderabad', 'Royal Challengers Bangalore', 'Mumbai Indians', 
            'Rising Pune Supergiant', 'Gujarat Lions', 'Kolkata Knight Riders',
            'Kings XI Punjab', 'Delhi Daredevils', 'Chennai Super Kings', 'Rajasthan Royals',
            'Deccan Chargers', 'Kochi Tuskers Kerala', 'Pune Warriors']
        runs_by_each_team=calculate_total_runs()
        plt.bar(teams, runs_by_each_team)

        # Customize the plot
        plt.title("Total Runs by Team")
        plt.xlabel("Teams")
        plt.ylabel("Runs")
        plt.xticks(rotation=20, ha='right', fontsize=10)

        # Display the plot
        plt.show()
    def execute():
        plot()
    execute()
    
        
