number = int( input() )
lucky_number = 0
nearly_lucky = 0
for i in str(number) :
    if i == '7' or i == '4' :
        lucky_number += 1

if lucky_number == 4 or lucky_number == 7 :
    nearly_lucky = 1

if nearly_lucky == 1:
    print( 'YES' )
else :
    print( 'NO' )