"""Find a quote from a famous person you admire. Print the quote and the name of it's author"""

quoter_name = "Washington Irving"

quote = "Great minds have purposes, others have wishes"

# To make sure quote is surrounded by double quotes when using an f string, you must begin the f string with single quotes
# and then wrap the quote inside curly brackets with double quotes
print(f'{quoter_name} once said, "{quote}"')