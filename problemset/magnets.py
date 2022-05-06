from re import I


n = input()
n = int(n)

group = 1

previous = input()
while n > 1 :
    i = input()
    if previous != i :
        group = group + 1
        previous = i    
    n -= 1

print(group)