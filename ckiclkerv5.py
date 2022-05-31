import time
import tkinter
from tokenize import Number
from turtle import back, width
window = tkinter.Tk()

window.title('Clicker')
window.geometry('300x300')
window.resizable(0,0)
nummer = 0
lastpress = True
autoklickerswitch = False
def update (event = ''):
    box1.configure(text=nummer)
    if nummer < 0 :
        window.config(background='red')
    if nummer > 0 :
        window.config(background='green')
    if nummer == 0 :
        window.config(background='grey')
    box1.configure(text="%.0f" %nummer)
    window.update()

def delenVerdubbelen(event):
    global nummer
    if lastpress == True:
        nummer *= 3

    elif lastpress == False:
        nummer /= 3
    update()







def yellowbackground (event):
     window.config(background='yellow')

def up(arg=''):
    global nummer, lastpress
    nummer += 1
    lastpress = True
    update()

def down(*args):
    global nummer, lastpress
    nummer -= 1
    lastpress = False
    update()

def autoklicker():
    global nummer, autoklickerswitch
    if autoklickerswitch == True:
        autoklickerswitch = False

    elif autoklickerswitch == False:
        autoklickerswitch = True
        while autoklickerswitch == True:
            time.sleep(0.2)
            if lastpress == True:
                nummer += 1
            elif lastpress == False:
                nummer -= 1
            update()


window.configure(background='grey')


autoklickerbox = tkinter.Checkbutton(window,width=35, height=3,command=autoklicker)
autoklickerbox.pack(
  pady=0
)
buttonUp = tkinter.Button(window,width=35, height=3,command=up,)
buttonUp.pack(
    pady=(30, 0)
)
buttonUp.configure(text='UP')

box1 = tkinter.Label(
    window,
    width=35,height=3,
    text=(nummer),
    bg="white",
    fg="black"
)
box1.pack(
  pady=25
)
box1.bind('<Enter>',yellowbackground)
box1.bind('<Leave>',update)
box1.bind('<Double-Button>',delenVerdubbelen)
window.bind('<plus>',up)
window.bind('<minus>',down)
window.bind('<space>',delenVerdubbelen)
buttonDown = tkinter.Button(window,width=35, height=3,command=down)
buttonDown.pack()
buttonDown.configure(text='down')

window.mainloop()
