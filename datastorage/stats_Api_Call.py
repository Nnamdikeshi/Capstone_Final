import os
import base64
import requests


def stats_find(self):
        # Here we need our MySportsFeed User/Pass
        username = 'Nnamdikeshi'
        password = 'Kiidfrost23!'
        team = 'minnesota-vikings'
        sp = self.seasonGet.get()
        pos = self.positionGet.get()
        seasonPick = self.seasonGet.get() + '-regular'
        positionPick = self.positionGet.get()
        playername = self.name.get()
   
   
        """To Do - Fix the logic/flow in this api call"""
        
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