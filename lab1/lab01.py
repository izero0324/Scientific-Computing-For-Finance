# Lab exercises

# Hello world - variable
hw_msg = "Hello World"
print(hw_msg)
print('\n')

# One variable, two messages
ov_tm = "message"
print(ov_tm)
ov_tm = "new message"
print(ov_tm)
print('\n')

# Someone said
quote = 'One of my most productive days was throwing away 1000 lines of code'
print("Ken Thompson once said, '"+ quote + "'")
print('\n')

# First name cases
my_name = "chia hung"
print('lower case: ',my_name.lower(), '\nTitle case: ', my_name.title(), '\nUPPER CASE: ', my_name.upper())
print('\n')

# FUll name
my_last_name = "Yang"
print(my_name.title(), my_last_name)
print('\n')

# About this person
sb_FN = "Steven"
sb_LN = "Jobs"
sentence = sb_FN +' ' + sb_LN + ' is brillent!!!'
print(sentence)
print('\n')

# Name strip
my_name_for_strip = ' ' + my_name + ' '
print(my_name_for_strip)
print(my_name_for_strip.lstrip())
print(my_name_for_strip.rstrip())
print(my_name_for_strip.strip())
print('\n')

# Arithmetic
a = 3
b = 5
print('addition:', a, '+', b , '=', a + b)
print('subtraction:', a, '-', b , '=', a - b)
print('multiplication:', a, 'x', b , '=', a * b)
print('division: ', a, '/', b , '=', a / b)
print('exponentiation: ', a, 'exponential', b , '=', a ** b)
print('\n')

# Order of operations
c = 2
print('a + b x c = ', a + b * c)
print('(a + b) * c = ', (a + b) * c)
print('\n')

# Long decimals
print("0.1+0.1+0.1-0.3 = ", 0.1+0.1+0.1-0.3)
print('\n')

# Incrementing a value
zero = 0
print(zero)
zero += 1
print(zero)
for i in range(3):
    zero +=1
print(zero)
print('\n')

# Fibonacci sequence
x = 0
y = 1
z = x+y
print(z)
z1 = y+z
print(z1)
z2 = z+z1
print(z2)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))