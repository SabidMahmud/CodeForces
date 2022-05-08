n = int( input() )
li = list( input().split() )
orange = [int(i) for i in li]

total = 0
for i in orange :
    total += i

percent = total / len( orange )
print( percent )
