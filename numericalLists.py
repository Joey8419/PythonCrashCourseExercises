""" Using the range() function in a for loop; range() function makes it easy to generate a series of numbers."""

# Example:
for value in range(1, 5):
    print(value)


""" The range() function causes Python to start counting at the first value you give it, and stop when it reaches 
the second value that you provide.

Because you stop at that second value, the output never contains the end value. To print and include that number,
increase that second value by 1. """

# Example
for value in range(1, 6):
    print(value)




""" If you want to create a list of numbers, convert the results of range() directly into a list using the list() function.
When you wrap list() around a call to the range() function, the output will be a list of numbers."""

# Example
numbers = list(range(1, 11))
print(numbers)




""" The range() function can also tell Python to skip numbers in a given range. If you pass a third argument to
range(), Python uses that value as a step size when generating numbers. (START, STOP, STEP) """

# Example
even_numbers = list(range(2, 13, 2))
print(even_numbers)



""" Make a list of the first 10 numbers squared; Using an empty list and adding elements as needed ensures efficient memory allocation,
particularly with large datasets or when the list size isn't predetermined."""

# Create an empty list
squares = []
# Create for loop and include the numbers wanted in the range
for value in range(1, 11):
    # Now we want each number in range squared; 
    square = value ** 2
    # Each new square value is appended to the list 'squares'
    squares.append(square)

# Print the list
print(squares)



""" Write the above code more concicesly 'squares'; Using an empty list and adding elements as needed ensures efficient memory allocation,
particularly with large datasets or when the list size isn't predetermined."""

# Create an empty list
squares = []
# Create for loop
for value in range(1, 11):
    # Raise each value to the second power and then append it to the list
    squares.append(value ** 2)

# Print the list
print(squares)


""" Finding the min, max, and sum of a list"""

# List
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Find the minimun
min(digits)
# Print minimum number in list
print(min(digits))


# Find the maximum
max(digits)
# Print maximum number in list
print(max(digits))


# Find the sum of the list
sum(digits)
# Print sum of list
print(sum(digits))


""" LIST COMPREHENSION!!
A list comprehension allows you to generate multiple lines of code into one. It combines the for loop and the creation
of new elements into one line, and automatically appends each new element. """

        # Equation for list comprehension
""" ** [expression for value in range]

** [expression for value in list if condition]

- expression: The operation to perform on each value.

- for value in list: Specifies the loop variable (value) and the list over which to iterate.

- if condition (optional): Specifies a condition that filters which values are included in the new list.
"""

# Example
squares = [value ** 2 for value in range(1, 11)]
# Print list
print(squares)
