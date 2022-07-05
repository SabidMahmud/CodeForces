n, k, l, c, d, p, nl, np = input().split()
n = int(n)
drinks = int(k) * int(l)
limes = int(c)*int(d)
salt = int(p)
nl = int(nl)
np = int(np)
max_drink = drinks // nl
max_lime = limes // 1
max_salt = salt // np

each_friend_can_make = min(max_drink, max_lime, max_salt)//n
print( each_friend_can_make )