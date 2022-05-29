n, h = input().split()
h = int(h)
a = list( input().split() )
a = [ int(x) for x in a ]
width = 0
for i in a :
    if i > h :
        width += 2
    else :
        width += 1

print( width )