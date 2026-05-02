#10, 13, 17, 22, 28, 35, ... for 6 terms
n = int(input('n:'))
term = 10
diff = 3
print('series:')
for i in range (n):
    print(term,end=' ') 
    term = term + diff
    diff = diff + 1 