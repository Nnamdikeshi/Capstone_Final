from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import base64
import requests


class ApiGUI():

    def __init__(self,master):
        # Some useful variables
        self.season=StringVar()
        self.season.set("2017")
        self.position=StringVar()
        self.position.set("All")
        self.name=StringVar()
        # Build our window
        self.master=master
        self.master.geometry('450x450+250+170')
        self.master.title('STAT.1.1')
        
        # Welcome label
        self.welcomeLabel=Label(self.master,text='Welcome to the Vikings Stat Finder',fg='purple').grid(row=0,column=0)
        
        self.seasonLabel=Label(self.master,text='Season -->',fg='purple').grid(row=1,column=0)
        self.seasonGet = ttk.Combobox(self.master, textvariable=self.season)
        self.seasonGet['values'] = ("2017", "2016", "2015")
        self.seasonGet.current(0)
        self.seasonGet.grid(row=1, column=1)
        
        # Position label
        self.positionLabel=Label(self.master,text='Positon -->',fg='purple').grid(row=2,column=0)
        # Combo box for positon
        self.positionGet = ttk.Combobox(self.master, textvariable=self.position)
        self.positionGet['values'] = ("All", "QB", "HB", "FB", "WR", "TE", "C", "OG", "OT", "DT", "DE", "MLB", "LB", "CB", "S", "K", "H", "P")
        self.positionGet.current(0)
        self.positionGet.grid(row = 2, column = 1)
        
        # Search by last name
        self.nameLabel=Label(self.master,text='Enter Last Name -->',fg='purple').grid(row=3,column=0)
        self.nameEntry=Entry(self.master,textvariable=self.name).grid(row=3,column=1)
        # Find button
        self.findButton=Button(self.master,text=" FIND ",bg='purple4',command=self.find).grid(row=3,column=2)
        #Exit button
        self.exitButton=Button(self.master,text=" EXIT ",fg='red', bg='black',command=self.exit).grid(row=2,column=2)
        
        # Labels for when i have completed: Formatting .Json data
        self.attemptsLabel=Label(self.master,text="ATTEMPTS",fg='purple').grid(row=4,column=0)
        self.completionsLabel=Label(self.master,text='COMPLETIONS',fg='purple').grid(row=4,column=1)
        self.yardsLabell=Label(self.master,text='YARDS',fg='purple').grid(row=4,column=2)
        self.touchdownsLabel=Label(self.master,text="TD's",fg='purple').grid(row=4,column=3)

    def find(self):
        # Here we need our MySportsFeed User/Pass
        username = 'Nnamdikeshi'
        password = 'Kiidfrost23!'
        team = 'minnesota-vikings'
        sp = self.seasonGet.get()
        pos = self.positionGet.get()
        seasonPick = self.seasonGet.get() + '-regular'
        positionPick = self.positionGet.get()
        playername = self.name.get()
   
        try:
            # If season chosen is 2017 make request
            if sp == "2017":
                response = requests.get(
                    url = 'https://api.mysportsfeeds.com/v1.2/pull/nfl/2017-regular/cumulative_player_stats.json',
                    params = {
                        'team' : team, 'player' : playername, 'position' : pos,'sort' : 'stats.TD'
                    }, 
                    headers = {"Authorization": "Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
                    }
                )#.json()
                
                ''' Here lies the last Issue to fix. 
                Users will see raw code with hard to read stats. 
                A fix is set for the near future. '''
                # Issue start
                f = open('stats.txt', 'w' )
                f.write(response.text)
                f.close()
                osCommandString = "notepad.exe stats.txt"
                os.system(osCommandString)
                #open('stats.txt').readline().split(':')[1].strip()
                
                print('Response HTTP Status Code: {status_code}'.format(
                    status_code=response.status_code))
                #print('Response HTTP Response Body: {content}'.format(
                 #   content=response.content))
                #Issue End
                
            # If season chosen is 2016 make request
            elif sp == "2016":
                response = requests.get(
                    url = 'https://api.mysportsfeeds.com/v1.2/pull/nfl/2016-regular/cumulative_player_stats.json',
                    params = {
                        'team' : team, 'player' : playername, 'position' : pos,'playerstats' : 'Comp,Yds,TD'
                    }, 
                    headers = {"Authorization": "Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
                    }
                )#.json()
                
                # Issue start
                f = open('stats.txt', 'w' )
                f.write(response.text)
                f.close()
                osCommandString = "notepad.exe stats.txt"
                os.system(osCommandString)
                #open('stats.txt').readline().split(':')[1].strip()
                
                # response.content.split("@abbreviation")[1]
                # print(response.content)
                
                print('Response HTTP Status Code: {status_code}'.format(
                    status_code=response.status_code))
                print('Response HTTP Response Body: {content}'.format(
                    content=response.content))
                # Issue End
            # If season chosen is 2015 make request
            elif sp == "2015":
                response = requests.get(
                    url = 'https://api.mysportsfeeds.com/v1.2/pull/nfl/2017-regular/cumulative_player_stats.json',
                    params = {
                        'team' : team, 'player' : playername, 'position' : pos,'playerstats' : 'Comp,Yds,TD'
                    }, 
                    headers = {"Authorization": "Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
                    }
                )#.json()
                
                # Issue start
                f = open('stats.txt', 'w' )
                f.write(response.text)
                f.close()
                osCommandString = "notepad.exe stats.txt"
                os.system(osCommandString)
                #open('stats.txt').readline().split(':')[1].strip()
                
                # response.content.split("@abbreviation")[1]
                # print(response.content)
                
                print('Response HTTP Status Code: {status_code}'.format(
                    status_code=response.status_code))
                print('Response HTTP Response Body: {content}'.format(
                    content=response.content))
                # Issue End
                    
            elif pos == "All":
                response = requests.get(
                    url = 'https://api.mysportsfeeds.com/v1.2/pull/nfl/2017-regular/cumulative_player_stats.json',
                    params = {
                        'team' : team, 'player' : playername,'playerstats' : 'Comp,Yds,TD'
                    }, 
                    headers = {"Authorization": "Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
                    }
                )#.json()
                
                # Issue start
                f = open('stats.txt', 'w' )
                f.write(response.text)
                f.close()
                osCommandString = "notepad.exe stats.txt"
                os.system(osCommandString)
                #open('stats.txt').readline().split(':')[1].strip()
                
                # response.content.split("@abbreviation")[1]
                # print(response.content)
                
                print('Response HTTP Status Code: {status_code}'.format(
                    status_code=response.status_code))
                print('Response HTTP Response Body: {content}'.format(
                    content=response.content))
                # Issue End
            else:
                ms.showerror('Error!','Season not available')
        except: 
            print("Unexpected error:", sys.exc_info()[0])
    def exit(self):
        self.master.destroy()
        