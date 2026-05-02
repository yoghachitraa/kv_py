#0,1,1,2,3,5,8,13, .... for 8 terms 
n = int(input('n:'))
first = 0 
second = 1

print('series:')
for i in range (n):
    print(first,end=' ') 
    third = first + second
    first = second 
    second = third