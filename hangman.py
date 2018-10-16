#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HANGMAN PROJECT - M. KLAI
# © STEPHANE DUCHEMIN & YANIS MAHRANE - EFREI L1 INTERNATIONAL 2022

#=======================================================================================================================================================================================================
#																							IMPORT OF REQUIRED LIBRARIES
#=======================================================================================================================================================================================================

from random import randrange
from Tkinter import *

#=======================================================================================================================================================================================================
#																							CONSTANTS
#=======================================================================================================================================================================================================

letters = "abcdefghijklmnopqrstuvwxyz"
text = "new file.txt"
dictionary = []
with open(text,'r') as f: 
		for line in f:
			for word in line.split(): #for all words in the text file
				dictionary.append(word.lower()) #add each word to a liste



##=======================================================================================================================================================================================================
#																							FUNCTIONS
#=======================================================================================================================================================================================================

def gui(): #graphic function which computes a canvas where the hangman will be display with all buttons and text
	global canvas
	exite=Button(window, text="QUIT", command=quit)
	canvas = Canvas(window, width=800, height=800, background='white')
	title= canvas.create_text(400,50, text="WELCOME IN THE HANGMAN GAME", font="Times 20", fill="red")
	copyrighte= canvas.create_text(145,780, text="A game from Stéphane Duchemin & Yanis Mahrane", font="Times 10", fill="black")
	canvas.pack()
	exite.pack()

	canvas.create_line(250,100,250,600)
	canvas.create_line(250,100,500,100)
	canvas.create_line(250,200,300,100)
	canvas.create_line(500,100,500,200)




def read_letter(tries): #this function analyse the letter that the user enter and compare to the correct word

    while True:
        letter = raw_input("Enter a letter : ")

        if letter in tries:
            print("this letter has already been requested")
        elif letter not in letters or len(letter) != 1:
            print("Only one letter in small caps")
        else:
            break;
    tries.append(letter)
    
    return letter




def clue(word, tries): #this function allows to the player to know how many letters there are in the correct word and displayed the correct letters
    c = ''
    for letter in word:
        if letter in tries:
            c = c + letter
        else:
            c = c + '-'
    return c

def game(): #this function is the heart of the game, with the main while who permit to know when the game is over or not / win or not
	error=0
	gender = " "
	print("WELCOME ON STEPHANE AND YANIS' HANGMAN")
	while gender not in genders_list:	
		gender = raw_input("Hello there, are you a Man or a Woman? Press M for Man and W for Woman: ") 
	while True:
		print("Letters already proposed", tries)
		print("The word is :", clue(word, tries))
		letter = read_letter(tries)
		
		if letter in word:
			if clue(word, tries) == word:
				canvas.create_text(400,700, text=('Congratulation ! You won, the word was',word), font="Times 20", fill="green")
				canvas.create_text(400,750, text=('Number of errors: ',error), font="Times 20", fill="blue")
				return True
		else:
			error = error + 1
			if error == 1 and gender in 'Mm':
				canvas.create_oval(470,200,530,250)
			if error == 1 and gender in 'Ww':
				canvas.create_oval(470,200,530,250)
				
			if error ==2 and gender in 'Mm':
				canvas.create_line(500,250,500,280)
			if error == 2 and gender in 'Ww':
				canvas.create_line(500,250,500,280)
				
			if error ==3 and gender in 'Mm':
				canvas.create_line(500,280,450,320)
			if error == 3 and gender in 'Ww':
				canvas.create_line(500,280,450,320)	
				canvas.create_line(500,280,550,320)
				
			if error ==4 and gender in 'Mm':
				canvas.create_line(500,280,550,320)
			if error == 4 and gender in 'Ww':
				canvas.create_line(500,280,500,400)
				
			if error ==5 and gender in 'Mm':
				canvas.create_line(500,280,500,400)
			if error == 5 and gender in 'Ww':
				canvas.create_line(500,320,450,380)
				canvas.create_line(500,320,550,380)
				canvas.create_line(450,380,550,380)
				
			if error ==6 and gender in 'Mm':
				canvas.create_line(500,400,450,450)
				canvas.create_line(500,400,550,450)
			if error == 6 and gender in 'Ww':
				canvas.create_line(500,400,450,450)
				canvas.create_line(500,400,550,450)
				
			if error >= max_error:
				canvas.create_text(400,700, text=('You loose the person is hanged, the word was',word), font="Times 20", fill="red")
				canvas.create_text(400,750, text=('Number of errors: ',error), font="Times 20", fill="red")
				return False


#=======================================================================================================================================================================================================
#																							MAIN WHILE
#=======================================================================================================================================================================================================

while True: #this function computes the main while who permit to run the window and the game function
	window=Tk()
	window.title('Hangman Project: DUCHEMIN ; MAHRANE ; EFREI L1 INTER')
	gui()
	number_games = number_games + 1
	if game():
		wins = wins + 1
		canvas.create_text(400,725, text=('You played',number_games,'time(s) and you won',wins,'time(s)'), font="Times 20", fill="black")
	else:
		canvas.create_text(400,725, text=('You played',number_games,'time(s) and you won',wins,'time(s)'), font="Times 20", fill="red")
	while True:
		cont = raw_input("c to continue, s to stop : ")
		if cont == 'c' or cont == 's':
			break

	if cont == 's':
		print('You played',number_games,'time(s) and you won',wins,'time(s)')
		break

	if cont == 'c':
		window.destroy()
		text = "new file.txt"
		dictionary = []
		with open(text,'r') as f: 
			for line in f:
				for word in line.split(): #for all words in the text file
					dictionary.append(word.lower()) #add each word to a list
		word = dictionary[randrange(len(dictionary))]
		tries = []
		
		



