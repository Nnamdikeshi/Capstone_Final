from tkinter import *
from tkinter import messagebox as ms
import os
import sqlite3
import tkinter as tk


with sqlite3.connect('profiles.db') as db:
    c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL ,name TEXT NOT NULL,age INT NOT NULL, email TEXT NOT NULL, favplayer TEXT NOT NULL);')
db.commit()
db.close()

# user = main.profile_view.name
# print(user)
class Profile():
    def __init__(self,master):
    
        self.master=master
        self.master.geometry('400x450+250+170')
        self.master.title('PV.1.1')
        
        self.userLabel=Label(self.master,text='Welcome to your profile!' ,fg='purple').grid(row=0,column=0)

    
    
    
    
    
    
    
    
    
    
    
    
def main():
    #Create Object
	#and setup window
     root=Tk()
     root.iconbitmap(r'C:\Users\Nnamdi\Python_programs\Final Project\icons\profile.ico')
     myGUIWelcome=Profile(root)
     root.mainloop()

if __name__ == '__main__':
     main()