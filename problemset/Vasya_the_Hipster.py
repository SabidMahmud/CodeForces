red_socks, yellow_socks = input().split()
red = int( red_socks )
yellow = int( yellow_socks )

if yellow < red :
    x = yellow
    y = ( red - yellow ) // 2
elif red < yellow :
    x = red
    y = ( yellow - red ) // 2
else :
    x = red
    y = 0

print( x, y )
