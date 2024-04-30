""" Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting
to each user after they log in to a website. Loop through the list, and print a greeting to each user.

If user name is 'admin' print a special greeting, such as Hello admin, would you like to see a status report?

Otherwise print a generic greeting, such as Hello Jaden, thank you for logging in again."""

usernames = ['justin', 'courtney', 'jake', 'sophia', 'admin', 'emma']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again!")


""" Add an if test to make sure the list of users is not empty. If the list is empty, print the message We need to
find some users.

Remove all the usernames from your list, and make sure the correct message is printed."""

usernames = []

if usernames:
    print(f"Hey {username}, welcome back")
else:
    print(f"We need to find some users.")


""" Make a list of five or more usernames called current_users.

Make another list of five usernames called new_users. Make sure one or two of the new usernames are are also in the 
current_users list.

Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person
will need to enter a new username.. If a username has not been used, print a message saying that username is available.

Make sure the comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this
you'll need to make a copy of current_users containing the lowercase versions of all existing users.)"""


current_users = ['Eric', 'John', 'Jim', 'Casey', 'Thelma']

new_users = ['Thelma', 'Brian', 'Clyde', 'Eli', 'Jim']

# Convert current_users to lowercase
current_users_lower = [user.lower() for user in current_users]

for username in new_users:
    if username.lower() in current_users_lower:
        print(f"{username} already exists! Please choose another username.")
    else:
        print(f"{username} is available.")



""" Ordinal numbers indicate their position ina list, such as 1st or 2nd. Most ordinal numbers end in th,
except 1, 2, and 3.

Store the numbers 1 through 9 in a list.

Loop through the list.

Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output
should read 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, and results should be on separate lines."""

 
num_lis = list(range(1, 10))

for num in num_lis:
    if num == 1:
        ordinal = "1st"
    elif num == 2:
        ordinal = "2nd"
    elif num == 3:
        ordinal = "3rd"
    else:
        ordinal = str(num) + "th"
    print(ordinal)