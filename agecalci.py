from tkinter import *

root = Tk()
root.title("AI Age calculator")
root.geometry("280x100")


def end():
    root.destroy()


def do():
    global button
    age = int(e.get())
    print(age)
    e.destroy()
    button.destroy()
    myLabel.destroy()
    if age != 0 and age <= 100:
        myLabel2 = Label(root, text=f"You are {age} years old", font=30)
    else:
        myLabel2 = Label(root, text='Are you retarded?', font=30)

    myLabel2.place(relx=0.5, rely=0.2, anchor=CENTER)
    button = Button(root, text="      Close      ", font=20, command=end, borderwidth=2)
    button.place(relx=0.5, rely=0.68, anchor=CENTER)


def capture(event):
    if e.get().isnumeric():
        button['state'] = 'normal'

    else:
        button['state'] = 'disabled'


button = Button(root, text="      ok      ", state="disabled", font=20, command=do)
button.grid(row=2)

e = Entry(root, font=20, borderwidth=5)
e.grid(row=1)

e.bind("<KeyRelease>", capture)

myLabel = Label(root, text="              Enter your age in years             ", font=20)
myLabel.grid(row=0)

root.resizable(False, False)
root.mainloop()