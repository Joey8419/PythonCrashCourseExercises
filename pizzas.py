# Think of at least three kinds of your favorite pizza. Store these pizza names in a list.
fav_pizza = ['pepperoni', 'garlic', 'cheese']
# Then use a for loop to print the name of each pizza
for toppings in fav_pizza:
    print(toppings)


""" Modify your for loop to print a sentence using the name of the pizza, instead of printing the name of each pizza.
For each pizza, you should have one line of output containing a simple statement like 'I like pepperoni pizza'."""

fav_pizza = ['pepperoni', 'garlic', 'cheese']
# Then use a for loop to print the name of each pizza
for toppings in fav_pizza:
    print(f"One of my favorite pizzas is {toppings}!\n")
# Add a line at the end of your program, outside the for loop that states how much you like pizza.
# The output should consist of three or more lines about the kinds of pizza you like
    print(f"I think {toppings} is the best kind of pizza out there!")
# Then add an additional sentence, such as 'I really love pizza.'
print("I really love pizza.")
