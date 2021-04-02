from csv import DictReader

artists = []
with open('Artists.csv', 'r') as file:
    csv_dict_reader = DictReader(file)
    for row in csv_dict_reader:
        if row['DisplayName'] == 'Claude Monet' or row['DisplayName'] == 'Pablo Picasso':
            artists.append(row)
print(artists)
with open('output.txt', 'w') as file1:
    for line in artists:
        file1.write(str(line) + '\n')
file1.close()
