"""
Exercise: Using the following sentence:
	“The quick brown fox jumps over the lazy dog”,
	 convert this string into a list and then find the index of the word dog and sort the list of terms/words in
	 ascending order. Print out the first two elements of this sorted list. Additionally, as a bonus, try to reverse
	 the list of words using the slice operation.
Hint: Use split() method!
"""

string = "The quick brown fox jumps over the lazy dog"

string_list = string.split()
print("\nList: ", string_list)

print("\nIndex of \"dog\": " + str(string_list.index("dog")))

string_list.sort(key = str.lower)
print("\nSorted List: ", string_list)

print("\nFirst two elements: ", string_list[0:2])

print("\nReversed List: ", string_list[::-1])
