
file = open('students.csv')

lines = file.readlines()

for line in lines:
    values = line.split(',')
    print(values[2], values[3])

