# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits_mr = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2_mr = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2_mr = ('Apples',)

# Get value
print(fruits_mr[1])

# Can't change value
fruits_mr[0] = 'Pears'

# Delete tuple
del fruits2_mr

# Get length
print(len(fruits_mr))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set_mr = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set_mr)

# Add to set
fruits_set_mr.add('Grape')

# Remove from set
fruits_set_mr.remove('Grape')

# Add duplicate
fruits_set_mr.add('Apples')

# Clear set
fruits_set_mr.clear()

# Delete
del fruits_set_mr

print(fruits_set_mr)
