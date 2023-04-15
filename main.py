# import dependencies
import csv
import random


def random_quote_generator(filepath) -> None:
    # Open the CSV file and read the quotes into a list
    with open(filepath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        quotes = [row for row in reader]

    # Select a random quote from the list
    quote = random.choice(quotes)

    # Print the random quote and its author
    print(f'"{quote["quote"]}" - {quote["author"]}')

random_quote_generator('random-quotes.csv')
# new comment