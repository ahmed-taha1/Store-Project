from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox 
import tkinter as tk
from tkinter.ttk import Notebook, Style

file = open("accs.txt", "r+")
lines = file.readlines()
#-----------functions ------------
#--- w1 ---

def next1():
    try:
        file = open("credit.txt","r+")
        lines=file.readlines()
        size=len(lines)


        if(w1.i==size and w1.k==3):
            w1.i=-1
            w1.k=1
            file.truncate(0)
            messagebox.showinfo('done','please refill the text')
            os.startfile("credit.txt")

        if (size!=0 and w1.i==size):
            w1.k+=1
            w1.i=0

        v1.set(lines[w1.i])
        command = 'echo ' + lines[w1.i].strip() + '| clip'
        os.system(command)
        Repeat['text'] ="Repeat: "+ str(w1.k)
        w1.i+=1
        Line1['text'] ="Line: "+ str(w1.i)
    except IndexError:
        messagebox.showinfo('done', 'please refill the text')
        os.startfile("credit.txt")

def clear():
    file = open("credit.txt","r+")
    file.truncate(0)
    w1.i=0
    w1.k=1
    file.close
    Line1["text"]="Line: "+ str(w1.i)
    Repeat["text"]="Repeat: "+ str(w1.k)

def copy1():
    file = open("credit.txt","r+")
    lines=file.readlines()
    command = 'echo ' + lines[w1.i-1].strip() + '| clip'
    os.system(command)

def back1():
    file = open("credit.txt", "r+")
    lines = file.readlines()
    size = len(lines)
    if (size != 0 and w1.i == 1):
        w1.k -= 1
        w1.i = size+1
    w1.i -= 2

    v1.set(lines[w1.i])
    command = 'echo ' + lines[w1.i].strip() + '| clip'
    os.system(command)
    Repeat['text'] = "Repeat: " + str(w1.k)
    w1.i += 1
    Line1['text'] = "Line: " + str(w1.i)

def open1():
    os.startfile("credit.txt")
#--- w2 ---

def copy2():
    file = open("accs.txt","r+")
    lines=file.readlines()
    command = 'echo ' + lines[w2.ii-1].strip() + '| clip'
    os.system(command)

def done2():
    top.size-=1
    w2.ii-=1
    remaining['text']="remaining: "+str(top.size)
    Line2['text'] ="Line: "+ str(w2.ii)
    w2.done['text'] = "Done"
    file = open("accs.txt", "r+")
    lines = file.readlines()
    with open('accs.txt', 'a') as the_file:
        the_file.write(lines[0])
    file.seek(0)
    file.truncate()
    file.writelines(lines[1:])

def next2():

    file = open("accs.txt","r+")
    lines=file.readlines()
    size=len(lines)

    if(w2.ii==size):
        w2.ii=0
        file.truncate(0)
        messagebox.showinfo('done','please refill the accounts')
    else:
        command = 'echo ' + lines[w2.ii].strip() + '| clip'
        os.system(command)
        v2.set(lines[w2.ii])
        w2.ii+=1
        Line2['text'] = "Line: " + str(w2.ii)

def back2():
    w2.ii-=2
    file = open("accs.txt","r+")
    lines=file.readlines()

    command = 'echo ' + lines[w2.ii].strip() + '| clip'
    os.system(command)
    v2.set(lines[w2.ii])
    w2.ii+=1
    Line2['text'] ="Line: "+ str(w2.ii)

def count2():
    with open(r"accs.txt", 'r') as fp:
        for count, line in enumerate(fp):
            pass
    remaining['text']="remaining: "+str(count + 1)
    
def open2():
    os.startfile("accs.txt")

    
#--- w3 ---

def copy3():
    file = open("GamersGangStore.txt","r+")
    lines=file.readlines()
    command = 'echo ' + lines[w3.ii-1].strip() + '| clip'
    os.system(command)

def done3():
    top.size+=1
    w3.ii-=1
    Line3['text'] ="Line: "+ str(w3.ii)
    w3.done['text'] = "Done"
    file = open("GamersGangStore.txt", "r+")
    lines = file.readlines()
    with open('accs.txt', 'a') as the_file:
        the_file.write(lines[0])
    file.seek(0)
    file.truncate()
    file.writelines(lines[1:])
    remaining['text']="remaining: "+str(top.size)

def next3():

    w3.done['text'] =""
    file = open("GamersGangStore.txt","r+")
    lines=file.readlines()
    size=len(lines)
    if(w3.ii==size):
        w3.ii=0
        file.truncate(0)
        messagebox.showinfo('done','please refill the text')
        os.startfile("credit.txt")
    else:

        command = 'echo ' + lines[w3.ii].strip() + '| clip'
        os.system(command)
        v.set(lines[w3.ii])
        w3.ii += 1
    Line3['text'] = "Line: " + str(w3.ii)

def back3():
    w3.done['text'] =""
    file = open("GamersGangStore.txt","r+")
    lines=file.readlines()
    size=len(lines)

    if(w3.ii==size):
        w3.ii=0
        file.truncate(0)
        messagebox.showinfo('done','please refill the text')
        os.startfile("credit.txt")
    else:
        w3.ii -= 2
        command = 'echo ' + lines[w3.ii].strip() + '| clip'
        os.system(command)
        v.set(lines[w3.ii])
    w3.ii+=1
    Line3['text'] = "Line: " + str(w3.ii)
    
def open3():
    os.startfile("GamersGangStore.txt")


