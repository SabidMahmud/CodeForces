t = int( input() )

while t > 0 :
    a, b = input().split()
    a = int(a)
    b = int(b)
    
    # counter = 0
    # while True:
        # if a % b != 0 :
            # a+=1
            # counter+=1
        # else :
            # break

    if a % b == 0 :
        count = 0
    else :
        count = b - ( a % b )
        
    print( count )
    t-=1

