""" ** Checking for Special Items ** """


# Examples
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for toppings in requested_toppings:
    print(f"Adding {toppings}")

print("\nFinished making your pizza!")


# Examples
# What if they pizzeria is out of green peppers
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for toppings in requested_toppings:
    if toppings == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {toppings}")

print("\nFinished making your pizza!")


""" ** Checking That a List is Not Empty ** 

- Check if the list is empty before running for loops."""

# Example
requested_toppings = []

if requested_toppings:
    for toppings in requested_toppings:
        print(f"Adding {toppings}")
else:
    print("Are you sure you want plain pizza")



""" ** Using Multiple Lists ** """

# Example
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for toppings in requested_toppings:
    if toppings in available_toppings:
        print(f"Adding {toppings}.")
    else:
        print(f"Sorry, we dont have {toppings}.")

print("\nFinished making your pizza!")