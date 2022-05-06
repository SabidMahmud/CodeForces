year = int(input())
while True :
    year += 1
    unique_year = set(str(year))
    if len(unique_year) == len(str(year)) :
        print(year)
        break
    else :
        continue
    