n = int( input() )
x = list( input().split() )
y = list( input().split() )

x_can_pass = x[1:]
y_can_pass = y[1:]

total = x_can_pass + y_can_pass
total = [ int(i) for i in total ]
total_passed = set( total )

# levels = [ int(i) for i in range(1, n+1) ]

if len( total_passed ) == n :
    print("I become the guy.")
else :
    print( "Oh, my keyboard!" )
