# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:30:28 2021

@author: Ayush
"""

import tkinter
from PIL import Image,ImageTk
import random

# top-level widget which represents the main window of an application
root = tkinter.Toplevel()
root.geometry('400x400')
root.title('Roll the Dice')

dice = ['dice1.png', 'dice2.png', 'dice3.png', 
    'dice4.png', 'dice5.png', 'dice6.png']
DiceImage = ImageTk.PhotoImage(Image.open("dice/"+random.choice(dice)))

ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
# packing a widget in the parent widget 
ImageLabel.pack( expand=True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open("dice/"+random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage
# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
# pack a widget in the parent widget
button.pack( expand=True)

root.mainloop()