#1,  4,  9,  16,  25,... for 5 terms 
n = int(input('n:'))
term = 1
diff = 1
print('series:')
for i in range (n):
    print(term,end=' ') 
    diff = diff + 1 
    term = diff ** 2