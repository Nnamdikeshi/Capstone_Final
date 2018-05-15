import os
import tkinter as tk
from datastorage.create_Profile_DB import CreateDB
from tkinter import *
from tkinter import messagebox as ms


    # profile GUI class    
class Profile():
    def __init__(self,master):
    
        from __main__ import profile_name
        global pn 
        pn = profile_name
        global name
        name = pn
        
        
        # Build our GUI
        self.master=master
        self.master.geometry('600x400+250+170')
        self.master.title('PV.1.1')

        # Welcome label
        self.welcomeLabel=Label(self.master,text='Welcome to your profile ' + pn,fg='purple').grid(row=0,column=0)
        
        # Name labels
        self.nameLabel=Label(self.master,text=' Name: ',fg='purple').grid(row=1,column=0)
        self.userLabel=Label(self.master,text=pn,fg='purple').grid(row=1,column=1)
        
        # Age label
        self.aqeLabel=Label(self.master,text=' Age: ' ,fg='purple').grid(row=2,column=0)
        
        # Email label
        self.emailLabel=Label(self.master,text=' Email: ',fg='purple').grid(row=3,column=0)
        
        # Favorite player label
        self.favplayerLabel=Label(self.master,text=' Favorite Player: ', fg='purple').grid(row=4, column=0)
        
        # Edit profile button
        self.editButton=Button(self.master,text=" EDIT ",fg='gold', bg='purple4',command=self.editprofilewidgets).grid(row=3,column=3)
        
        
        self.showallprofile(name)
        
        
    def editprofilewidgets(self):
        # profile Variables
        self.ageGet = IntVar()
        self.emailGet = StringVar()
        self.favGet = StringVar()
        
        # Entry widgets
        self.ageEntry=Entry(self.master,textvariable=self.ageGet).grid(row=2, column=2)
        self.emailEntry=Entry(self.master,textvariable=self.emailGet).grid(row=3, column=2)
        self.favplayerEntry=Entry(self.master,textvariable=self.favGet).grid(row=4, column=2)
        
        # Add button
        self.editButton=Button(self.master,text=" ADD ",fg='gold', bg='purple4',command=self.changeprofile).grid(row=4,column=3)
        
    def changeprofile(self):
    
        # Get our info from our entries
        age = int(self.ageGet.get())
        email = self.emailGet.get()
        favplayer = self.favGet.get()
        #name = pn
        
        CreateDB.update(name, age, email, favplayer)
        self.showallprofile(name)
            
    def showallprofile(self, name):
        pname = name
        data = CreateDB.showAll(pname)
        # Itterates through database and appends what we want
        for index, dat in enumerate(data):
            Label(self.master, text=dat[2],fg='purple').grid(row=2, column=1)
            Label(self.master, text=dat[3],fg='purple').grid(row=3, column=1)
            Label(self.master, text=dat[4],fg='purple').grid(row=4, column=1)
            