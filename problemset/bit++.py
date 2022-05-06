n = int( input() )
x_pos = 0
x_neg = 0
for i in range(n):
    write = input()
    if "++" in write and "X" in write:
        x_pos += 1
    elif "--" in write and "X" in write:
        x_neg -= 1

x = x_pos + x_neg
print(x)
    
