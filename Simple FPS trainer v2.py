from distutils.cmd import Command
from re import X
from telnetlib import XASCII
from threading import Timer
import tkinter
import random
from tkinter import Entry, ttk
from tkinter.messagebox import askyesno
window = tkinter.Tk()

keys = ['w', 'a', 's', 'd', 'space', 'Button-1', 'Double-Button-1', 'Triple-Button-1']

window.title('FPS Trainer')
window.geometry('400x400')
window.resizable(0,0)
tijd = 20
points = 0

def start():
    print ('welcome')
    fpstrainer()


def update(arg=''):
    global points, boxes, chosenKey
    if chosenKey in 'wasdspace':
        points += 2
        window.unbind(f'<{chosenKey}>')
    else:
        points += 1
        boxes.unbind(f'<{chosenKey}>')
    boxes.destroy()
    window.update()
    box2.configure(text='Points: '+ str(points))
    klickboxen()

def updatetijd(*args):
    global tijd
    tijd = int(text.get())
    box1.configure(text='Time Remaining: '+ str(tijd))
    




def timer():
    global tijd
    klaar = False
    if tijd > 0 :
     tijd -= 1
    if tijd == 0 :
        klaar = True
        medling()
    box1.configure(text='Time Remaining: ' + str(tijd))
    if not klaar:
        box1.after(1000, timer) 
    
    
def medling():
    global points, tijd, boxes
    boxes.destroy()
    if askyesno('klaar', f'je bent klaar!\nJe punten zijn {points}\nWil je nog een keer spelen?'):
        tijd = 20
        points = 0
        window.update()
        start()
    else:
        exit()


def klickboxen():
    global boxes, chosenKey
    ranx = random.randint(10,80)/100
    rany = random.randint(20,90)/100
    boxes = tkinter.Button()
    boxes.place(relx=ranx,rely=rany,relwidth=0.25,relheight=0.1)
    chosenKey = random.choice(keys)
    formattedKey = chosenKey.replace('-', ' ') 
    formattedKey = formattedKey.replace('Button 1', 'click me')
    if chosenKey in 'wasdspace':
        boxes.configure(text=f'Press {formattedKey}')
        window.bind(f'<{chosenKey}>', update)
    else:
        boxes.configure(text=f'{formattedKey}')
        boxes.bind(f'<{chosenKey}>', update)
    

def fpstrainer():
    timer()
    button.destroy()
    startentry.destroy()
    klickboxen()
   
        
    
    
box1 = tkinter.Label(window,width=100,text='Time Remaining: '+ str(tijd),height=2,bg="black",fg="white" )
box1.pack()

box2 = tkinter.Label(window,width=100,text='Points: '+ str(points),height=2,bg="black",fg="white" )
box2.pack(pady=2)
  


button = tkinter.Button(window,width=35, height=10,command=start)
text = tkinter.StringVar(value=tijd)
text.trace('w',updatetijd)
startentry = ttk.Entry(window, textvariable=text)
startentry.pack()
button.pack()
button.configure(text='start')


window.mainloop()