x = int(input('x= '))
y = int(input('y= '))
z = int(input('z= '))

if x + y + z == 2:
    sum = 0
else:
    sum = 1

if x + y + z != 1 or 0 :
    carry = 1
else:
    carry = 0

print('carry = ',carry)
print('sum = ', sum)
