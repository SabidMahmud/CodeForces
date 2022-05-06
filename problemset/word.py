word = input()
uppercase = 0
lowercase = 0
for letter in word :
    if letter == letter.upper() :
        uppercase += 1
    else :
        lowercase += 1

if uppercase > lowercase :
    print(word.upper())
else :
    print( word.lower() )