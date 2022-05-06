n = int( input() )
room = 0
while n > 0 :
    p, q = input().split()
    p, q = int(p), int(q)
    sit_available = q - p
    if sit_available >= 2 :
        room += 1
    # else :
    #     continue
    n = n - 1

print(room)