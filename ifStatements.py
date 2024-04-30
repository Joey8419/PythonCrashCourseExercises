""" Python's if statement allows you to examine the current state of a program and respond appropriately to that state"""


# Example 
cars = ['audi', 'bmw', 'subaru', 'toyota']

# Create for loop
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


""" Conditional Tests

- At the heart of every if statement is an expression that can be evaluated as True or False and is called 
a conditional test

- Python uses the values True and False to decide whether the code in an if statement should be executed

- If a conditional test evaluates to true (conditional is met), Python executes the code following the if statement.

- If the test evaluates to False, Python ignores the code following the if statement."""



""" Checking for Equality and Inequality

- Most conditional tests compare the current value of a variable to a specific value of interest

- The equality operator returns True if the values on the left and right side of the operator match, and false 
if they don't match.

- Single equal sign (=) is really a statement [Set the value of ____ to ___].

- Double equal sign (==) asks a question: [Is the value of ___ equal to ___]."""


car = 'bmw'
car == 'bmw'  
# True

car = 'audi'
car == 'bmw'
# False


# Example
A = 1
B = 1.0
C = "1"
 
print(A!=B) # False
print(B!=C) # True
print(A!=C) # True


""" Ignoring Case When Checking for Equality 

- Testing for equality is case sensitive in Python; Two values with different capitalizaions are not considered equal."""

car = 'Audi'
car == 'audi'
# False


""" If case does not matter and instead you just want to test the value of a variable, you can convert the
variable's value to lowercase before doing the comparison:

- This test will return True no matter how the value is formatted because the test is now case insensitive """

car = 'Audi'
car.lower() == 'audi'
# True


""" ** Checking Multiple Conditions ** 

- To check multiple conditions at the same time, use the 'AND' and 'OR' keywords.

- To check whether two conditionss are both True simultaneously, use the keyword 'AND'.

- If each tests passes, the overall expression evaluates to True.

- If either test fails or if both test fails, the expression evaluates to False.

- 'OR' keyword returns true if one of the statements is True; fails only when both individual tests fail """


# Example
X = 15

X > 5 and X > 10 # True; Returns True if both statements are True

X < 5 or X > 10 # True; Returns true if one of the statements is True


""" ** Checking Whether a Value Is in a List or Not in a List **

- use the keyword 'IN' to determine whether a particular value is already in a list.

- Use the keyword 'NOT' to determine whether a particular value is noot in the list."""


# Example
requested_toppings = ['mushrooms', 'onions', 'pineapple']

'mushrooms' in requested_toppings
# True

'pepperoni' in requested_toppings
# False

# Example
fruits = ['apple', 'banana', 'orange'] 

if 'grape' not in fruits: 
    print("Element not found.") 
else: 
    print("Element found!")


""" ** Boolean Expressions **

- Boolean expression is just another name for a conditional test

- Boolean value is either 'True' or 'False'

- Boolean values are often used to keep track of certain conditions """

# Example
age = 15
print(age > 21) # False

print(age < 21) # True


# Example
age = 15
can_drink = age > 20
print(can_drink) # False


""" ** Simple if Statements ** 

- The simplest kind of if statement has one test and one action.

- All indented lines after an if statement will be executed if the test passes, and the entire block of indented lines will be ignored 
if the test does not pass.

- You can have as many lines of code as you want in the block following the if statement."""


# Example
age = 19
if age >= 18:
    print("You are old enough to vote!")


# Example
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")



""" ** if-else Statements ** 

- An if-else statement is similar to a simple if statement, but the else statement allows you to define an action or set of actions 
that are executed when the conditional test fails.

- The if-else statement can be used when you want Python to always execute one of two possible actions."""


# Example
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are to young to vote.")
    print("Please register to vote as soon as you turn 18!.")


""" ** if-elif-else Chain ** 

- Is used to test more than two possible situations

- Python executes only one block in an if-elif-else chain

- It runs each conditional test in order, until one passes

- When a test passes, the code following that test is executed and python skips the rest of the test.

- You can use as many elif blocks as you need to in your code."""


# Example
# Prompt user for age
age = int(input("Enter your age: "))

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


# Example
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is {price}.")


# Example (Using multiple  elif statements)
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is {price}.")


""" ** Omitting the else Block ** 

- Python does not require an else block at the end of an if-elif chain """

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:
    price = 20

print(f"Your admission cost is {price}.")


""" ** Testing Multiple Conditions ** 
 - To check all conditions of interest, use a series of simple if statements with no elif or else blocks
 
 - This method is used when more than one condition could be True, and you want to act on every condition that is True."""


# Example
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")




