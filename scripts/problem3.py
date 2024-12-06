import csv
import matplotlib.pyplot as plt
with open('Umpires_data/umpires.csv',mode='r') as umpires:
    umpires_file=csv.DictReader(umpires)
    def umpires_count_by_country(umpires_file):
        country={}
        for umpire in umpires_file:
            if umpire[' country']==' India':
                continue
            elif umpire[' country'] in country:
                country[umpire[' country']]=country[umpire[' country']]+1
            else:
                country[umpire[' country']]=1
        country_name=[]
        umpires_count=[]
        for name in country:
            country_name.append(name)
            umpires_count.append(country[name])
        return country_name,umpires_count
    def plot():
        country,umpires_count=umpires_count_by_country(umpires_file)
        plt.bar(country,umpires_count)
        plt.title("Count of IPL Umpires by Country")
        plt.xlabel("Country")
        plt.ylabel("Count")
        plt.xticks(rotation=20, ha='right', fontsize=10)
        plt.show()
    def execute():
        plot()
    execute()