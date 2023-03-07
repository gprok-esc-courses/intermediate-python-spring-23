import csv

file = open('students.csv')

reader = csv.reader(file, delimiter=',')

for row in reader:
    print(row[2], row[3])

