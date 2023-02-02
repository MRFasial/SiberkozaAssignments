# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name_mr='Sam'):
    print(f'Hello {name_mr}')


# Return values
def getSum(num1_mr, num2_mr):
    total_mr = num1_mr + num2_mr
    return total_mr


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1_mr, num2_mr: num1_mr + num2_mr

print(getSum(10, 3))
