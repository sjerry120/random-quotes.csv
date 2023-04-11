# Version-Control-Practice-AI-Class
A repository created to practice and improve collaboration &amp; version control among group members as part of the Intro. to Artificial Intelligence Course.


Team members
------------
Nathan Turkson, Francis Arkoful, Daniella Omenogor


Prompt: 
--------
Write a program to read in a file containing a list of quotes and their authors,
randomly select one quote, and print it to the console along with its author. You should also include a
README file describing how to use your program and how to add new quotes to the file.

Algorithm for implementation:
-----------------------------
- Read in csv file
- Convert to dictionary
- Import random module for selecting a random quote. We use random.choice to select a single key: value pair from the quotes dictionary.
- Use string formatting to print random quote generated in this format:

"A random quote" - some author


Usage Instructions
-------------------
- Clone the repository to your local machine.
- Navigate to the repository directory.
- Make sure you have Python installed.
- Run the random_quote_generator.py file using a Python interpreter. This will randomly select a quote from the existing CSV file and print it to the console along with its author.
- If you want to add new quotes to the CSV file, you can run the add_quotes.py file. Follow the prompts in your console to enter unique quotes and authors, and they will be added to the CSV file.

Note: You can also manually edit the CSV file directly to add new quotes, following the format of existing quotes.