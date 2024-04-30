""" A buffet style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

- Use a for loop to print each food the reastaurant offers.

- Try to modify one of the items, and make sure that python rejects the change.

- The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites 
the tuple, and then use a for loop to print each of the items on the revised menu"""


# List of five foods
buffet_foods = ('fried fish', 'rice', 'sweet potatoes', 'chicken', 'mac & cheese')
# Create for loop to print out food
for food in buffet_foods:
    print(food)

# Try to modify one of the items; Make sure python rejects the change
#buffet_foods[3] = 'steak'


# The restaurant changed two things on their menu; Add a line that rewrites the tuple

buffet_foods = ('fried fish', 'rice', 'sweet potatoes', 'chicken', 'mac & cheese')
print("Original Menu:")
# Create for loop to print out food
for food in buffet_foods:
    print(food)


# Create the new tuple with the changed items
buffet_foods = ('fried fish', 'rice & beans', 'sweet potatoes', 'steak', 'mac & cheese')
print("\nModified Menu:")
# Then use a for loop to print each of the items on the revised menu
for food in buffet_foods:
    print(food)