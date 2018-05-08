from tkinter import *
from tkinter import messagebox as ms
import os
import sqlite3
import tkinter as tk
import webbrowser
#from PIL import ImageTk
#from PIL import Image as PilImage

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()
# Creat our users table if it doesnt already exist
c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

#main Class
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_password2 = StringVar()
        #Create Widgets
        self.login_widgets()
        
    #Login Function
    def login(self):
        '''This Logs Users in with correct credentials'''
        
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            
            # Clears GUI
            self.logf.pack_forget()
            profile_name = self.username.get()
            self.head['text'] = profile_name + '\n Logged In'
            self.account_widgets(profile_name)
            # Who is logged in?
            

            # Photo testing
            # img1 = PhotoImage(file="test.png")
            # lab1 = Label(root, image=img1, text = "test")
            # lab1.image = img1
            # lab1.pack()
            
            # image = ImageTk.PhotoImage(PilImage.open('test.png'))
            # lbl = tk.Label(window, image = img).pack()

            #self.account_widgets()
            #open_merch()
        else:
            ms.showerror('Oops!','Username or Password Incorrect')
            
    def open_merch(self):
        ''' This opens up the mock merchandise buyer app '''
     
        os.system('python vikings_Merch_app.py')
        
    def new_user(self):
        ''' This creates our new user if everything checks out'''
        
    	# Establish Connection
        passw1 = ''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        elif not self.n_username.get():
            ms.showerror('Error!', 'Username cannot be blank.')
            self.cr()
        elif self.n_password.get() != self.n_password2.get():
            ms.showerror('Error!', 'Passwords do no match.')
            self.cr()
        elif len(self.n_password.get()) < 6:
            ms.showerror('Error!','Password must be atleast 6 characters long.')
            self.cr()
        else:
            ms.showinfo('Success!','Account Created!')
            
            #Create New Account 
            insert = 'INSERT INTO user(username,password) VALUES(?,?)'
            c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
            db.commit()
            self.log()
        # Clears our screen for profile view
    def profile_view(self, profile_name):
        name = profile_name
        self.prf.pack_forget()
        #label.pack_forget()
        self.head ['text'] = name + "'s Profile "
        
        # Frame Packing Methods
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
        
        # Clears our Creat Account screen for new entry
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.n_password2.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
        # This opens up the (Official) Vikings NFL shop 
    def nfl(self):
        webbrowser.open('http://www.nflshop.com/Minnesota_Vikings_', new=0)
        
        # Exit
    def exit(self):
        self.master.destroy()
    #Draw Widgets
    def login_widgets(self):
        
        # GUI header
        self.head = Label(self.master,text = 'LOGIN',fg = 'Purple4',font = ('',35),pady = 10)
        self.head.pack()
        
        # Set up our Login frame
        self.logf = Frame(self.master,padx =10,pady = 10)
        
        # Username label/entry
        Label(self.logf,text = 'Username: ',fg = 'Purple4',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5, font = ('',15)).grid(row=0,column=1)
        
        # Password label/entry
        Label(self.logf,text = 'Password: ',fg = 'purple4', font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        
        # Login button
        Button(self.logf,text = ' Login ',bg = 'green4',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid(row=2,column=0)
        
        # Switch to Create Account button
        Button(self.logf,text = ' Create Account ',fg = 'gold', bg = 'purple4',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        # Set up our Create Account frame
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        
        # Password label/entry
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        
        # Confirmed password label/entry
        Label(self.crf,text = 'Re-Enter Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password2,bd = 5, font = ('',15),show = '*').grid(row=2,column=1)
        
        # Create account button
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid(row=4, column=0)
        
        # Back to login button
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=4,column=1)

    def account_widgets(self, profile_name):
        ''' This creates our Top Menu in the window '''
        
        # Set frame
        self.prf = Frame(self.master,padx =10,pady = 10)
        # Change our icon and title
        self.master.title("Menu")
        self.master.iconbitmap(r'C:\Users\Nnamdi\Python_programs\Final Project\icons\helm.ico')
        # Profile label/button
        Label(self.prf,text = ' Profile --> ',fg = 'Purple4',pady=5,padx=5).grid(row = 1, column = 0)
        Button(self.prf,text = ' Profile ',bg = 'aqua',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.profile_view(profile_name)).grid(row=1,column=1)
        
        # Mock Merch label/button
        Label(self.prf,text = ' Buy Merchandise\n (Creators Shop) ',fg = 'purple4',pady=5,padx=5).grid(sticky = W)
        Button(self.prf,text = ' Buy (practice) ',bg = 'green3',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.open_merch).grid(row=2,column=1)
        
        # Real NFL Merch label/button
        Label(self.prf,text = ' Buy Merchandise\n (NFL Shop) ',fg = 'purple4',pady=5,padx=5).grid(sticky = W)
        Button(self.prf,text = ' Buy (Actual) ',bg = 'green4',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.nfl).grid(row=3,column=1)
        
        # View Stats API label/button
        Label(self.prf,text = ' View Vikings Stats ',fg = 'purple4',pady=5,padx=5).grid(sticky = W)
        Button(self.prf,text = ' Stats ',fg = 'gold', bg = 'purple4',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=4,column=1)
        self.prf.pack()
        
        # Exit Button 
        Button(self.prf,text = ' Exit ',fg = 'red2', bg = 'black',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.exit).grid(row=4,column=2)
        self.prf.pack()
        
        
    
if __name__ == '__main__':
    #Create Object
    #and setup window
    root = Tk()
    # App Login Picture
    image = tk.PhotoImage(file="icons\glitter.gif")
    label = tk.Label(image=image)
    label.pack()
    # Login page icon
    root.iconbitmap(r'C:\Users\Nnamdi\Python_programs\Final Project\icons\if_Login_73221.ico')
    root.title('Login Form')
    main(root)
    root.mainloop()