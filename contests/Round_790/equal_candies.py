t = int( input() )

while t > 0 :
    n = int( input() )
    candies = list( input().split() )
    candies = [int(x) for x in candies]
    
    minimum = min( candies )
    
    to_eat = 0
    
    for i in range( n ) :
        to_eat = to_eat + ( candies[i] - minimum )

    print( to_eat )
    t -= 1
