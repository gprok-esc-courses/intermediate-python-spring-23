import csv

file = open('students.csv')

reader = csv.DictReader(file, delimiter=',')

for row in reader:
    print(row['First Name'], row['Last Name'])

