""" Use a for loop to print the numbers from 1 to 20, inclusive."""

for num in range(1, 21):
    print(num)



""" Make a list of the numbers from one to a million, and then use a for loop to print the numbers."""

for value in range(1, 31):
    print(value)


num_lis = []

for value in range(1, 31):
    num_lis.append(value)
    print(value)



""" Make a list of numbers and find the min, max, and sum of the list."""

digits = [2, 4, 6, 8, 10, 14, 16, 18, 20]

min(digits)
print(min(digits))


max(digits)
print(max(digits))


sum(digits)
print(sum(digits))



""" Use a third argument of the range() function to make a list of the odd numbers from 1 to 20.
Use a for loop to print each number."""

for value in range(1, 20, 3):
    print(value)



""" Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list"""

# Create an empty list
multiples_of_three = []
# Create a for loop
for value in range(1, 11):
    multiples_of_three.append(value * 3)
print(multiples_of_three)



""" A number raised to the third power is called a cube (** 3). Make a list of the first 10
cubes, and use a for loop to print out the value of each cube"""

cube_num = []
# Create a for loop
for value in range(1, 11):
    cube_num.append(value ** 3)
# Print the list
print(cube_num)


""" Use a list comprehension to generate a list of the first 10 cubes"""
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)


