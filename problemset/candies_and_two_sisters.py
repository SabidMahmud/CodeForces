t = int( input() ) #test cases 

# Alice will get a candies and Betty will get b candies
# a > 0
# b > 0
# a+b = n
# a > b

while t > 0 :
    n = int( input() ) # Number of candies 
    if n < 3 :
        ways = 0
    elif n >= 3 and n <= 2*10**9 :
        if n % 2 == 0 :
            ways = ( n / 2 ) - 1
        else :
            ways = ( n - 1 ) / 2

    t -= 1
    print( int(ways) )
