import csv

with open('world_alcohol.csv', 'r') as csvfile:
    world_alcohol = list(csv.reader(csvfile))
    
years = [row[0] for row in world_alcohol][1:]

total = 0
for year in years:
    total += float(year);

avg_year = total / len(years)