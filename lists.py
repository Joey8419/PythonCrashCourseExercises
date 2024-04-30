# List is one of the 4 data types; mutable
# A list is a collection of items in a particular order (ordered)
# List can have duplicate values
# The list[] function is used to convert an iterable (such as a string, tuple or dictionary) into a list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# To access an elelment in a list use the index (location of element)
print(bicycles[0])

# You can use string methods on the elements in the list; this will capitalize the first letter 'Trek'
print(bicycles[0].title())

# Store the names of a few of your friends in a list called names
names = ['Larry', 'Moe', 'Joe','Phillip', 'Diane']
# Print each persons name by accessing each element in the list, one at a time
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# Using the code above, print a message to them. The message should be the same, but each message should be personalized to each persons name
message = f"{names[0]}, let's hang out later"
print(message)

message = f"{names[1]}, let's hang out later"
print(message)

message = f"{names[2]}, let's hang out later"
print(message)

message = f"{names[3]}, let's hang out later"
print(message)

message = f"{names[4]}, let's hang out later"
print(message)

# Think of your favorite mode of transportation, and make a list that stores several examples
transportation = ['Honda', 'Chevy', 'Cadillac', 'GMC', 'Ford']
# Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle"
print(f"Very soon I will own a {transportation[3]} Yukon truck.")



""" Modifying elements in a list; Replacing """

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Change an element in that list at index 0
motorcycles[0] = 'ducati'
print(motorcycles)



"""Adding elements to a list"""

# This is the original list
motorcycles = ['honda', 'yamaha', 'suzuki']

# Now add to the list
motorcycles.append('ducati')
print(motorcycles)

# The append method also makes it easier to build lists
# Create an empty list and begin adding elements to the list
motorcycle = []

motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')


"""Inserting elements into a list opens a space at that position, and stores the value at that location"""

# Add a new element at any position in your list by using the insert() method
colors = ['black', 'red', 'green', 'purple', 'blue']
print(colors)

# Add an element at any position in your list by using the insert() method
colors.insert(3, 'orange')
print(colors)


""" Removing elements from a list using the 'del' statement; 'del' comes before the list """
colors = ['black', 'red', 'green', 'purple', 'blue']

# Use the del statement
del colors[3]
print(colors)


""" Removing an item from the list using pop(); pop() removes the last item in the list, but it 
lets you work with that item after removing it"""

motorcycles = ['honda', 'yamaha', 'suzuki']

# pop() an item out of the list
motorcycles_popped = motorcycles.pop()

# Another example of pop()
last_owned = motorcycles.pop()

# Print the popped list
print(motorcycles_popped)
print(f"The last motorcycle I owned was a {last_owned.title()}")



""" Popping items from any position in the list; using an index. Each time you use pop(), the item
you work with/ pop() is no longer stored in the list """

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# pop() item from list using index
first_owned = motorcycles.pop(3)
print(f"My first owned motorcycle was a {first_owned.title()}.")



""" Removing items by value; if you only know the value of the item you want to remove, you can 
use the remove() method """

sneaker_brands = ['Nike', 'Puma', 'New Balance', 'Adidas', 'Jordan']
sneaker_brands.remove('Puma')
print(sneaker_brands)


# You can use the remove() method to work with a value that's being removed from a list
sneaker_brands = ['Nike', 'Puma', 'New Balance', 'Adidas', 'Jordan']
# Assign the value you want to remove to a variable
too_expensive = 'Nike'
# Now remove the value from the list
sneaker_brands.remove(too_expensive)
# Print statement
print(sneaker_brands)


""" Sorting a list permanently with the sort() method; Python sort() method makes it easy to sort a list and changes the order
of the list permanently."""

# Create a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
# Now sort the list
cars.sort()
# Print list
print(cars)


# You can also sort() this list in reverse alphabetical order by passing argument reverse = True to the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
# Now sort the list
cars.sort(reverse=True)
# Print list
print(cars)


""" Sorting a list temporarily with the sorted() function; Displays list in particular order, but doesn't affect the actual order
of the list """

cars = ['bmw', 'audi', 'toyota', 'subaru']
# Now print sorted list
print(sorted(cars))
# print original list
print(cars)


""" Printing lists in reverse order"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
# Print out the list
print(cars)

# Reverse the list
cars.reverse()
# print the list
print(cars)



""" Finding the length of a list; you can find the list by using the len() function """

cars = ['bmw', 'audi', 'toyota', 'subaru']
# get length of list
len(cars)
# Print list
print(len(cars))


""" Slicing a list; Used when you want to work with a specific group of items in a list.
To make a slice, you specify the index of the first and last element you want. Python stops one item before 
the second index you specify."""

# List of players
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Print the  sliced list
print(players[0:3])




""" You can also generate the subset of a list; If you want the second, third, or fourth item in the list,
start the slice at index 1 and end it at index 4."""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Print sliced list
print(players[1:4])



""" Omitting the first index in a slice, Python automatically starts your slice at the beginning of the list:"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])


""" If you want the slice that includes the end of a list (regardless of how long the list is):"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])



""" A negative index returns an element a certain distance from the end of a list;"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])




""" ** Looping through a slice **
You can use a slice in a for loop if you want to loop through subset of the elements in a list."""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the three players on my team: ")
# Create a for loop
# Python loops through the first three players
for player in players[:3]:
    print(player.title())



""" ** Copying a list ** 
To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]).
Python makes a slice that starts with the first item and ends with the last item, producing a copy of the entire list."""


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


print("My favorite foods are:")
print(my_foods)


print("\nMy friends favorite foods are:")
print(friend_foods)


""" Lets add a new food to each list to show that each list keeps track of the appropriate person's favorite food."""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)


print("\nMy friends favorite foods are:")
print(friend_foods)
