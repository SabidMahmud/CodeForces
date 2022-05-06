# def f( n ) :
    # result = 0
    # counter = 0
    # while counter < n:
        # result += ((-1) ** n) * n
        # counter += 1

    # return result

n = int( input() )
result = 0
for i in range(1,n+1) :
    result = result + ((-1)**i)*i

print( result )
