from re import L
from tkinter import *
from API.login import login

class memberLoginFrame(Frame):

    def login(self, username, password):
        l = login()
        if (l.memberLogin(username, password)):
            Label(self, text="Logged in").place(anchor='s',relx=0.5, rely=0.5)
            
        else:
            Label(self, text="Incorrect login!").place(anchor='s',relx=0.5, rely=0.5)

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="memberLogin")
        self.config(width=1280, height=720)

        back = Button(self, text="Back to login choice", command=lambda: parent.switchFrame("loginChoice"))
        back.place(anchor='nw')

        container = Frame(self)
        heading = Label(container, text="Member Login", font=("Arial Bold", 25), pady=10)
        heading.pack(side=TOP)

        usernameS = Frame(container)
        usernameL = Label(usernameS, text="Username:")
        usernameL.pack(anchor='w',side=LEFT)
        usernameF = Entry(usernameS)
        usernameF.pack(anchor='w',side=LEFT)
        usernameS.pack(anchor='w',side=TOP)

        passwordS = Frame(container)
        passwordL = Label(passwordS, text="Password:")
        passwordL.pack(anchor='w',side=LEFT)
        passwordF = Entry(passwordS)
        passwordF.pack(anchor='w',side=LEFT)
        passwordS.pack(anchor='w',side=TOP)

        submit = Button(container, text="Login", command=lambda: parent.switchFrame("membercontainer")) #self.login(usernameF.get(), passwordF.get()) 
        submit.pack(anchor='w',side=BOTTOM)
        container.place(relx=0.5, rely=0.33, anchor="center")

