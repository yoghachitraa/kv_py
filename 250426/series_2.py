#1,4,7,10,13,16,19,22,25,28, .... for 10 terms
n = int(input('n:'))
term = 1
print('series:')
for i in range (n):
    print(term,end=' ') 
    term = term + 3