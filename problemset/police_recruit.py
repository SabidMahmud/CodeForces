n = int( input() )
cases = list( input().split() )
cases = [ int( i ) for i in cases ]

cops = 0
unresolved = 0

for i in cases :
    if i == -1 :
        if cops > 0 :
            cops -= 1
        else :
            unresolved += 1
    else :
        cops += i

print( unresolved )
