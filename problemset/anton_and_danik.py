n = int(input())
s = input()
if len(s) == n :
    A = 0
    D = 0
    for i in s :
        if i == "A" :
            A += 1
        elif i == "D" :
            D += 1

if A == D :
    print("Friendship")
elif A > D :
    print("Anton")
else :
    print("Danik")