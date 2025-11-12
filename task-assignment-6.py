#inclusion of libraries
from tkinter import *
window = Tk()
window.title('Counter')
window.geometry('300x350')

#def function
def add(a,b):
    res=a+b
    return res

def diff(a,b):
    res=a-b
    return res

def multiply(a,b):
    res=a*b
    return res

def div(a,b):
    try:
        res=a/b
    except ZeroDivisionError:
        res='Error'
    return res

#display
display = Entry(window,justify='center',bd=10,font=24)
display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
display.insert(END,0)

#add 
def press(val):
    if display.get() == '0': 
        display.delete(0, END)
    display.insert(END, str(val))

#clear
def clear():
    display.delete(0, END)
    display.insert(END,0)

#solving
def equal():
    expr = display.get()
    if '+' in expr:
        a, b = expr.split('+')
        result = add(float(a), float(b))
    elif '-' in expr:
        a, b = expr.split('-')
        result = diff(float(a), float(b))
    elif '*' in expr:
        a, b = expr.split('*')
        result = multiply(float(a), float(b))
    elif '/' in expr:
        a, b = expr.split('/')
        result = div(float(a), float(b))
    else:
        result = 'Error'
    #display the result
    display.delete(0, END)
    display.insert(END, result)

#button creation
btn = [('1',1,0),('2',1,1),('3',1,2),('+',1,3),('4',2,0),('5',2,1),('6',2,2),('-',2,3),('7',3,0),('8',3,1),('9',3,2),('*',3,3),('0',4,0),('=',4,1),('C',4,2),('/',4,3)]
for (txt,r,c) in btn:
    if txt=='=':
        Button(window,text=txt,width=7,height=2,command=equal).grid(row=r,column=c,columnspan=1,pady=10,padx=7)
    elif txt=='C':
        Button(window,text=txt,width=7,height=2,command=clear).grid(row=r,column=c,columnspan=1,pady=10,padx=7)
    else:
        Button(window,text=txt,width=7,height=2,command=lambda t=txt:press(t)).grid(row=r,column=c,columnspan=1,pady=10,padx=7)

#running the GUI
window.mainloop()
