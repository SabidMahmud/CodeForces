n = int(input())
opinion = list( input().split() )
easy = None
if len(opinion) == n :
    opinion = set(opinion)
    for i in opinion :
        if i == '0' and len(opinion) == 1 :
            easy = 1
        else :
            easy = 0

if easy == 1 :
    print("EASY")
else :
    print("HARD")