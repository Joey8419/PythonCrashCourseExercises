""" Think of at least three animals that have similar characteristics. Store the names of these animals in a list.
Then use a for loop and print out the name of each animal."""

animals = ['sharks', 'fish', 'eels']
# Use a for loop and print out the name of each animal
for sea_animals in animals:
    print(sea_animals)


""" Modify your program to print a statement about each animal."""

animals = ['sharks', 'fish', 'eels']
# Create a for loop
for sea_animals in animals:
    print(f"{sea_animals.title()} are not good pets to have. Some of them are dangerous!\n")
print("I am not a fan of any of these animals.")