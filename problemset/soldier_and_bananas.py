k, n, w = input().split()
k, n, w = int(k), int(n), int(w)
pay = 0
for i in range(1, w+1) :
    price = k * i
    pay += price

if pay > n :
    borrow = pay - n
else :
    borrow = 0

print( borrow )