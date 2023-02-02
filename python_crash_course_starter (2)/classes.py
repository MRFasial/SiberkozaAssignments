# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:

  # Constructor : is basically a function that runs when you instantiate an object from a class.
  def __init__(self_mr, name_mr, email_mr, age_mr):
    self_mr.name_mr = name_mr
    self_mr.email_mr = email_mr
    self_mr.age_mr = age_mr
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
    self_mr._private_mr = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self_mr):
      return f'My name is {self_mr.name_mr} and I am {self_mr.age_mr}'

  def has_birthday(self_mr):
      self_mr.age_mr += 1
 
 #function for encap variable
  def print_encap(self_mr):
      print(self_mr._private_mr)

# Extend class
class Customer(User):
  # Constructor
  def __init__(self_mr, name_mr, email_mr, age_mr):
      User.__init__(self_mr, name_mr, email_mr, age_mr) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self_mr.name_mr = name_mr
      self_mr.email_mr = email_mr
      self_mr.age_mr = age_mr
      self_mr.balance_mr = 0

  def set_balance(self_mr, balance_mr):
      self_mr.balance_mr = balance_mr

  def greeting(self_mr):
      return f'My name is {self_mr.name_mr} and I am {self_mr.age_mr} and my balance is {self_mr.balance_mr}'

#  Init user object
brad_mr = User('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet_mr = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet_mr.set_balance(500)
print(janet_mr.greeting())

brad_mr.has_birthday()
print(brad_mr.greeting())

#Encapsulation -->
brad_mr.print_encap()
brad_mr._private = 800 #Changing for brad
brad_mr.print_encap()

# Method inherited from parent
janet_mr.print_encap() #Changing the variable for brad doesn't affect janets variable --> Encapsulation
janet_mr._private = 600
janet_mr.print_encap()

#Similary changing janet's doesn't affect brad's variable.
brad_mr.print_encap()
