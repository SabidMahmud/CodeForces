n = int(input())
for i in range(n) :
    word = input()
    length = len(word)
    if length > 10 :
        first = word[0]
        x = len(word)
        last = word[x-1]
        shrinked = word[1:x-1]
        how_long = len(shrinked)
        print( first + str(how_long) + last )
    else :
        print( word )

quit()
