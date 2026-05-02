# to find factorial of n
n = int (input('n :')) 
fact = 1
for I in range(n,0,-1):
    fact = fact * I 
print(f'fact of {n} is {fact}')