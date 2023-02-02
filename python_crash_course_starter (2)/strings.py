# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_mr = 'Brad'
age_mr = 37

# Concatenate
print('Hello, my name is ' + name_mr + ' and I am ' + str(age_mr))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name_mr, age=age_mr))

# F-Strings (3.6+)
print(f'Hello, my name is {name_mr} and I am {age_mr}')

# String Methods

s_mr = 'helloworld'

# Capitalize string
print(s_mr.capitalize())

# Make all uppercase
print(s_mr.upper())

# Make all lower
print(s_mr.lower())

# Swap case
print(s_mr.swapcase())

# Get length
print(len(s_mr))

# Replace
print(s_mr.replace('world', 'everyone'))

# Count
sub_mr = 'h'
print(s_mr.count(sub_mr))

# Starts with
print(s_mr.startswith('hello'))

# Ends with
print(s_mr.endswith('d'))

# Split into a list
print(s_mr.split())

# Find position
print(s_mr.find('r'))

# Is all alphanumeric
print(s_mr.isalnum())

# Is all alphabetic
print(s_mr.isalpha())

# Is all numeric
print(s_mr.isnumeric())
