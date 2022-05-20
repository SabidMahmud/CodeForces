def prime( num ) :
    flag = 1

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = 0
                break

    if flag == 0 :
        return False
    else:
        return True


n = int( input() )

for i in range( 2, n, 2 ) :
    x = i
    y = n - i
    if prime(x) is False and prime( y ) is False :
        if x + y == n :
            break

print( x, y )
