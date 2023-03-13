import random

def read_quotes():
    with open('quotes.txt', 'r') as file:
        quotes = [line.strip() for line in file]
    return quotes

# Read quotes from file
quotes = read_quotes()

# Select a random quote
quote = random.choice(quotes)

# Display the quote to the user
print(quote)

# Allow user to add a new quote to the file
add_quote = input('Do you want to add a new quote? (y/n) ')
if add_quote.lower() == 'y':
    new_quote = input('Enter the new quote: ')
    with open('quotes.txt', 'a') as file:
        file.write(new_quote + '\n')
    # Read quotes from file again to update the list
    quotes = read_quotes()
