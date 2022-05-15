guest = list( input() ) 
host = list( input() )
letters = list( input() )

expected_letters = guest + host

expected_letters.sort()
letters.sort()

# print( "Letters :", letters )
# print( "Expected Letters :", expected_letters )

if letters == expected_letters :
    print( "YES" )
else :
    print( "NO" )
