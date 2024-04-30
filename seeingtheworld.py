""" Think of at least five places in the world you'd like to travel to visit. Store the locations in a list. Make sure 
the list is not in alphabetical order.

* Sort() list makes permanent changes to the list
* Sorted() makes temporary changes to the list"""

travel_destinations = ['Saint Lucia', 'Cabo', 'Aruba', 'Bali', 'Fiji', 'Africa']
# Print list in original order
print(travel_destinations)

# Use sorted() to print your list in alphabetical order without modifying the actual list
sorted(travel_destinations)
# Print list in alphabetical order
print(sorted(travel_destinations))

# Show that your list is still in its original order by printing it
print(travel_destinations)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
sorted(travel_destinations).reverse()
# print list
# 'reverse=True parameter is particularly useful when you need to sort data in reverse alphabetical, numerical, or any other order.
print(sorted(travel_destinations, reverse=True))

# Show that your list is still in it's original order by printing it again
print(travel_destinations)

# Use the reverse() method to change the order of your list 
travel_destinations.reverse()
# Print list to show that order has changed
print(travel_destinations)


# Use reverse to change order of your list again back to its original order
travel_destinations.reverse()
# Print the list to show it's back to it's original order
print(travel_destinations)


# Use sort() to change your list so it's stored in alphabetical order
travel_destinations.sort()
# Print the list to show that it's order has changed
print(travel_destinations)


# Use sort() to change the list so its stored in reverse-alphabetical order
travel_destinations.sort(reverse=True)
# Print the list to show that the order has been changed
print(travel_destinations)


# Print the length of your list
print(len(travel_destinations))