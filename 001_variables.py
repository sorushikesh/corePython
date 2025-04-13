# Variables:
# 	Variables in Python are references to object in memory. This means that they do not store the actual data directly, but the reference to that object.
# 	When we assign a value to a variable, we are actually binding that name of the variable to an object in memory.

#String
first_name = "Rushikesh"
print(first_name)
print(f"Hello {first_name}")

#Integer
age = 26
print(f"Hi I'm {first_name} and I'm {age} old")

#Float
price = 10.99
print(f"The price is ${price}")

#Boolean
is_passed = True
print(f"Passed {is_passed}")


#Typecasting
#   Type Casting is the process of converting the value of one data type into another.
#   In some cases, Python automatically converts types.
#	However, there are few built-in functions like int(), float(), str() and more, in order to ease type casting.

print(f"Variable {first_name} is of type {type(first_name)}")

#Convert float to int
val1 = 11.2
print(f"Variable {val1} is of type {type(val1)}")
val1 = int(val1)
print(f"Variable {val1} is of type {type(val1)} after conversion to int")
val1 = float(val1)
print(f"Variable {val1} is of type {type(val1)} after conversion to float")
val1 = str(val1)
print(f"Variable {val1} is of type {type(val1)} after conversion to String")


