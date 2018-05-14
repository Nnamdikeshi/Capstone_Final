import os
import time
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Establish connection to our db
          self.button3=Button(self.master,text="Week Two Merch List",fg='yellow',bg='purple',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.gotoweekThreeMerch).grid(row=3,column=1)
          self.button4=Button(self.master,text="Week Three Merch List",fg='yellow',bg='purple',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.gotoweekThreeMerch).grid(row=4,column=1)
          
          
    def gotoweekThreeMerch(self):
        #This is where the weekTwoMerch is kept
          root2=Toplevel(self.master)
          mygui=weekThreeMerch(root2)
          
        #This is where weekThreeMerch is kept
          root2=Toplevel(self.master)
          mygui=weekThreeMerch(root2)
          
          self.colorname=StringVar()
          self.merchquantity=StringVar()
          self.box1_value = StringVar()
          self.deletename=StringVar()
          
          
          self.label2=Label(self.master,text='Please Select Color',fg='black').grid(row=5,column=0)
          self.label2=Label(self.master,text='Please Select a Location',fg='black').grid(row=6,column=0)
          self.label2=Label(self.master,text='Please Enter Buy Quantity',fg='black').grid(row=7,column=0)
          self.label3=Label(self.master,text='****Total Sold for Week 1****',fg='purple').grid(row=8,column=1)
          
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
          
          self.garbname=Entry(self.master,textvariable=self.deletename,text="test").grid(row=4,column=2)
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
          
          self.button8=Button(self.master,text="DELETE",fg='red',command=self.deleteRecords).grid(row=4,column=3)
          self.button9=Button(self.master,text="*Prices*",fg='purple',command=self.getPrices).grid(row=4,column=4)
          
          self.connection = sqlite3.connect('databases/vikingsdatabase.db')
          self.cur = self.connection.cursor()
          self.showallweekOneMerch()
          
    # Show our table from vikingsdatabase
    def getTotal(self):
         self.cur.execute("SELECT SUM(Sold) WHERE Name = 'Hat w/Logo' FROM sold")
         
    def getPrices(self):
         lines = ["PRICES", "Hats: - $15.00", "Shirts: - $20.00", "Shorts: - $25.00"]
         messagebox.showinfo("** PRICES **", "\n".join(lines))
         
    def readfromdatabase(self):
         self.cur.execute('SELECT * FROM sold')
         return self.cur.fetchall()
     
    def showallweekOneMerch(self):
          
         data = self.readfromdatabase()

         for index, dat in enumerate(data):
             Label(self.master, text=dat[0],fg='purple').grid(row=index+10, column=0)
             Label(self.master, text=dat[1],fg='purple').grid(row=index+10, column=1)
             Label(self.master, text=dat[2],fg='purple').grid(row=index+10, column=2)
             Label(self.master, text=dat[3],fg='purple').grid(row=index+10, column=3)
             Label(self.master, text=dat[4],fg='purple').grid(row=index+10, column=4)
             Label(self.master, text=dat[5],fg='purple').grid(row=index+10, column=5)
             
          # Brings us back to merch buyer frame
          self.master.deiconify()
          self.dynamic_data_entry()
          
          """ Logic could be a little cleaner but it works """
             isBought = False
             idFind=int(self.idnum.get())
             amount=int(self.merchquantity.get())
             print (amount)
             if idFind == 1: 
                # Unsupported type dilemma conquered ^_^
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 1",(amount,amount))
                conn.commit()
                idFind = "Hat w/Logo" 
                print (idFind)
                
             elif idFind == 2:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 2",(amount,amount))
                conn.commit()
                idFind = "Hat w/Logo"                              
                print (idFind)
                
             elif idFind == 3:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 3",(amount,amount))               
                conn.commit()
                idFind = "Hat w/Logo"
                print (idFind)
                
             elif idFind == 4:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 4",(amount,amount))
                conn.commit()
                idFind = "Shirt w/Logo"
                print (idFind)
                
             elif idFind == 5:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 5",(amount,amount))
                conn.commit()
                idFind = "Shirt w/Logo"
                print (idFind)
                
             elif idFind == 6:                
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 6",(amount,amount))
                conn.commit()
                idFind = "Shirt w/Logo"
                print (idFind)
             
             elif idFind == 7:
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 7",(amount,amount))
                idFind = "Shorts w/Logo"
                print (idFind)
             elif idFind == 8:
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 8",(amount,amount))
                idFind = "Shorts w/Logo"
                print (idFind)
             elif idFind == 9:
                sold = int(self.merchquantity.get())
                c.execute("UPDATE for_sale_week1 SET Sold = +? , Available = Available - ? WHERE ID = 9",(amount,amount))
                idFind = "Shorts w/Logo"
                print (idFind) 
                 
             else:
                #message box display
                messagebox.showerror("Error", "The ID # you entered doesn't exist in our system... \nClick 'OK'  & Try another purchase")
                self.merchname.delete(0, END)
                return 
               

             custname=str(self.buyname.get())
             print (custname)          
             colorname=str(self.color.get())
             print (colorname)
             locationname=str(self.loc.get())
             print (locationname)
             timestamp = str(datetime.datetime.now().date())
              # SQL query INSERT our details
             self.showallweekOneMerch()
             # If it got this far... Success!
             self.label1=Label(self.master,text='Your Purchase was successfull ' + custname,fg='green').grid(row=8,column=0)
             
             # Error message for ValueError
             messagebox.showerror('Error','Please enter numbers ie: "1", "2", or "3" in their corrosponding boxes!')
             #self.merchname.selection_clear()
             #self.merchname.focus()
             self.label1=Label(self.master,text='Your Purchase was unsuccessfull. Sorry ' + custname,fg='red').grid(row=8,column=0)
             return  
    def deleteRecords(self):
    
          id = self.deletename.get()
          c.execute("DELETE FROM sold WHERE ID=?", (id,))
          conn.commit()
          c.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='sold'")
          conn.commit()
          
          self.showallweekOneMerch()
          return
          
     
         
             
     #class created to see weekTwoMerch that have been previously logged#
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
         self.colorLabel = Label(self.master, text="Color", width=10)
         self.colorLabel.grid(row=0, column=2)
         self.soldLabel = Label(self.master, text="Sold", width=10)
         self.soldLabel.grid(row=0, column=3)
         self.availableLabel = Label(self.master, text="Available", width=10)
         self.availableLabel.grid(row=0, column=4)
         self.showallweekThreeMerch()
         
    # Show our sock with SELECT
    def readfromdatabase(self):
         self.cur.execute("SELECT * FROM for_sale_week2")
         return self.cur.fetchall()
     
    def showallweekTwoMerch(self):
          
         data = self.readfromdatabase()
          
         for index, dat in enumerate(data):
             Label(self.master, text=dat[0]).grid(row=index+1, column=0)
             Label(self.master, text=dat[1]).grid(row=index+1, column=1)
             Label(self.master, text=dat[2]).grid(row=index+1, column=2)
             Label(self.master, text=dat[3]).grid(row=index+1, column=3)
             Label(self.master, text=dat[4]).grid(row=index+1, column=4)

class weekThreeMerch():
     #class created to see weekOneMerch that have been previously logged#
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
         self.colorLabel = Label(self.master, text="Color", width=10)
         self.colorLabel.grid(row=0, column=2)
         self.soldLabel = Label(self.master, text="Sold", width=10)
         self.soldLabel.grid(row=0, column=3)
         self.availableLabel = Label(self.master, text="Available", width=10)
         self.availableLabel.grid(row=0, column=4)
         self.showallweekThreeMerch()
    # Show our sock with SELECT
    def readfromdatabase(self):
         self.cur.execute("SELECT * FROM for_sale_week3")
         return self.cur.fetchall()
     
    def showallweekThreeMerch(self):
          
         data = self.readfromdatabase()
          
         for index, dat in enumerate(data):
             Label(self.master, text=dat[0]).grid(row=index+1, column=0)
             Label(self.master, text=dat[1]).grid(row=index+1, column=1)
             Label(self.master, text=dat[2]).grid(row=index+1, column=2)
             Label(self.master, text=dat[3]).grid(row=index+1, column=3)
             Label(self.master, text=dat[4]).grid(row=index+1, column=4)