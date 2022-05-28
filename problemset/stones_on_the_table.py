# https://codeforces.com/problemset/problem/266/A
input()
colour = list(input())
result = 0
i = 0
while i < len(colour)-1 :
    if colour[i] == colour[i+1] :
        del colour[i]
        result+=1
        i -=1
    i+=1

print( result )