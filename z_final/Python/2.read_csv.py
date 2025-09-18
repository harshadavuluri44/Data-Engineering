import csv
with open('data/e.csv', mode='r') as file_content:
    reader = csv.DictReader(file_content)

    d = {}
    for row in reader:
        d[row['name']]=int(row['salary'])

print(d)