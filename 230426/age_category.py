age = int ( input ( ' age : ' ))
if age <= 12 :
    category = 'child'
elif age <= 19 :
    category = ' teen'
elif age <= 40 :
    category = ' adult'
elif age <= 60 :
    category = ' middle aged'
elif age <= 80 :
    category = ' senior citizen'
else :
    category = ' super senior citizen'

print ( f' age : {age}')
print ( f' category : {category}')

