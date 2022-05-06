# The elephant can move up to 5 position with single move
distance = int(input())
step = 5
count = 0
if distance <= 5 :
    count = 1
else :
    if distance % step != 0 :
        count = (distance // step)+1
    else :
        count = distance // step
print(count)
