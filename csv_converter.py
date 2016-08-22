import json
import csv

raw_data = open("data.json")

data = json.loads(raw_data.read())

csv_file = open("data.csv", 'wb')

fieldnames = ['W', 'l', 'x', 'y']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

for chunk in data:
    for l in chunk["data"]:
        for n in l["data"]:
            writer.writerow({'W': chunk["W"], 'l': l["l"], 'x': n[0], 'y': n[1]})
