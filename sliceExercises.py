""" Using one of the programs you wrote, add several lines to the end of the program that does the following:

- Print the message 'The first three items in the list are:.' Then use a slice to print the first three items from the list.

- Print the message 'The items from the middle of the list are:.' Then use a slice to print three items from the middle of the list.

- Print the message 'The last three items in the list are:.' Then use a slice to print the last three items from the list."""


# list
sneaker_brands = ['nike', 'jordans', 'puma', 'adidas', 'converse', 'new balance']
# print the list
print(sneaker_brands)


# Print message
print("The first three items in the list are:")
print(sneaker_brands[0:3])

""" OR """

print("\nThe first three items in the list are:")
print(sneaker_brands[:3])


print("\nThe items in the middle of the list are:")
print(sneaker_brands[1:4])


print("\nThe last three items in the list are:")
print(sneaker_brands[-3:])

""" OR """

print("The last three items in the list are:")
print(sneaker_brands[3:])



""" Make a copy of the list of pizzas, and call it friends pizza. Then do the following:

- Add a new pizza to the original list

- Add a different pizza to the list friends pizza

- Prove that you have two seperate lists. Print the message 'My friend's favorite pizzas are:' and then use a for loop
to print the second list. Make sure each new pizza is stored in the appropriate list. """


my_pizza = ['pepperoni', 'garlic', 'cheese']
# Make a copy of the list and call it 'friends pizza'
friends_pizza = my_pizza[:]
# Print both lists
print(my_pizza)
print(friends_pizza)


# Add a new pizza to the original list
my_pizza.append('margarita')
print(my_pizza)


# Add a different pizza to the list friends pizza
friends_pizza.append('sausage')
print(friends_pizza)

# Print both lists to prove they are different
print(f"My favorite pizzas are {my_pizza}.")

print(f"\nMy friends favorite pizzas are {friends_pizza}.")


# Use a for loop to print the second list.
print("\nMy friends favorite pizzas are: ")
for pizza in friends_pizza:
    print(pizza)


""" OR IF YOU ONLY WANT TO PRINT OUT 3 FROM THE LIST IN A FOR LOOP:"""

print("\nMy friends favorite pizzas are:")
for pizza in friends_pizza[:3]:
    print(pizza)
