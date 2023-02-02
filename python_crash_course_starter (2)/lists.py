# A List is a collection which is ordered and changeable. Allows duplicate members.
# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers_mr = [1, 2, 3, 4, 5]
fruits_mr = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits_mr[1])

# Get the last value
print(fruits_mr[-1])



# Get length
print(len(fruits_mr))

# Append to list
fruits_mr.append('Mangos')

# Remove from list
fruits_mr.remove('Grapes')

# Insert into position
fruits_mr.insert(2, 'Strawberries')

# Change value
fruits_mr[0] = 'Blueberries'

# Remove with pop
fruits_mr.pop(2)

# Reverse list
fruits_mr.reverse()

# Sort list
fruits_mr.sort()

# Reverse sort
fruits_mr.sort(reverse=True)

print(fruits_mr)
