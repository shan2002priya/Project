import tkinter
from PIL import Image, ImageTk
import random
root = tkinter.Tk()
root.geometry('400x400')
root.title('Dice Program')
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()
HeadingLabel = tkinter.Label(root, text="Roll The Dice",
   fg = "black",
     bg = "white",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack()
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
ImageLabel.pack( expand=True)
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage
button = tkinter.Button(root, text='Click on', fg='white',bg='black' ,font = "Helvetica 16 bold ", command=rolling_dice)
button.pack( expand=True)
root.mainloop()
