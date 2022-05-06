n, k = input().split()
n = int(n)
for i in range( int(k) ) :
    if n % 10 == 0 :
        n = n / 10
    else :
        n = n-1

print( int(n) )