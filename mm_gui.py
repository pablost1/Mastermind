from tkinter import *
from PIL import ImageTk, Image
import random as rd

import mm_logic

main_windows = Tk()
main_windows.title('Mastermind')
main_windows.configure(background='skyblue')
# # # Variables
attempt = 1
COLORS = ['red',
          'purple',
          'blue',
          'orange',
          'brown',
          'white',
          'yellow',
          'green',
          'pink']

CIMG = {'red' : 'BRed.png',
          'purple' : 'BPurple.png',
          'blue' : 'BBlue.png',
          'orange' : 'BOrange.png',
          'brown' : 'BBrown.png',
          'white' : 'BWhite.png',
          'yellow' : 'BYellow.png',
          'green' : 'BGreen.png',
          'pink' : 'BPink.png'}

ball_labels = [label1:=0 , label2:=0, label3:=0, label4:=0, label5:=0]
# # # Main Logic
randomcolors = []

while len(randomcolors) <= 5:
    colore = COLORS[rd.randint(0,8)]
    if colore not in randomcolors:
        randomcolors.append(colore)
# # # Functions

# # # Widgets

for x in range(5):
    ball_labels[x] = ImageTk.PhotoImage(Image.open("C:\\Users\\pablo_iectaxb\\projetos\\imgs\\"+CIMG[randomcolors[x]]))
    temp_label = Label(image = ball_labels[x], bg='skyblue')
    temp_label.grid(row=attempt, column=x)


exit_button = Button(main_windows, text='Quit', command=main_windows.quit)
exit_button.grid(row=20, column=5)

main_windows.mainloop()