# Codeforces 1367A. [Short substrings]
n = int(input())
while n > 0 :
    n -= 1
    b = list( input() )
    i = 1
    while i < len(b)-1 :
        if b[i] == b[i+1] :
            b.pop(i)
        i += 1
        # print( b )

    print( "".join(b) )

