#100,95, 85, 70, 50, 25, ... for 6 terms   
n = int(input('n:'))
term = 100
diff = 5
print('series:')
for i in range (n):
    print(term,end=' ') 
    term = term - diff
    diff = diff + 5

