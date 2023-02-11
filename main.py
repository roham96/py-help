import csv
import random

with open('list.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print("Name: {}   Number: {}".format(row[0],random.randint(1,70)))