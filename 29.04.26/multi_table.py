#Print multiplication table of a number
n = int ( input ( 'enter a number:'))
print ( f' {n} table:')
for i in range ( 1 ,13 ):
    print (f' {i} x {n} = {i*n}')
