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
-To add new quotes to the file you can run the "add_quotes" python file and follow the prompt in your console to add unique quotes and authors.


	“A random quote” -  some author

