# Use  a varible to represent a person's name and include some whitespace characters at the beginning and end of the name.
name = " John Smith "
# Make sure to use each character combination, "\t" and "\n" at least once
print("\tJohn Smith")
print("\nJohn Smith")
print("\n\tJohn Smith")
# Print the name once, so the whitespace around the name is displayed 
print(name)
# Then print the name using each of the three stripping functions lstrip(), rstrip(), and strip()
print(name.lstrip())
print(name.rstrip())
print(name.strip())