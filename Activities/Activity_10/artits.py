# Modify your code to look for lines that contain either of the following artists: Pablo Picasso or Claude Monet and
# print only those two lines out.
# Return the two rows in a separate file called output.txt
# Bonus: Remove the two above lines from Artists.csv and save the new file as Artists2.csv separately.

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
