k, r = input().split()
k = int( k )
r = int( r )
shovels = 0

while 1 :
    shovels += 1
    price = k * shovels
    if price % 10 == 0 or ( price - r ) % 10 == 0 :
        break

print( shovels )
