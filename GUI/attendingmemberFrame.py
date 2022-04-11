from re import L
from tkinter import *


class attendingFrame(Frame):
    """def is_attending():
        

    def is_not_attending():"""
        

    def __init__(self, parent):
        Frame.__init__(self, parent, name="attendingFrame")
        self.config(width=1280, height=720)
        isAttending = Button(self, text="I am Attending this week",command=lambda: self.is_attending())
        isAttending.place("nw")

        isNotAttending = Button(self, text="I am Attending NOT week",command=lambda: self.is_not_attending())
        isNotAttending.place("w")
        