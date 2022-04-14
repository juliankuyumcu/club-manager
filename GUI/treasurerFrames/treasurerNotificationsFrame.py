from tkinter import *
from tkinter.ttk import Separator

from API.notificationData import notificationData
from API.week import week

from GUI.scrollableFrame import ScrollableFrame

class treasurerNotificationsFrame(Frame):
    def getNotifications(self):
        return notificationData.getTreasurerCoachNotifications()

    def createNotification(self, parent, message):
        notificationContainer = Frame(parent)

        body = Label(notificationContainer, text=message)
        body.pack(anchor='nw',side=BOTTOM)

        return notificationContainer

    def notificationBox(self, parent):
        container = LabelFrame(parent, text="Notification Box")

        scrollableFrame = ScrollableFrame(container,width=1280 * 0.8,height=720 * 0.8)
        scrollableFrame.pack_propagate(False)

        for notificationData in self.getNotifications():
            self.createNotification(scrollableFrame.scrollable_frame, notificationData).pack(anchor='nw',side=TOP)
            Separator(scrollableFrame.scrollable_frame,orient='horizontal').pack(anchor='nw',side=TOP,fill=X)
        
        scrollableFrame.pack()
        return container

    def __init__(self, parent):
        Frame.__init__(self, parent, name="treasurerNotifications")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        weekLabel = Label(self, text="Week: " + str(week.getCurrentWeek()))
        weekLabel.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        nav = Frame(self)

        coach = Button(nav, text="Coach List", command=lambda: parent.switchFrame("treasurerCoachList"))
        coach.grid(column=0,row=0)

        recentInvoice = Button(nav, text="Recent Invoice", command=lambda: parent.switchFrame("treasurerRecentInvoice"))
        recentInvoice.grid(column=1,row=0)

        globalInvoice = Button(nav, text="Global Invoice", command=lambda: parent.switchFrame("treasurerGlobalInvoice"))
        globalInvoice.grid(column=2,row=0)

        notifications = Button(nav, text="Notifications")
        notifications.grid(column=3,row=0)

        nav.pack(anchor='n',side=TOP)

        notificationBox = self.notificationBox(self)
        notificationBox.pack(side=TOP)