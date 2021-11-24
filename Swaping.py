x = input()
y = input()

print('The value of x is {}'.format(x))
print(f'The value of x is {x}')

print('The value of y is {}'.format(y))
print(f'The value of y is {y}')

temp_var = x

x = y

y = temp_var

print('The value of x after swapping is {}'.format(x))
print(f'The value of x is {x}')

print('The value of y after swapping is {}'.format(y))
print(f'The value of y after swapping is {y}')