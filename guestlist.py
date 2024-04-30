""" Make a list that includes three or more people you'd like to invite for dinner. Then use your list 
to print a message to each person, inviting them to dinner """ 

# Create a list
dinner_list = ['Jackson', 'Jetson', 'Joe']

# Create a message inviting them to dinner
message = 'you are invited to dinner at 7pm.'

# Print message to each person inviting them to dinner
print(f"{dinner_list[0]}, {message}")
print(f"{dinner_list[1]}, {message}")
print(f"{dinner_list[2]}, {message}")



# Exercise 3.5
""" You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.
You'll have to think of someone else to invite."""


# Add a print() call at the end of exercise above stating the name of the guest who can't make it
print(f"{dinner_list[1]} will not be able to make it to dinner!")

# Modify your list, replacing the name of the guest who can't make it with the name of the new person you're inviting
dinner_list[1] = 'Jennings'
print(dinner_list)



# Exercise 3.6
""" You just found a bigger dinner table, so now more space is available. Think of more guests to invite to dinner."""

# Add a print() call at the end of exercise above stating to your guests that you found a bigger table
print(f"{dinner_list}, I found a bigger dinner table")

# Use insert() to add one new guest to the beginning of your list
dinner_list.insert(0, 'Jade')
print(dinner_list)

# Use insert() to add one new guest to the middle of the list
dinner_list.insert(2, 'Jonathan')
print(dinner_list)


# Use append() to add one new guest to the end of the list
dinner_list.append('June')
print(dinner_list)

# Print a new set of invitation messages, one for each person in the list
message1 = 'dinner at Flames begins at 7pm. Please be on time!'

print(f"{dinner_list[0]}, {message1}")
print(f"{dinner_list[1]}, {message1}")
print(f"{dinner_list[2]}, {message1}")
print(f"{dinner_list[3]}, {message1}")
print(f"{dinner_list[4]}, {message1}")
print(f"{dinner_list[5]}, {message1}")


# You just foound out that the dinner table at the restaurant is no longer available, and now they only have a table for two

# Add a print() call at the end of exercise above stating that now you can only invite two people
print(f"{dinner_list},I can only invite two people for dinner")

# Use pop() to remove guests from your list one at a time, until only two names remain
dinner_list.pop()
# Each time you pop a name off the list, print a message to that person letting them know you're sorry you can't invite them to dinner
fir_cancellation = dinner_list.pop()
print(f"{fir_cancellation}, I'm sorry I had to cancel dinner with you tonight.")

sec_cancellation = dinner_list.pop()
print(f"{sec_cancellation}, I'm sorry I had to cancel dinner with you tonight.")

third_cancellation = dinner_list.pop()
print(f"{third_cancellation}, I'm sorry I had to cancel dinner with you tonight.")

print(dinner_list)

# Print a message to each of the two people still in the list, letting them know they're still invited
message = "Congratulations! you're still invited to dinner"

print(f"{dinner_list[0]}, {message}")
print(f"{dinner_list[1]}, {message}")


# Use 'del' to remove the last two names from the list, so you have an empty list.
del dinner_list[1]
print(dinner_list)

del dinner_list[0]
print(dinner_list)
# Print your list to make sure the list is empty
print(dinner_list)