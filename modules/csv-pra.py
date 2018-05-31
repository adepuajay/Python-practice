import csv

with open('small.csv') as csvfile:
    my_csv_file = csv.reader(csvfile, delimiter=';')
    for row in my_csv_file:
        print(row)
