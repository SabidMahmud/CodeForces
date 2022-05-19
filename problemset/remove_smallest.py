testcases = int( input() )
while testcases > 0 :
    testcases -= 1
    
    input()
    num = list( int(x) for x in input().split() )
    a = list(set(num))
    a.sort()
    # print(a)

    if len( a ) == 1 :
        print("YES")
        continue

    case = 0
    for i in range( len(a) - 1 ) :
        if (a[i]+1) != a[i+1] :
            case += 1
            print("NO")
            break

    if case == 0 :
        print("YES")