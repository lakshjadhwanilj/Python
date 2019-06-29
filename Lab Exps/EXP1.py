#FIRST
print("""Twinkle, twinkle, little star,
    \"How I wonder what you are!\"
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, \'twinkle\', little star,
    How I wonder what you are.""")

#SECOND
x = int(input('Enter 1st Number: '))
y = int(input('Enter 2nd Number: '))
sum = x + y
print('{} + {} = {}'.format(x,y,sum))
print('%d + %d = %d'%(x,y,sum))

#THIRD
year = int(input('Enter Year: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('{} is A Leap Year'.format(year))
        else:
            print('{} is Not A Leap Year'.format(year))
    else:
        print('{} is A Leap Year'.format(year))
else:
    print('{} is Not A Leap Year'.format(year))

#FOURTH
print('List of Armstrong Numbers is:')
for i in range(100,1000):
    temp = i
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit**3
        temp = temp // 10
    if sum == i:
        print(i)

#FIFTH
n = int(input('Enter A Number: '))
a = 1
b = 1
print(a)
print(b)
for i in range(n - 2):
    c = a + b
    print(c)
    a = b
    b = c

#SIXTH
n = int(input('Enter A Number: '))
c = 'A'
for i in range(n):
    print(c * (i + 1))
    d = ord(c)
    d += 1
    c = chr(d)

n = int(input('Enter A Number: '))
for i in range(n):
    print(" " * i,"*" * (n-i))

n = int(input('Enter A Number: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end = "")
    for k in range(1, i + 1):
        print(k, end = "")
    for j in range(i - 1,0,-1):
        print(j, end = "")
    print()

n = int(input('Enter A Number: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end = "")
    for k in range(i):
        print("* ", end = "")
    print()