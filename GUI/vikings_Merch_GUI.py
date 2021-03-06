import os
import time
import sqlite3import datetime
import tkinter as tkfrom tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datastorage.create_Merch_DB import CreateDB
class MerchGUI():#This is the class defining the first welcoming window.    def __init__(self,master):        #This is the GUI for the starting Menu area. Features five buttons for navigating towards the Buying Merch for week 1, and displaying the item list for each week (Updates) EXIT#
                  CreateDB.setupDB()
          CreateDB.setupWeeks()
                    self.master=master          self.master.geometry('350x300+250+170')          self.master.title('VMA.2.0')          # self.bar = Scrollbar(self.master)          self.label1=Label(self.master,text='Welcome to the Vikings Merch Store!',fg='purple', font = ('',15)).grid(row=0,column=1)          self.button1=Button(self.master,text="Buy Week 1 SuperBowl VII",fg='green',bg='purple',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.gotomerchandisebuyer).grid(row=1,column=1)          self.button2=Button(self.master,text="Week One Merch List",fg='yellow',bg='purple',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.gotoweekOneMerch).grid(row=2,column=1)
          self.button3=Button(self.master,text="Week Two Merch List",fg='yellow',bg='purple',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.gotoweekTwoMerch).grid(row=3,column=1)
          self.button4=Button(self.master,text="Week Three Merch List",fg='yellow',bg='purple',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.gotoweekThreeMerch).grid(row=4,column=1)          self.button5=Button(self.master,text="Exit",fg='red',bg='black',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.exit).grid(row=5,column=1)    def exit(self):        #Exit protocol for the exit button. This part is completely done.#          self.master.destroy()    def gotomerchandisebuyer(self):        #This is the Merchandise Buyer GUI#              root2=Toplevel(self.master)          myGUI=merchandisebuyer(root2)
              def gotoweekOneMerch(self):        #This is where the weekOneMerch is kept          root2=Toplevel(self.master)          mygui=weekOneMerch(root2)
          
    def gotoweekTwoMerch(self):
        #This is where the weekTwoMerch is kept
          root2=Toplevel(self.master)
          mygui=weekTwoMerch(root2)
              def gotoweekThreeMerch(self):
        #This is where weekThreeMerch is kept
          root2=Toplevel(self.master)
          mygui=weekThreeMerch(root2)
          class merchandisebuyer():     #class created for the Merch buyer GUI and processing the numbers (pain in the ass to make)#    def __init__(self,master):          self.idnum=StringVar()          self.buyname=StringVar()
          self.colorname=StringVar()
          self.merchquantity=StringVar()          self.box_value = StringVar()
          self.box1_value = StringVar()
          self.deletename=StringVar()
                    self.master=master          self.master.geometry('900x450+100+200')          self.master.title('*Buy Merch*')
                    self.label2=Label(self.master,text='Welcome to the Vikings Offseason SuperBowl Sale!!',fg='purple').grid(row=0,column=0)          self.label2=Label(self.master,text='Please Select an Item:',fg='black').grid(row=3,column=0)          self.label2=Label(self.master,text='Please Enter Customer Name:',fg='black').grid(row=4,column=0)
          self.label2=Label(self.master,text='Please Select Color:',fg='black').grid(row=5,column=0)
          self.label2=Label(self.master,text='Please Select a Location:',fg='black').grid(row=6,column=0)
          self.label2=Label(self.master,text='Please Enter Buy Quantity:',fg='black').grid(row=7,column=0)
          self.label3=Label(self.master,text='****Total Sold for Week 1****',fg='purple').grid(row=8,column=1)
                    self.idLabel = Label(self.master, text="ID", width=10)
          self.idLabel.grid(row=9, column=0)
          self.idFindLabel = Label(self.master, text="Item Name", width=10)
          self.idFindLabel.grid(row=9, column=1) 
          self.colorLabel = Label(self.master, text="Color",width=10)
          self.colorLabel.grid(row=9, column=2)
          self.buyernameLabel = Label(self.master, text="BuyerName", width=10)
          self.buyernameLabel.grid(row=9, column=3)
          self.locationLabel = Label(self.master, text="Location", width=10)
          self.locationLabel.grid(row=9, column=4)
          self.quantityLabel = Label(self.master, text="Quantity", width=10)
          self.quantityLabel.grid(row=9, column=5)
          self.dateLabel = Label(self.master, text="Date", width=10)
          self.dateLabel.grid(row=9, column=6)           
          self.hatLabel = Label(self.master, text="*Hat W/Logo*\nItem#: '1' '2' or '3'",fg='yellow',bg='purple')
          self.hatLabel.grid(row=5, column=2) 
          self.shirtLabel = Label(self.master, text="*Shirt with viking Logo*\nItem#: '4' '5' or '6'",fg='yellow',bg='purple')
          self.shirtLabel.grid(row=6, column=2) 
          self.shortsLabel = Label(self.master, text="*Shorts with Viking Logo*\nItem#: '7' '8' '9'",fg='yellow',bg='purple')
          self.shortsLabel.grid(row=7, column=2) 
                    self.merchname=ttk.Combobox(self.master,textvariable=self.idnum)
          self.merchname['values'] = ('Hat', 'Shirt', 'Shorts', 'Headband', 'Wristband', 'Football', 'Lanyard', 'Poster', 'jersey')
          self.merchname.current(1)
          self.merchname.grid(row=3,column=1)
                    self.myname=Entry(self.master,textvariable=self.buyname).grid(row=4,column=1)
          self.garbname=Entry(self.master,textvariable=self.deletename).grid(row=4,column=2)
          # Color Options
          self.color = ttk.Combobox(self.master, textvariable=self.box_value)
          self.color['values'] = ('Yellow', 'Purple', 'Black')
          self.color.current(1)
          self.color.grid(column=1, row=5)
          # Location options
          self.loc = ttk.Combobox(self.master, textvariable=self.box1_value)
          self.loc['values'] = ('Minneapolis', 'St. Paul')
          self.loc.current(0)
          self.loc.grid(column=1, row=6)
          
          
          self.merchQuan=Entry(self.master,textvariable=self.merchquantity).grid(row=7,column=1)  
                    self.button6=Button(self.master,text="Buy",fg='green',command=self.merchbuyer).grid(row=3,column=2)          self.button7=Button(self.master,text="Exit",fg='red',bg='black',command=self.exit).grid(row=3,column=3)
          self.button8=Button(self.master,text="DELETE",fg='red',command=self.deleteRecords).grid(row=4,column=3)
          self.button9=Button(self.master,text="*Prices*",fg='purple',command=self.getPrices).grid(row=4,column=4)
          self.showallsold()
          
    # Show our table from vikingsdatabase
    def getPrices(self):
         lines = ["PRICES", "Hat: - $10.00", "Shirt: - $20.00", "Shorts: - $25.00", "Headband: - $8.00", "Wristband: - $7.00", "Football: - $15.00", "Lanyard: - $5.00", "Poster: - $10.00", "jersey: - $20.00"]
         messagebox.showinfo("** PRICES **", "\n".join(lines))
         
    def showallsold(self):
        
         data = CreateDB.readsold()

         for index, dat in enumerate(data):
             Label(self.master, text=dat[0],fg='purple').grid(row=index+10, column=0)
             Label(self.master, text=dat[1],fg='purple').grid(row=index+10, column=1)
             Label(self.master, text=dat[2],fg='purple').grid(row=index+10, column=2)
             Label(self.master, text=dat[3],fg='purple').grid(row=index+10, column=3)
             Label(self.master, text=dat[4],fg='purple').grid(row=index+10, column=4)
             Label(self.master, text=dat[5],fg='purple').grid(row=index+10, column=5)
             Label(self.master, text=dat[6],fg='purple').grid(row=index+10, column=6)
    def merchbuyer(self):                     
          # Brings us back to merch buyer frame          self.master.update()
          self.master.deiconify()
          self.dynamic_data_entry()
              def dynamic_data_entry(self):          #this is what adds the data to the database.
          merchandise=str(self.merchname.get())
          amount=int(self.merchquantity.get())
          custname=str(self.buyname.get())
          colorname=str(self.color.get())
          locationname=str(self.loc.get())
          timestamp = str(datetime.datetime.now().date())

          CreateDB.insertBought(merchandise, colorname, custname, locationname, amount, timestamp)
         
          self.showallsold()
          # If it got this far... Success!
          self.label1=Label(self.master,text='Your Purchase was successfull ' + custname,fg='green').grid(row=8,column=0)
          
    # To calculate how much was sold this week      
    def howMuchSold(self):
        return
        
            # Delete function with sql DELETE statement and UPDATE merch stock
    def deleteRecords(self):
          id = int(self.deletename.get())
          print(id)
          CreateDB.deleteOrder(id)
          self.showallsold()
          return

              def exit(self):          #Exit protocol for the exit button. This part is completely done.#          self.master.destroy()
     class weekOneMerch():     #class created to see weekOneMerch that have been previously logged#
    from datastorage.create_Merch_DB import CreateDB    def __init__(self,master):         self.master=master         self.master.geometry('600x210+100+200')         self.master.title('weekOneMerch')         self.connection = sqlite3.connect('databases/vikingsdatabase.db')         self.cur = self.connection.cursor()         self.idLabel = Label(self.master, text="ID", width=10)         self.idLabel.grid(row=0, column=0)         self.nameLabel = Label(self.master, text="Name", width=10)         self.nameLabel.grid(row=0, column=1)         self.soldLabel = Label(self.master, text="Sold", width=10)         self.soldLabel.grid(row=0, column=2)         self.availableLabel = Label(self.master, text="Available", width=10)         self.availableLabel.grid(row=0, column=3)         self.showallweekMerch()
             def showallweekMerch(self):         week_number = 1         data = self.CreateDB.readfromdatabase(week_number)                   for index, dat in enumerate(data):             Label(self.master, text=dat[0]).grid(row=index+1, column=0)             Label(self.master, text=dat[1]).grid(row=index+1, column=1)             Label(self.master, text=dat[2]).grid(row=index+1, column=2)             Label(self.master, text=dat[3]).grid(row=index+1, column=3)           
             class weekTwoMerch():
     #class created to see weekTwoMerch that have been previously logged#
    from datastorage.create_Merch_DB import CreateDB
    def __init__(self,master):
         self.master=master
         self.master.geometry('600x210+100+200')
         self.master.title('weekTwoMerch')
         self.connection = sqlite3.connect('databases/vikingsdatabase.db')
         self.cur = self.connection.cursor()
         self.idLabel = Label(self.master, text="ID", width=10)
         self.idLabel.grid(row=0, column=0)
         self.nameLabel = Label(self.master, text="Name", width=10)
         self.nameLabel.grid(row=0, column=1)
         self.soldLabel = Label(self.master, text="Sold", width=10)
         self.soldLabel.grid(row=0, column=2)
         self.availableLabel = Label(self.master, text="Available", width=10)
         self.availableLabel.grid(row=0, column=3)
         self.showallweekMerch()
         
    def showallweekMerch(self):
         week_number = 2
         data = self.CreateDB.readfromdatabase(week_number)
          
         for index, dat in enumerate(data):
             Label(self.master, text=dat[0]).grid(row=index+1, column=0)
             Label(self.master, text=dat[1]).grid(row=index+1, column=1)
             Label(self.master, text=dat[2]).grid(row=index+1, column=2)
             Label(self.master, text=dat[3]).grid(row=index+1, column=3) 

