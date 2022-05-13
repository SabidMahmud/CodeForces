# available notes : 100, 20, 10, 5, 1

money = int( input() )

available_bills = [ 100, 20, 10, 5, 1 ]

remaining_money = money
bills_received = 0

for i in available_bills :
    bills_received = bills_received + ( remaining_money // i )
    remaining_money = remaining_money % i

print( bills_received )
