t = int( input() )
while t > 0 :
    t -= 1
    a, b = [ int(i) for i in input().split() ]
#     print( a, b )
    if a==b :
        print( 0 )
        continue
    else:
        if a > b :
            a,b = b,a
        
        res = 0
        sub = ( b - a)
        for i in range(10, 0, -1) :
            res = res + (sub // i)
            sub = sub % i
        
        print( res )