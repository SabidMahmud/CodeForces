# Codeforces 339A
p = input()
p = list( p.split("+") )
p = [int(i) for i in p]
p.sort()
p = [str(i) for i in p]
print( "+".join(p) )