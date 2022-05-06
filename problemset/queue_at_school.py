a, x = input().split()
a, x = int(a), int(x)
q = input()
q = list( q )

while x > 0 :
    i = 0
    while i < len(q)-1 :
        if q[i] == "B" and q[i+1] == "G" :
            q[i], q[i+1] = q[i+1], q[i]
            i += 1
        i += 1
    x -= 1

print( "".join(q) )