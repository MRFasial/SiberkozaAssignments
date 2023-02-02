# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON_mr = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user_mr = json.loads(userJSON_mr)

# print(user)
# print(user['first_name'])

car_mr = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON_mr = json.dumps(car_mr)

print(carJSON_mr)