# Guessing-Game-Python

Task:  To complete this assignment, you should write a Python program that allows users to guess words from a book title of your choosing. 

Output a welcome message describing the application for the user and any/all instructions
Output the author, year, and genre of the book title they are trying to guess (output from variables)
Output the number of words in the title programmatically (choose a title with more than one word) 

HINT: Research the split() (Links to an external site.) function and len() (Links to an external site.) function and utilize them to find the number of words in your title programmatically

Ask the user to guess a word in the title using input()
Store their guess in a variable and name the variable appropriately
Use the in operation first, then test the result with an if:else statement to see if the word they guessed is in the title string of the book

HINT: In order to test the input against the title words appropriately, consider the case of the word. If the user gave you a capitalized word and the title word is not capitalized (or vice versa), how can you ensure that the if:else test matches it? You need to utilize a command to either lower-case strings or upper-case strings BEFORE testing in the if:else.

Output the results from the user's guess and the complete title. Tell them they are correct or incorrect, then output the complete title, author, year and genre.
