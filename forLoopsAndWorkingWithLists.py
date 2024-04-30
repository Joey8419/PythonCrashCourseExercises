# Use a for loop to print out each name from the list
magicians = ['alice', 'david', 'carolina']

# for loop; which reads = 'for every magician in the list magicians, print out the magicians name.'
for magician in magicians:
    print(magician)


""" Equation for a for loop: 
            for variable in list:
                print(variable)
                
When writing for loops you can choose any name you want for a temporary variable, just make sure it's related to the 
each value in that list.


Example:
for cat in cats:
    print(cat)
for dog in dogs:
     print(dog)
for item in list_of_items:
     print(item) """


# Based on the list of magicians, print a message to each of them letting them know they performed a great trick
magicians = ['alice', 'david', 'caroline']

# create the for loop
for magician in magicians:
    print(f"{magician.title()}, your trick was amazing!")


""" Every line that's indented in the for loop is considered to be within the for loop.Each indented line is executed for each 
of the values in the list."""

magicians = ['alice', 'david', 'caroline']
# Create for loopnfor the list
for magician in magicians:
    print(f"{magician.title()}, your trick was amazing!")
    # Create another print statement letting each magician know we're looking forward to the next trick
    # '\n' inserts a blank line after each pass through the loop
    print(f"I can't wait to see your next trick {magician.title()}.\n")



""" Once for loop is completed, you usually want to summarize the block of output. Any lines of code after for loop
that is not indented are executed once without repetition."""

magicians = ['alice', 'david', 'caroline']
# Create for loopnfor the list
for magician in magicians:
    print(f"{magician.title()}, your trick was amazing!")
    # Create another print statement letting each magician know we're looking forward to the next trick
    # '\n' inserts a blank line after each pass through the loop
    print(f"I can't wait to see your next trick {magician.title()}.\n")

# outside of for loop; summarized block of output
print("Thank you, everyone. That was a great magic show!")




