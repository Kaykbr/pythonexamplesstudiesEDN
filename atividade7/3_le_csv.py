import csv

with open('pessoas.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            print(f'{row[0]:<20} {row[1]:<10} {row[2]:<20}')
            print('-'*50)
        else:
            print(f'{row[0]:<20} {row[1]:<10} {row[2]:<20}')
