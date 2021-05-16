s = input("\nEnter any string: ")

while True:
    i = int(input("Enter any number: "))
    if i < 0 or i > len(s):
        print(f"\n------- Invalid entry! enter value less than or equal to {len(s)} only -------\n")
    else:
        break

vowels_list = []
for x in range(len(s) - i + 1):
    vowels_count = 0
    substring = s[x:(x + i)]
    for char in range(i):
        if substring[char] == "a" or substring[char] == "e" or substring[char] == "i" or substring[char] == "o" or \
                substring[char] == "u":
            vowels_count += 1
        vowels_list.append(vowels_count)

most_vowels = 0
if not len(vowels_list) == 0:
    most_vowels = max(vowels_list)

print("\nMost number of vowels: ", most_vowels)
