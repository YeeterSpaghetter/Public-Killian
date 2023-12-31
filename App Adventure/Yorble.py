#Yorble

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import Self
from tkinter import * 
import tkinter as tk
import random 
#import tkinter.filedialog
import pygame
#from PIL import Image, ImageSequence
import time
#import os, sys
import sys
#import runpy
from importlib import util
from tokenize import *

def YNquestion(questionString): #putting the code necessary for the GUI into a function allows it to be called every time the quesiton is asked
    pygame.mixer.music.load("Sfx/click.mp3")
    pygame.mixer.music.play()
    global answer #allows the vaiable to be used anywhere in the program 
    def yes_command(): #called by the GUI to change the variable when the button is clicked
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        answer.set('yes') #.set allows this to exit the GUI as it is a gloabal variable
        window.destroy() #closes the GUI window so the program does no become stuck
    def no_command(): #similar to the procedure above but sets the variable to 'no'
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        answer.set('no')
        window.destroy()
    
    window = tk.Tk() #creates GUI window 
    window.title('Flee')
    yes_no_label = Label(window, text=questionString) # sets label within GUI specified as 'window', set to the string specified when called so this can be used in multiple ways such as in tic tac toe or setting gender of character
    yes_no_label.grid(row=0, column=1) # Label in GUI
    
    answer=StringVar() # Value not assigned in Tk
    
    YESbutton = Button(window, text="Yes", fg='green', command = lambda :yes_command()) # sets the button with test/colour deatils, as well as what happens when pressed
    YESbutton.grid(row=1, column=0) # sets button location
    NObutton = Button(window, text = 'No', fg = 'red', command= lambda :no_command()) # same as for button above
    NObutton.grid(row=1, column=2)
    
    window.mainloop() # GUI

# fighting code

global health # needs to be used anywhere
global energy
global armor

health = 20 # stats altered thru fight
energy = 10
weapon = 'Awesome Cool Dude Sword' 
necklace = "Mother's Pendant" # used to assign damage done by user during their turn
boots = 'Well Worn Boots' # used to assign chance to dodge for user
armor = 1
inventory = ["Water(+5 energy)", "Meat(+6 health)"] # items that can be used, to be deleted from or appended to

pygame.mixer.init()
        
