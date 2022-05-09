num1 = list( input() )
num2 = list( input() )

result = []

i = 0
while i < len(num1) :
    if num1[i] != num2[i] :
        result.append( 1 )
    else :
        result.append( 0 )
    i+=1

print( *result, sep="")
