# Version-Control-Practice-AI-Class
A repository created to practice and improve collaboration &amp; version control among group members as part of the Intro. to Artificial Intelligence Course.


Team members
------------
- Nathan Turkson
- Francis Arkoful
- Daniella Omenogor


Assignment prompt: 
-------------------
Write a program to do the following:
You will work in a team of 3-4 members to create a Python program that generates a random quote
each time it is run. Your program should read in a file containing a list of quotes and their authors,
randomly select one quote, and print it to the console along with its author. You should also include a
README file describing how to use your program and how to add new quotes to the file.

Algorithm for implementation:
------------------------------
------------------------------
- Read in csv file
- Convert to dictionary (keys = authors, values = quotes by authors)
- Import random module for selecting a random quote. We use random.choice to select a single key: value pair from the quotes dictionary.
- Use string formatting to print random quote generated in this format:

	“A random quote” -  some author

