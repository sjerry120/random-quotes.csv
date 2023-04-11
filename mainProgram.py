import csv
import random

# Open the CSV file and read the quotes into a list
with open('random-quotes.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    quotes = [row for row in reader]

# Select a random quote from the list
quote = random.choice(quotes)

# Print the quote and its author
print(f'"{quote["quote"]}" - {quote["author"]}')