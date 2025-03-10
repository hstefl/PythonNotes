import csv

with open('subjects.csv', 'w', newline='') as csvfile:
    # fieldnames = ['Name']
    writer = csv.DictWriter(csvfile)

    writer.writeheader()
    writer.writerow({'Name': 'math'})
    writer.writerow({'Name': 'chemistry'})
