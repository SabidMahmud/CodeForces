testcases = int( input() )

while testcases > 0 :
    testcases = testcases - 1

    ticket = input()
    ticket = [int(x) for x in ticket]

    half1 = ticket[0] + ticket[1] + ticket[2]
    half2 = ticket[3] + ticket[4] + ticket[5]

    if half1 == half2 :
        print( "YES" )
    else :
        print( "NO" )
