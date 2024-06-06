a = int(input('a= '))
b = int(input('b= '))
if a and b == 1:
    carry = 1
else:
    carry = 0

if 0< a + b < 2:
    sum = 1
else:
    sum = 0

print('carry = ',carry)
print('sum = ',sum)
