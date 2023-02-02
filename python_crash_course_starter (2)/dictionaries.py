# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person_mr = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2_mr = dict(first_name='Sara', last_name='Williams')

# Get value
print(person_mr['first_name'])
print(person_mr.get('last_name'))

# Add key/value
person_mr['phone'] = '555-555-5555'

# Get dict keys
print(person_mr.keys())

# Get dict items
print(person_mr.items())

# Copy dict
person2_mr = person_mr.copy()
person2_mr['city'] = 'Boston'

# Remove item
del(person_mr['age'])
person_mr.pop('phone')

# Clear
person_mr.clear()

# Get length
print(len(person2_mr))

# List of dict
people_mr = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people_mr[1]['name'])
