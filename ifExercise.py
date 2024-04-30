""" Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

- Write an if statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.

- Write one version of this program that passes the if test and another that fails. (Failed version should have no output)"""

alien_color  = 'green'

if alien_color == 'green':
    print("Player just earned 5 points.")


alien_color = 'red'

if alien_color == 'green':
    print("Player just earned 5 points.")


""" Choose a color for an alien as you just did and write an if-else chain.

- If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.

- If the alien's color isn't green, print a statement that the player just earned 10 points

- Write one version of this program that runs the if block and another that runs the else block. """


alien_color = 'green'

if alien_color == 'green':
    print("Player just earned 5 points.")
else:
    print("Player just earned 10 points.")


alien_color = 'yellow'

if alien_color == 'green':
    print("Player just earned 5 points.")
else:
    print("Player just earned 10 points.")


""" Turn if-else chain to if-elif-else chain. 

- If the alien is green, print a message that the player earned 5 points

- If the alien is yellow, print a message that the player has earned 10 points

- If the alien is red, print a message that the player has earned 15 points

- Write three versions of this program, making sure each message is printed for the appropriate color alien."""


alien_color = 'green'

if alien_color == 'green':
    print("Player has earned 5 points.")
elif alien_color == 'yellow':
    print("Player has earned 10 points.")
elif alien_color == 'red':
    print("Player has earned 15 points.")


alien_color = 'yellow'

if alien_color == 'green':
    print("Player has earned 5 points.")
elif alien_color == 'yellow':
    print("Player has earned 10 points.")
elif alien_color == 'red':
    print("Player has earned 15 points.")


alien_color = 'red'

if alien_color == 'green':
    print("Player has earned 5 points.")
elif alien_color == 'yellow':
    print("Player has earned 10 points.")
elif alien_color == 'red':
    print("Player has earned 15 points.")




""" Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age and then:

- If the person is less than 2 years old, print a message that the person is a baby.

- If the person is at least 2 years old but less than 4, print a message the person is a toddler.

- If the person is at least 4 years old but less than 13, print a message this person is a kid.

- If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

- If the person is at least 20 years old but less than 65, print a message that this person is an adult.

- If the person is at least 65 years or older, print a message that this person is an elder."""


age = 25

if age < 2:
    print("This person is a baby")
elif age >= 2 and age < 4:
    print("This person is a toddler")
elif age >= 4 and age < 13:
    print("This person is a kid")
elif age >= 13 and age < 20:
    print("This person is a teenager")
elif age >= 20 and age < 65:
    print("This person is an adult")
elif age >= 65:
    print("This person is an elder")
 

