n, k = input().split()
n = int(n)
k = int(k)
scores = input().split() 

# print(scores)

count = 0
kth_score = int(scores[k-1])
for i in scores :
    if int(i) >= kth_score and int(i) > 0 :
        count += 1

print(count)
