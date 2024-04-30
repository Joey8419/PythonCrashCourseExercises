first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# f strings can be used to compose complete messages associated with a variable
print(f"{full_name.title()}")

# To add a tab to text use \t
print("\tPython")

# To add a newline in a string use \n
print("Languages: \nPython\nC\nJavaScript")

# \n and \t can also be combined
print("Languages: \n\tPython\n\tC\n\tJavaScript")

# To ensure that no whitespace exists at the right side of a string use rstrip() method:
favorite_language = 'python '
print(favorite_language.rstrip())

# To ensure that no whitespace exists at the left side of a string use lstrip() method:
favorite_language = ' python'
print(favorite_language.lstrip())

# To strip whitespaces from both sides use strip()
# To ensure that no whitespace exists at the right side of a string use rstrip() method:
favorite_language = ' python '
print(favorite_language.strip())