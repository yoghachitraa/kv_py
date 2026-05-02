#Find sum of first N natural numbers.
n = int ( input ( ' n :'))
sum = 0 
for i in range ( 1 , n+1 ) :
        sum = sum + i
print ( f' sum of {n} natural numbers is {sum}')
