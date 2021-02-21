#Lists have exactly the same operators as strings:
#+, +=, *, *=, [], ==, !=, <, <=, >, >=, in


l = [1,2,3,4]
print(l + [5,6])
l += [5,6]
print(l)
print(3 in l)
print(l > [5,6])
int([5,6] * 3)

