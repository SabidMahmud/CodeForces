x = list( int(i) for i in input().split() )
x.sort()

a, b, c = x

print( b - a + c - b )
