t = int(input())
while t > 0 :
    t-=1
    input()
    a = input().split()
    a = [ int(i) for i in a ]
    a2 = a.copy()
    a2.sort()
    spy = a2[0]
    for i in range( len(a2) ) :
        if a2[0] != a2[1] :
            spy = a2[0]
        if a2[-1] != a2[-2] :
            spy = a2[-1]
    
    index_of_spy = 1 + a.index(spy)
    print( index_of_spy )