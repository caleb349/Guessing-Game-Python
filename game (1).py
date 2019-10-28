#!/usr/bin/en python3
# -*- coding: utf-8 -*-
"""
#title: Exercise 2

@desc: This is a Python program that allows users 
to guess words from a book title of their choosing. 

@created:  sun jan 20 18:15:11 2019
@author:   Caleb obi
@course:   Introduction to programming
@univ:     Wayne state University
@assign:   Exercise 2
@pyVerrsion: 3.7x
"""
import datetime
import random


# Get todays's date fromt the datetime library i imported above
currentDate = datetime.date.today()
currentYear = currentDate.year # # I am using the CurrentDate value and...
# extracting the year; We can access the day, month and year with attributes:
# currentDate.day   currentDate.month   currentDate.year

# Here i will print out a welcome message for my Guessing game  to the user
# What the progam is doing and what to expect 
print("\n"*3) # for new lines
print("*"*72) # asterisks
print("WELCOME:")
print("\n")# new line
    #print the instructions of the game using variables.
print(" This is a Python program that allows users to guess words" 
      "from a book title of your choosing. ")
print("\n") #new line
print("let's begin!")
print("\n"*3) # 3 new lines
print("Welcome to Book Guessing Game!")   
Title = "The revolution of the Clean Eater"
Author = "charles paltron"
year = "may 1999"
print("This title of my book is:", Title, "By", Author, "on", year)
print("\n"*1)

# creating a list
lists = ['The', 'revolution', 'of', 'the', 'Clean', 'Eater']
# Number of tries
tries = +5
#variables
lists = random.randint(0, 6)

#questions
#if lists == 0:
    #print ("thats correct")
#else: 
    #print ("thats incorrect of ", random)    
question = input("woud you like to play a game? [Y/N] ")
if question == "n":
    print("ohh..okay")

if question == "y":
   print("Guess a word; from the book The revolution of the Clean Eater") 
   guess = bool(input("Guess a word:"))
   if guess == lists:
        print("Thats correct...")
    
   if guess != lists:
            print("Thats incorrect,")
   #while guess != lists: 
            #tries += 1
      #guess = bool(input("try again:"))   
print("\n"*1)

print("This title of my book is:", Title, "By", Author, "on", year)

   
      