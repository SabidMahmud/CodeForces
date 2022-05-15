n, m = input().split()
n = int(n)
m = int( m )

a = "#" * m
b = "." * (m-1)
c = "#"
for i in range(1, n+1) :
    if i % 2 != 0 :
        print( a )
    else :
        print( b + c )
        temp = b
        b = c
        c = temp


