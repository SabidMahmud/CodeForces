n = int( input() )
points = list( input().split() )
points = [ int( x ) for x in points ]

# print( points )

maximum = points[0]
minimum = points[0]
res = 0

for i in points :
    if i < minimum :
        res += 1
        minimum = i
    elif i > maximum :
        res += 1
        maximum = i

print( res )
        
