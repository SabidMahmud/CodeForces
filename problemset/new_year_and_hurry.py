total_time = 4 * 60

n, k = input().split()
n, k = int(n), int(k)

time = 0
can_solve = 0

for i in range( 1, n+1 ) :
    time += 5 * i
    time_spent = time + k
    if time_spent <= total_time :
        can_solve += 1
        continue
    else :
        break

print( can_solve )
