#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HANGMAN PROJECT - M. KLAI
# © STEPHANE DUCHEMIN & YANIS MAHRANE - EFREI L1 INTERNATIONAL 2022


from Tkinter import *



def importe(): 	#function who import the main algorithm
	import hangman 
	
menu = Tk() #define the tkinter window
menu.title ("Hangman Menu: DUCHEMIN ; MAHRANE ; EFREI L1 INTER") #rename the tkinter window

hangpic = PhotoImage(file="hangman.png") #Import of the picture

canvas = Canvas(menu,width=500, height=300) 		#create the canvas and display it
canvas.create_image(0, 0, anchor=NW, image=hangpic)
canvas.pack()

hm_button = Button(menu, text="Start", command = importe) #create the buttons start and exit
hm_button.pack()
exit_button = Button(menu, text= "Exit", command = menu.destroy)
exit_button.pack(side = BOTTOM)

menu.mainloop() #the main boucle of the menu window (tkinter)

