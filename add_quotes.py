import csv 

""" Python program to demonstrate to add more quotes to random-quotes. """

def add_new_quote(filepath, quote, author):
    # Create a dictionary for the new quote
    new_quote = {"quote": quote, "author": author}

    # Append(write) the new quote to the CSV file
    with open(filepath, 'a', newline='') as csvfile:
        fieldnames = ["quote", "author"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_quote)

# Prompt the user to add a new quote
quote = input("Enter a new quote: ")
author = input("Enter the author of the quote: ")
add_new_quote('random-quotes.csv', quote, author)