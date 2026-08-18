# Just notes for me
# To declare a class you do "class ClassName:"
# if you don't want errors, and you plan on leaving your class empty use "pass"' to continue to the next line of code
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

# this is how to initialize an object from a class "object_name = ClassName()"
# needs to have parenthesis at the end in order to initialize the object to the class
# Use PascalCase for the classes and in python and snake_case for everything else

# made a new user with these staring values, much more convenient: lessens code
user_1 = User("001", "sophia")
user_2 = User("002", "Rachel")
print(f"{user_1.id}, {user_1.username}, {user_2.id}, {user_2.username}, {user_1.followers}")

# Adding an attribute: a variable associated to an object
# in this case we are adding the attribute and to the object
# user_1.id = "001"
# user_1.username = "sophia"
# print(user_1.username)


# Constructor: part of the blueprint that allows us to specify what should happen when our object is being constructed (AKA initializing
# To set (variables, counters, switches, ect.) to their values
# to create a constructor we us "def __init__(self)" to initialize the attributes
