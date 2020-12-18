# Import Modules
import tkinter as tk
import random
import pygame

# initialize 
main = tk.Tk()
main.geometry('800x600')
main.resizable(0,0)
main.title('Rock Paper Scissors Game Simulator')
main.config(bg ='aquamarine')

Title = tk.Label(main, text = 'Rock Paper Scissors Game', font='arial 20 bold', bg = 'seashell2').pack()

# User Pick
text = tk.Label(main, text = 'Choose one: rock, paper ,scissors', font='arial 15 bold', bg = 'seashell2').place(x = 230,y=70)

# Start the Game
Result = tk.StringVar()
user_pick = tk.StringVar()

def play(k):
    # User Pick
    user_pick = k
    if user_pick == 'rock':
        plays('rock')
    elif user_pick == 'paper':
        plays('paper')
    else:
        plays('scissors')

    # Computer Pick
    comp_pick = random.randint(1,3)
    if comp_pick == 1:
        comp_pick = 'rock'
    elif comp_pick ==2:
        comp_pick = 'paper'
    else:
        comp_pick = 'scissors'

    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you lose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you lose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you lose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

#reset
def Reset():
    Result.set("") 
    user_pick.set("")

#Exit
def Exit():
    main.destroy()

#Sound Effect
pygame.mixer.init()

def plays(p):
    if p == 'rock':
        x = 'Sound/PUNCH.mp3'
    elif p == 'paper':
        x = 'Sound/slap.mp3'
    else:
        x = 'Sound/swordecho.mp3'

    pygame.mixer.music.load(x)
    pygame.mixer.music.play(loops=1)

# Result
entry = tk.Label(main, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=200, y = 150)

# User Pick
rock = tk.Button(main, font = 'arial 13 bold', text = 'Rock', padx =5, bg ='cyan', command = lambda: play('rock'))
Rock_photo = tk.PhotoImage(file = "Image/Rock.png")
rock.config(image=Rock_photo, width = '200', height = '200')
rock.place(x=70,y=230)

paper = tk.Button(main, font = 'arial 13 bold', text = 'Paper', padx =5, bg ='cyan', command = lambda: play('paper'))
Paper_photo = tk.PhotoImage(file = "Image/Paper.png")
paper.config(image=Paper_photo, width = '200', height = '200')
paper.place(x=300,y=230)

scissors = tk.Button(main, font = 'arial 13 bold', text = 'Scissors', padx =5, bg ='cyan', command = lambda: play('scissors'))
Scissors_photo = tk.PhotoImage(file = "Image/Scissors.png")
scissors.config(image=Scissors_photo, width = '200', height = '200')
scissors.place(x=530,y=230)

# Reset Button
reset = tk.Button(main, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=330,y=500)

# Exit Button
Close = tk.Button(main, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=430,y=500)

# Run Program
main.mainloop()