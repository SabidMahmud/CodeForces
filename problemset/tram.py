n = int(input())
passenger = []
x = 0
count = 0
while count < n:
    a, b = input().split()
    x = x + int(b) - int(a)
    passenger.append(x)
    count += 1

min_pas = 0
for i in range(n) :
    if passenger[i] > min_pas :
        min_pas = passenger[i]

print(min_pas)