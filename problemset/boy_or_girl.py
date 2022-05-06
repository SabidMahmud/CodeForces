def remove_duplicates(username):
    return "".join(set(username.lower()))

username = input()
username_after = remove_duplicates(username)
# print( remove_duplicates( username ) )

length = len(username_after)
# print(length)

if length % 2 == 0 :
    flag = 0
else :
    flag = 1

if flag == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