#section that creates the function that can be called to bring up the fight GUI
def fight(enemy):
    
    #section that decides what enemy is being fought and therefore their health and flavour text
    def endTurn():#finishes the user's turn
        print('end turn called')
        #fightWindow.destroy()#closes the GUI used to fight
        turn.set(False)#ends the turn so the enemy can attack
        
    def enemies(enemy):
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        if enemy == 'yorble':
            global eHealth
        eHealth = 10
        return eHealth
            
    def eAtt(enemy, health):#called when it is the enemy's turn
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        if enemy == 'yorble':#used to calculate possible damage output and flavour text when attacking
            gFlavTxt = random.choice(["It attacks wildly!", "It attacks without skill!", "It aims it's weapon nervously!"])#flavour text chosen randomly
            print(gFlavTxt)#flavour text outputted
            health = health - (3 - armor)#takes away a certain amount of health, with this lessoned by the amount of armour the user has
            print ('You have '+ str(health)+' health left!')
        turn = True
    
    #section that decides how much damage is beign done by a regular attack    
    def attPwr(weapon):#branches to test how much damage should be done each turn
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        if weapon == 'Awesome Cool Dude Sword':
            global damage
            damage = 5
            
    def att(health, enemy, eHealth): #command assigned to GUI button
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        endTurn()
        attPwr(weapon)
        eHealth -= damage#stats reassigned so fight can end and user can win
        print ('It has '+ str(eHealth)+' health left!')#user info
        if eHealth > 0: #only outputs if not defeated
            if enemy == 'yorble': #will output different text depending on enemy
                gFlavTxt = random.choice(["It screams wildly!", "It recoils in fear!", "It fails to defend!"])
                print(gFlavTxt)
        else:
            print('Enemy is already dead')
        turn.set(eHealth)
            
    # section that decides how much damage is done my a magic attack
    def magPwr(necklace): # branches to test how much damage should be done each turn
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        if necklace == "Mother's Pendant":
            global damage
            damage = 10
            
    def mag(health, enemy, eHealth): 
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        endTurn()
        magPwr(necklace) # decides how much damage should be done when the attack is used
        eHealth -= damage # re-assigns value so user can win
        print ('It has '+ str(eHealth)+' health left!') # user info
        if eHealth > 0:    
            if enemy == 'yorble': 
                gFlavTxt = random.choice(["It screams wildly!", "It recoils in fear!", "It fails to defend!"])
                print(gFlavTxt)
        return (eHealth)
                
    # inv system
    def checkHealth(health): # validates stats to make sure the user canot go above maximum health
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        if health > 20:
            health = 20
            return health
    def checkEnergy(energy):    
        if energy > 10:
            energy = 10
            return energy
    def inv(health, energy):
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        def close():
            window.destroy()
        def water(): # called by GUI to use the item when the button is clicked
            itemText.set('5 energy has been restored!') # allows this to exit the GUI as it is a global variable
            window.destroy() # closes the GUI window
            turn.set('False') # ends the turn so fight can continue
        def meat(): 
            itemText.set('6 health has been restored!')
            window.destroy()
            turn.set('False')
        
        window = tk.Tk() # GUI window
        window.title('Inventory') 
        
        itemText=StringVar() # allows variable to be used outside of program 
        turn=StringVar()
        
        invLabel = Label(window, text='Choose an item from your inventory!')
        invLabel.grid(row=1, column=1) # sets a place for the label to be displayed on the GUI
        
        closeButton = Button(window, text='Back', fg = 'red', command = lambda :close())#ends if the user does not want to use an item
        closeButton.grid(row=2, column=1) # sets button location
        for i in range(0,len(inventory)): # each item is checked to see if it is in the inventory   
            if inventory[i] == "Water(+5 energy)":# if it is in the inventory then the branch is chosen
                waterButton = Button(window, text= inventory[i], command = lambda :water()) #the button will be displayed with the command to use the item
                waterButton.grid(row=3, column=0) 
            if inventory[i] == "Meat(+6 health)":
                meatButton = Button(window, text = inventory[i], command = lambda :meat()) 
                meatButton.grid(row=4, column=0)
                
        window.mainloop() # required to create the GUI which is essentially an infinite loop waiting for changes (button press)
        itemChoice = itemText.get()
        turn = turn.get() # fetches the choices and assigns them so they can be used to branch below and end the user's turn
        if itemChoice == '5 energy has been restored!': # gives a different output depending on the item used
            energy += 5 # such as by assigning a stat  
            energy = checkEnergy(energy) # makes sure that the user does not do over their limit of stats eg max 20 health
            inventory.remove("Water(+5 energy)") # removes the item from the inventory list so it does not appear again
            print ('You now have '+ str(energy) +' energy!') # gives user information
        elif itemChoice == '6 health has been restored!':
            health += 6
            health = checkHealth(health)
            inventory.remove("Meat(+6 health)")
            print ('You now have '+ str(health) +' health!')
        turn = turn.get()#fetches the choices and assigns them so they can be used to branch below and end the user's turn
        if turn == False:
            endTurn()
            
    #section that decides if the user can run from a fight
    def dodgeChance(boots):
        if boots == 'Well Worn Boots':
            global dodge
            dodge = random.choice(['y','y','n','n']) # 50/50 chances to flee
            
    def flee(enemy, boots):
        pygame.mixer.music.load("Sfx/click.mp3")
        pygame.mixer.music.play()
        if boots == 'Well Worn Boots':
            print('You Have a 50% Chance to Escape.')
        if enemy != 'gBoss': # only works if the fight can be run from (not boss fights)
            YNquestion('Would you still like to try to flee?') # calls GUI which sets variable and asks for label text as arguement
            choice = answer.get()
            if choice == 'yes': 
                print("You try to run!") # user info
                dodgeChance(boots) # redoes the chance to dodge again
                if dodge == 'y': # if successful
                    print ('You escape successfully!')
                    fightWindow.destroy # ends fight
                else:
                    print ('You cannot get away!')#
                endTurn()
                turn = turn.get()
        else:
            print("You can't run now! This is too important!")
    
    

    eHealth = enemies(enemy)# sets health of enemy
    turn = True # sets loops condition
    while turn == True:
        while int(eHealth) > 0: # continues fighting if enemy is alive
            while turn == True: # allows users to make their decision 
                fightWindow = tk.Tk()
                fightWindow.geometry('330x150')
                fightWindow.title('Yorble')
                #pyexec = sys.executable

                def story():
                    global gogo
                    gogo=0
                    storyWindow = tk.Tk()
                    storyWindow.geometry('770x120')
                    storyWindow.title('Story')
                    display = Label(storyWindow, text="Long ago, in a small village in Russia,")
                    display.grid(row=1, column=1)

                    def _change():
                        if button.counter == 0:
                            display.config(text="You were a young boy who often ran around the woods to caese your bordedom,")
                        elif button.counter == 1:
                            display.config(text="You trip on a tree root sticking out of the ground, and begin to fall into a bush")
                        else:
                            display.config(text="You feel one of the leaves prick your back, with a strange liquid on it, and you pass out as you slowly submerge into the bush")
                        if button.counter != 2:
                            button.counter += 1
                        else:
                            def poopy():
                                pygame.mixer.music.load("Sfx/click.mp3")
                                pygame.mixer.music.play()
                                storyWindow.destroy()
                            button2 = Button(storyWindow, text='Go back to battle', command=poopy)
                            button2.grid(row=3, column=2)

                    button = Button(storyWindow,text="Press me",command=_change)
                    button.counter = 0
                    button.grid(row=2, column=1)
                    storyWindow.mainloop()
                
                def exit():
                    pygame.mixer.music.load("Sfx/click.mp3")
                    pygame.mixer.music.play()
                    fightWindow.destroy()
                                
                def goobly():
                    pygame.mixer.music.load("Sfx/click.mp3")
                    pygame.mixer.music.play()
                    spec = util.spec_from_file_location('Goobly.py', 'Goobly.py')
                    module = util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return module
                
                def yorble():
                    pygame.mixer.music.load("Sfx/click.mp3")
                    pygame.mixer.music.play()
                    spec = util.spec_from_file_location('Yorble.py', 'Yorble.py')
                    module = util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return module
                
                def bloober():
                    pygame.mixer.music.load("Sfx/click.mp3")
                    pygame.mixer.music.play()
                    spec = util.spec_from_file_location('Bloober.py', 'Bloober')
                    module = util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return module
                
                menu = Menu(fightWindow)
                file = Menu(menu, tearoff=OFF)
                Other_Battles = Menu(menu, tearoff=OFF)
                file.add_command(label='Close Program', command=exit)
                Other_Battles.add_command(label='Fight Goobly', command=goobly)
                Other_Battles.add_command(label='Fight Goblin', )
                Other_Battles.add_command(label='Fight Bloober', command=bloober)
                Other_Battles.add_command(label='Fight Yorble', command=yorble)   
                menu.add_cascade(label='File', menu=file)
                menu.add_cascade(label='Other Battles', menu=Other_Battles) 
                fightWindow.config(menu=menu)
            
                turn = StringVar()
                
                frameCnt = 12
                #frames = [PhotoImage(file='Enemies\Bananer\Bananaer.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
                frames = [PhotoImage(file='Enemies/Yorble/Yorble.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

                def update(ind):

                    frame = frames[ind]
                    ind += 1
                    if ind == frameCnt:
                        ind = 0
                    Enemy_sprite.configure(image=frame)
                    fightWindow.after(100, update, ind)

                Enemy_sprite = Label(fightWindow)
                Enemy_sprite.grid(row=0, column=2)
                fightWindow.after(0, update, 0)

                storyButton = Button(fightWindow, text="Learn the Story", command=story)
                storyButton.grid(row=2, column=2)
                
                fightLabel = Label(fightWindow, text='Pick an action for this turn!') 
                fightLabel.grid(row=1, column=2) 
                
                attButton = Button(fightWindow, text= 'Attack', command = lambda :att(health, enemy, eHealth)) # to attack
                attButton.grid(row=1, column=0)
                
                magButton = Button(fightWindow, text= 'Magic', command = lambda :mag(health, enemy, eHealth)) # to use magic
                magButton.grid(row=1, column=1)
                
                invButton = Button(fightWindow, text= 'Inventory', command = lambda :inv(health, energy)) # to use item
                invButton.grid(row=1, column=3)
                
                fleButton = Button(fightWindow, text= 'Flee', command = lambda :flee(enemy, boots)) # to end the fight
                fleButton.grid(row=1, column=4)
                
                fightWindow.mainloop()
            
                eHealth = turn.get()    
                
                eAtt(enemy, health)        
        
    else:
        def victory():
            pygame.mixer.music.load("Sfx/click.mp3")
            pygame.mixer.music.play()
            youwin.destroy()
        youwin = tk.Tk()
        youwin.title('You Won!')
        fightLabel2 = Label(youwin, text='You defeated the enemy!(Go to Other Battles tab to continue on)')
        fightLabel2.grid(row=1, column=2)
        leavebutton = Button(youwin, text='Leave', command=victory)
        leavebutton.grid(row=2, column=2)
        youwin.mainloop()

fight('yorble')