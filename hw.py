import csv
import pandas as pd
stars=[]
with open('star_with_gravity.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        stars.append(row)


headers= stars[0]
planetdata=stars[1:]

headers[0]= 'Row_Number'

data = pd.read_csv('star_with_gravity.csv')

mass = data["Mass"].tolist()
radius = data["Radius"].tolist()

mass.pop(0)
radius.pop(0)
kg=[]

for i in mass:
    kg = i*(1.98855e+30)
print("kilo",kg)

for i in radius:
    meters=i*(1.496e+11)
print("meters",meters)

