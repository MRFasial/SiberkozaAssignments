# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_mr = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person_mr in people_mr:
  print(f'Current Person: {person_mr}')

# Break
for person_mr in people_mr:
  if person_mr == 'Sara':
    break
  print(f'Current Person: {person_mr}')

# Continue
for person_mr in people_mr:
  if person_mr == 'Sara':
    continue
  print(f'Current Person: {person_mr}')

# range
for i_mr in range(len(people_mr)):
  print(people_mr[i_mr])

for i_mr in range(0, 11):
  print(f'Number: {i_mr}')

# While loops execute a set of statements as long as a condition is true.

count_mr = 0
while count_mr < 10:
  print(f'Count: {count_mr}')
  count_mr += 1