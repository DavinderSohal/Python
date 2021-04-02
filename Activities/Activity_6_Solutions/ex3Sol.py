#Activity 6 - Exercise 3 Solution

n = input("Enter a number: ")
x = str(n)
k = len(x)
ans = []
for c in x:
    ans.append(c)
    k -= 1
    if k and k % 3 == 0:
        ans.append('.')
print("".join(ans))       
