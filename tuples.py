""" ** Tuples **

- Tuples are a list that cannot change which makes them immutable.

- Tuples use parentheses (,) instead of square brackets; and is defined by the presence of a comma; 
If you want to define a tuple with one element, you need to include a trailing comma 

- Tuples also use indexes to access individual elements
"""

# Example
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])



""" ** Looping through all values in a tuple ** 

- You can loop over all the values in a tuple using a for loop"""

dimensions = (200, 50)
# Create a for loop
for dimension in dimensions:
    print(dimension)




    """ ** Writing over a tuple ** 
    
    - You can't modify a tuple, you can assign a new value to a variable that represents a tuple."""

    # Example
    dimensions = (200, 50)
    print(" Original Dimensions:")
    # Create a for loop
    for dimension in dimensions:
        print(dimension)


    dimensions = (400, 100)
    print("\nModified Dimensions:")
    for dimension in dimensions:
        print(dimension)