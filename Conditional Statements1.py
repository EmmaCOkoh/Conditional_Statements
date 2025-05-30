# Conditional Statements

# if else principle
# if a condition is met
# else an alternative
# if it's raining (condition), take an umbrella
# otheriwse, wear shorts

if 5 > 3:
    print("Hello") # prints hello

if 3 < 2:
    print("Hello") # prints nothing because condition is not met

if 3 < 2:
    print("Hello")
else:
    print("Condition was not true") # prints condition was not true

# relation operators
# > < >= <= == !=

age = 16
if age <= 15:
    print("You are younger than 16")
elif age == 16:
    print("You are 16")
elif age == 17:
    print("You are 17")
else:
    print("You are older than 16")

# logical operators
# and
age = 19
if age < 13:
    print("You are a child")
elif age >= 13 and age <= 18:
    print("You are a teenager")
else:
    print("You are an adult")

# or
if 5 > 3 or 2 < 1:
    print("hi")



