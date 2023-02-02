# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x_mr = 1           # int
# y_mr = 2.5         # float
# name_mr = 'John'   # str
# is_cool_mr = True  # bool

# Multiple assignment
x_mr, y_mr, name_mr, is_cool_mr = (1, 2.5, 'John', True)

# Basic math
a_mr = x_mr + y_mr

# Casting
x_mr = str(x_mr)
y_mr = int(y_mr)
z_mr = float(y_mr)

print(type(z_mr), z_mr)