def pw():
    command = 'echo ' + "yosefxahme1".strip() + '| clip'
    os.system(command)
    
def pw2():
    command = 'echo ' + "yosefxahme1".strip() + '| clip'
    os.system(command)
    
def pw3():
    command = 'echo ' + "yosefxahme1".strip() + '| clip'
    os.system(command)

#--- main window ---
top = Tk()
top.geometry('230x300')
top.title("credit card generator")

nb = ttk.Notebook(top)
nb.pack(fill=X)

w1 = Frame(nb, width='500',height='500')
nb.add(w1,text='Credit')

w2 = Frame(nb, width='500',height='500')
nb.add(w2,text='Emails')

w3 = Frame(nb, width='500',height='500')
nb.add(w3,text='Create account')



#--- style ---
Mysky = "#DCF0F2"
Myyellow = "#F2C84B"

style = Style()
style.theme_create( "dummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": Mysky },
            "map":       {"background": [("selected", Myyellow)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )
style.theme_use("dummy")

top.iconbitmap('visa.ico')

#--- varaibles ---

w1.i = 0
w1.k = 1

w2.ii=0
v1 = tk.StringVar()
v = tk.StringVar()
w3.ii = 0
top.size = len(lines)
v2 = tk.StringVar()

#------------------- labels ---------------------

#--- w1 ---

Line1 = Label(w1,text="Line: 0",font=('Arail',20))
Line1.place(x=10,y=10)


Repeat = Label(w1,text="Repeat: 1",font=('Arail',20))
Repeat.place(x=10,y=45)

#--- w2 ---
Line2 = Label(w2,text="Line: 0",font=('Arail',20))
Line2.place(x=10,y=10)

w2.done = Label(w2,text="",font=('Arail',20))
w2.done.place(x=80,y=200)

remaining = Label(w2,text="remaining: "+str(top.size),font=('Arail',20))
remaining.place(x=10,y=45)

#--- w3 ---

Line3 = Label(w3,text="Line: 0",font=('Arail',20))
Line3.place(x=10,y=10)

w3.done = Label(w3,text="",font=('Arail',20))
w3.done.place(x=80,y=185)

#------------------- buttons ----------------

#--- w1 ---

next1 = Button(w1,text="next",font=("Arail",12),height=2,width=5,bg='lightgreen',command=(next1))
next1.place(x=165,y=115)

back1 = Button(w1,text="back",font=("Arail",12),height=2,width=5,bg='brown',command=(back1))
back1.place(x=10,y=115)

pw = Button(w1,text="pw",font=("Arail",12),height=2,width=5,bg='lightblue',command=(pw))
pw.place(x=88,y=115)

copy1= Button(w1,text="Copy",font=("Arail",12),height=2,width=5,bg='white',command=(copy1))
copy1.place(x=165,y=185)

clear = Button(w1,text="Clear",font=("Arail",12),height=2,width=5,bg='red',command=(clear))
clear.place(x=10,y=185)

open1= Button(w1,text="Open",font=("Arail",12),height=1,width=5,bg='gray',command=(open1))
open1.place(x=165,y=15)

#--- w2 ---
next2 = Button(w2,text="next",font=("Arail",12),height=2,width=5,bg='lightgreen',command=(next2))
next2.place(x=165,y=115)

back2 = Button(w2,text="back",font=("Arail",12),height=2,width=5,bg='brown',command=(back2))
back2.place(x=10,y=115)

pw2 = Button(w2,text="pw",font=("Arail",12),height=2,width=5,bg='lightblue',command=(pw2))
pw2.place(x=88,y=115)

done2 = Button(w2,text="Done",font=("Arail",12),height=2,width=5,bg='red',command=(done2))
done2.place(x=10,y=185)

copy2 = Button(w2,text="Copy",font=("Arail",12),height=2,width=5,bg='white',command=(copy2))
copy2.place(x=165,y=185)

open2= Button(w2,text="Open",font=("Arail",12),height=1,width=5,bg='gray',command=(open2))
open2.place(x=165,y=15)

count2 = Button(w2,text="Count",font=("Arail",12),height=2,width=5,bg='green',command=(count2))
count2.place(x=88,y=185)
#--- w3 ---

next3 = Button(w3,text="next",font=("Arail",12),height=2,width=5,bg='lightgreen',command=(next3))
next3.place(x=165,y=115)

back3 = Button(w3,text="back",font=("Arail",12),height=2,width=5,bg='brown',command=(back3))
back3.place(x=10,y=115)

pw3 = Button(w3,text="pw",font=("Arail",12),height=2,width=5,bg='lightblue',command=(pw3))
pw3.place(x=88,y=115)

done3 = Button(w3,text="Done",font=("Arail",12),height=2,width=5,bg='red',command=(done3))
done3.place(x=10,y=185)


copy3 = Button(w3,text="Copy",font=("Arail",12),height=2,width=5,bg='white',command=(copy3))
copy3.place(x=165,y=185)

open3= Button(w3,text="Open",font=("Arail",12),height=1,width=5,bg='gray',command=(open3))
open3.place(x=165,y=15)
#--------- entery field ---------

# --- w1 ---
c1 = ttk.Entry(w1, textvariable=v1,font=15)
c1.place(x=2,y=245)

# --- w2 ---
c2 = ttk.Entry(w2, textvariable=v2,font=15)
c2.place(x=2,y=245)

# --- w3 ---
c3 = ttk.Entry(w3, textvariable=v,font=15)
c3.place(x=2,y=245)

top.mainloop()