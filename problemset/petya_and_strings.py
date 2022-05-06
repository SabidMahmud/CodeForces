string1 = input()
string2 = input()

if string1.lower() == string2.lower():
    res = 0
elif string1.lower() < string2.lower() :
    res = -1
else :
    res = 1

print(res)
