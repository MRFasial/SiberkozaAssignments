# If/ Else conditions are used to decide to do something based on something being true or false

x_mr = 21
y_mr = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_mr > y_mr:
  print(f'{x_mr} is greater than {y_mr}')

# If/else
if x_mr > y_mr:
  print(f'{x_mr} is greater than {y_mr}')
else:
  print(f'{y_mr} is greater than {x_mr}')  

# elif
if x_mr > y_mr:
  print(f'{x_mr} is greater than {y_mr}')
elif x_mr == y_mr:
  print(f'{x_mr} is equal to {y_mr}')  
else:
  print(f'{y_mr} is greater than {x_mr}')  

# Nested if
if x_mr > 2:
  if x_mr <= 10:
    print(f'{x_mr} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_mr > 2 and x_mr <= 10:
    print(f'{x_mr} is greater than 2 and less than or equal to 10')

# or
if x_mr > 2 or x_mr <= 10:
    print(f'{x_mr} is greater than 2 or less than or equal to 10')

# not
if not(x_mr == y_mr):
  print(f'{x_mr} is not equal to {y_mr}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_mr = [1,2,3,4,5]

#  in
if x_mr in numbers_mr:
  print(x_mr in numbers_mr)

# not in
if x_mr not in numbers_mr:
  print(x_mr not in numbers_mr)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_mr is y_mr:
  print(x_mr is y_mr)

# is not
if x_mr is not y_mr:
  print(x_mr is not y_mr)