class weekThreeMerch():
     #class created to see weekOneMerch that have been previously logged#
    from datastorage.create_Merch_DB import CreateDB
    def __init__(self,master):
        #
         self.master=master
         self.master.geometry('600x210+100+200')
         # Title Name goes here
         self.master.title('weekThreeMerch')
         self.connection = sqlite3.connect('databases/vikingsdatabase.db')
         self.cur = self.connection.cursor()
         self.idLabel = Label(self.master, text="ID", width=10)
         self.idLabel.grid(row=0, column=0)
         self.nameLabel = Label(self.master, text="Name", width=10)
         self.nameLabel.grid(row=0, column=1)
         self.soldLabel = Label(self.master, text="Sold", width=10)
         self.soldLabel.grid(row=0, column=2)
         self.availableLabel = Label(self.master, text="Available", width=10)
         self.availableLabel.grid(row=0, column=3)
         self.showallweekMerch()
         
    def showallweekMerch(self):
         week_number = 3
         data = self.CreateDB.readfromdatabase(week_number)
          
         for index, dat in enumerate(data):
             Label(self.master, text=dat[0]).grid(row=index+1, column=0)
             Label(self.master, text=dat[1]).grid(row=index+1, column=1)
             Label(self.master, text=dat[2]).grid(row=index+1, column=2)
             Label(self.master, text=dat[3]).grid(row=index+1, column=3) 