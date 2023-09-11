#Goobly

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import Self
from tkinter import * 
import tkinter as tk
import random 
import os, sys
import runpy
from importlib import util
from tokenize import *
import pygame

def YNquestion(questionString): 
    global answer 
    def yes_command(): 
        pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
        pygame.mixer.music.play()
        answer.set('yes') 
        window.destroy() 
    def no_command():
        pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
        pygame.mixer.music.play() 
        answer.set('no')
        window.destroy()
    
    window = tk.Tk() 
    
    yes_no_label = Label(window, text=questionString) 
    yes_no_label.grid(row=0, column=1) 
    
    answer=StringVar() 
    
    YESbutton = Button(window, text="Yes", fg='green', command = lambda :yes_command()) 
    YESbutton.grid(row=1, column=0) 
    NObutton = Button(window, text = 'No', fg = 'red', command= lambda :no_command()) 
    NObutton.grid(row=1, column=2)
    
    window.mainloop() 
    
global health
global energy
global armor
health = 20 
energy = 10
weapon = 'Rusty Old Sword' 
necklace = "Mother's Pendant" 
boots = 'Well Worn Boots' 
armor = 1
inventory = ["Water(+5 energy)", "Meat(+6 health)"]

pygame.mixer.init()

def fight(enemy):
    
    def endTurn():
        fightWindow.destroy()
        
        
    def enemies(enemy):
        pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
        pygame.mixer.music.play()
        if enemy == 'goobly':
            global eHealth
        eHealth = 10
        return eHealth
            
    def eAtt(enemy, health):
        if enemy == 'goobly':
            gFlavTxt = random.choice(["It attacks wildly!", "It attacks without skill!", "It aims it's weapon nervously!"])
            print(gFlavTxt)
            health = health - (3 - armor)
            print ('You have '+str(health)+' health left!')
        turn = True
    
      
    def attPwr(weapon):
        if weapon == 'Rusty Old Sword':
            global damage
            damage = 5
            
    def att(health, enemy, eHealth):
        pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
        pygame.mixer.music.play() 
        endTurn()
        attPwr(weapon)
        eHealth -= damage
        print ('It has '+str(eHealth)+' health left!')
        if eHealth > 0:
            if enemy == 'goobly': 
                gFlavTxt = random.choice(["It screams wildly!", "It recoils in fear!", "It fails to defend!"])
                print(gFlavTxt)
        turn.set(eHealth)
            
    def magPwr(necklace):
        if necklace == "Mother's Pendant":
            global damage
            damage = 10
            
    def mag(health, enemy, eHealth): 
        pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
        pygame.mixer.music.play()
        endTurn()
        magPwr(necklace)
        eHealth -= damage 
        print ('It has '+str(eHealth)+' health left!') 
        if eHealth > 0:    
            if enemy == 'goobly': 
                gFlavTxt = random.choice(["It screams wildly!", "It recoils in fear!", "It fails to defend!"])
                print(gFlavTxt)
        return (eHealth)
                
    def checkHealth(health):
        if health > 20:
            health = 20
            return health
    def checkEnergy(energy):    
        if energy > 10:
            energy = 10
            return energy
    def inv(health, energy):
        def close():
            window.destroy()
        def water(): 
            itemText.set('5 energy has been restored!')
            window.destroy()
            turn.set('False')
        def meat(): 
            itemText.set('6 health has been restored!')
            window.destroy()
            turn.set('False')
        
        window = tk.Tk()
        
        itemText=StringVar()
        turn=StringVar()
        
        invLabel = Label(window, text='Choose an item from your inventory!')
        invLabel.grid(row=1, column=1)
        
        closeButton = Button(window, text='Back', fg = 'red', command = lambda :close())
        closeButton.grid(row=2, column=1)
        for i in range(0,len(inventory)):
            if inventory[i] == "Water(+5 energy)":
                waterButton = Button(window, text= inventory[i], command = lambda :water()) 
                waterButton.grid(row=3, column=0) 
            if inventory[i] == "Meat(+6 health)":
                meatButton = Button(window, text = inventory[i], command = lambda :meat()) 
                meatButton.grid(row=4, column=0)
                
        window.mainloop() 
        itemChoice = itemText.get()
        turn = turn.get() 
        if itemChoice == '5 energy has been restored!': 
            energy += 5 
            energy = checkEnergy(energy) 
            inventory.remove("Water(+5 energy)")
            print ('You now have '+ str(energy)+' energy!') 
        elif itemChoice == '6 health has been restored!':
            health += 6
            health = checkHealth(health)
            inventory.remove("Meat(+6 health)")
            print ('You now have '+ str(health) +' health!')
        turn = turn.get()
        if turn == False:
            endTurn()
            
    def dodgeChance(boots):
        if boots == 'Well Worn Boots':
            global dodge
            dodge = random.choice(['y','y','y','n','n','n']) 
            
    def flee(enemy, boots):
        pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
        pygame.mixer.music.play()
        if boots == 'Well Worn Boots':
            print('You have a 30% chance to escape.')
        if enemy != 'gBoss': 
            YNquestion('Would you still like to try to flee?') 
            choice = answer.get()
            if choice == 'yes': 
                print("You try to run!") 
                dodgeChance(boots) 
                if dodge == 'y': 
                    print ('You escape successfully!')
                    fightWindow.destroy 
                else:
                    print ('You cannot get away!')
                endTurn()
                turn = turn.get()
        else:
            print("You can't run now! This is too important!")

    eHealth = enemies(enemy)
    turn = True 
    while turn == True:
        while int(eHealth) > 0:
            while turn == True: 
                fightWindow = tk.Tk()
                fightWindow.geometry('330x100')
                fightWindow.title('Goobly')
            
                def exit():
                    fightWindow.destroy()
                    pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
                    pygame.mixer.music.play()
                    
                class python3Execfile(object):
                    def _get_file_encoding(self, filename):
                        with open(filename, 'rb') as fp:
                            try:
                                return tokenize.detect_encoding(fp.readline)[0]
                            except SyntaxError:
                                return "utf-8"
                            
                def my_execfile(filename):
                    globals['__file__'] = filename
                    with open(filename, 'r', encoding=Self._get_file_encoding(filename)) as fp:
                        contents = fp.read()
                        if not contents.endswith("\n"):
                            contents += "\n"
                            exec(contents, globals, globals)
                                
                def bananer():
                    pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
                    pygame.mixer.music.play()    
                    spec = util.spec_from_file_location('Tkinter_rpg_start.py', 'App Adventure\Tkinter_rpg_start.py')
                    module = util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return module
                
                def bloober():
                    pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
                    pygame.mixer.music.play()
                    spec = util.spec_from_file_location('bloober.py', 'App Adventure\Bloober.py')
                    module = util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return module
                
                def yorble():
                    pygame.mixer.music.load("App Adventure\Sfx\click.mp3")
                    pygame.mixer.music.play()
                    spec = util.spec_from_file_location('Yorble.py', 'App Adventure\Yorble.py')
                    module = util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return module
                    
                menu = Menu(fightWindow)
                file = Menu(menu, tearoff=OFF)
                Other_Battles = Menu(menu, tearoff=OFF)
                file.add_command(label='Close Program', command=exit)
                Other_Battles.add_command(label='Fight Bananer', command= bananer)
                Other_Battles.add_command(label='Fight Goblin', )
                Other_Battles.add_command(label='Fight Bloober', command=bloober)
                Other_Battles.add_command(label='Fight Yorble', command=yorble)   
                menu.add_cascade(label='File', menu=file)
                menu.add_cascade(label='Other Battles', menu=Other_Battles) 
                fightWindow.config(menu=menu)
            
                turn = StringVar()
                
                frameCnt = 10
                #frames = [PhotoImage(file='Enemies\Bananer\Bananaer.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
                frames = [PhotoImage(file='App Adventure\Enemies\Goobly\Goobly.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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
        fightLabel.config(fightWindow, text='You defeated the enemy!(Go to Other Battles tab to continue on)')

fight('goobly')