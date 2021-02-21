string = "The quick brown fox jumps over the lazy dog"

string_list = string.split()
print("\nList: ", string_list)

print("\nIndex of \"dog\": " + str(string_list.index("dog")))

string_list.sort(key = str.lower)
print("\nSorted List: ", string_list)

print("\nFirst two elements: ", string_list[0:2])

print("\nReversed List: ", string_list[::-1])
