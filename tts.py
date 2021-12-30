import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

root = tk.Tk() 
root.title('Text to Speech')
root.configure(background="pink")

label = tk.Label(root,text="Type something here:",
font="arial 25 bold",bg="pink",fg="blue")
label.pack()

textarea = tk.Entry(root,width=30,font="arial 20")
textarea.pack()

def speak(text):
    engine.say(text)
    engine.runAndWait()

button = tk.Button(root,text="Speak",font="arial 25 bold",
bg="yellow",fg="blue",command=lambda:speak(textarea.get()))
button.pack()

root.mainloop()

