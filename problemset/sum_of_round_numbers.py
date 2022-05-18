t = int( input() )

while t > 0 :
    t -= 1
    n = int( input() )
    result = []
    for i in range( 6 ) :
        rem = n % ( 10**i )
        if rem != 0 :
            result.append(rem)
        n -= rem
    
    out = [ str(i) for i in result ]
    print( len(result) )
    print( " ".join( out ) )
