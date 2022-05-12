n = int( input() )
string = input()
string = string.lower()
string = list( string )

string = set( string )

if len( string ) == 26 :
    print( "YES" )
else :
    print( "NO" )
