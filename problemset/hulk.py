n = int( input() )
flag1 = "I love "
flag2 = "I hate "

for i in range(1, n+1) :
    if i%2 == 0 :
        if i== n :
            print( flag1 , end = "" )
        else :
            print( flag1 + "that", end = " " )
    else :
        if i == n :
            print( flag2 , end = "" )
        else :
            print( flag2 + "that", end = " " )

print( "it" )