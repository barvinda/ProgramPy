from tkinter import *
import json

#creating the tkinter window
window=Tk()

#loading the dictionary into a variable
data=json.load(open("076 data.json"))

#function that translates word
def translate():
    #get the word from text box in tkinter (e1)
    word = e1_value.get().lower()
    if word in data:
        t1.delete(1.0, END)
        if type(data[word])==list:
            for item in data[word]:
                t1.insert(END, item)
        else:
            t1.insert(END, data[word])
    #return message
    else:
        t1.delete(1.0, END)
        t1.insert(END, "The word doesn't exist! Try again")

#creating the window features
b1= Button(window,text="Translate",command=translate)
b1.grid(row=1,column=2)

e1_value= StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=1,column=1)

t1=Text(window, height=10, width=35)
t1.grid(row=2,column=1,rowspan=5,columnspan=2)

#ending the loop
window.mainloop()
