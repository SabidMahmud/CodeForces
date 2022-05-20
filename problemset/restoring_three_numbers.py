numbers = list( int(i) for i in input().split() )

numbers.sort()

p, q, r, s = numbers

# p = a + b
# q = a + c
# r = b + c
# s = a + b + c

a = s - r
b = s - q
c = s - p
print( a, b, c)