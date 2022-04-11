from re import L
from tkinter import *
from GUI.attendingmemberFrame import attendingFrame

class membercontainer():
    def __init__(self, parent):
        self.children = {
            "attendingFrame": attendingFrame,}
            # "pay": payFrame,
            # "notification": notificationFrame}
        Frame.__init__(self, parent, name="membercontainer")
        attendingFrame.pack()