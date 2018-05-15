import sqlite3


class CreateDB(object):    
    """DB initializes and manipulates SQLite3 databases."""
    # Set up our DB
    
    def setupDB():
    
        # Some default variables
        createsold = 'CREATE TABLE IF NOT EXISTS sold (ID INTEGER PRIMARY KEY AUTOINCREMENT, MerchName TEXT NOT NULL, Color	TEXT NOT NULL, BuyerName TEXT NOT NULL, Location TEXT NOT NULL, Quantity INTEGER NOT NULL, Date	TEXT NOT NULL)'
        
        # Establish connection to db
        with sqlite3.connect('databases/vikingsdatabase.db') as conn:
            conn.execute(createsold)
            #self.close()
        
        
    def setupWeeks():
        """ This Creates our tables """
        
        createweek1 = 'CREATE TABLE IF NOT EXISTS for_sale_week1 (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Sold INTEGER NOT NULL, Available INTEGER NOT NULL)'
        
        createweek2 = 'CREATE TABLE IF NOT EXISTS for_sale_week2 (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Sold INTEGER NOT NULL, Available INTEGER NOT NULL)'
        
        createweek3 = 'CREATE TABLE IF NOT EXISTS for_sale_week3 (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Sold INTEGER NOT NULL, Available INTEGER NOT NULL)'
        
        """ Table row values """
        
        purchases = [('Hat', 0, 1000),
             ('Shirt', 0, 1000),
             ('Shorts', 0, 1000),
             ('Headband', 0, 1000),
             ('Wristband', 0, 1000),
             ('Football', 0, 1000),
             ('Lanyard', 0, 1000),
             ('Poster', 0, 1000),
             ('Jersey', 0, 1000),
             ]
        
        with sqlite3.connect('databases/vikingsdatabase.db') as conn:
        
            conn.execute(createweek1)
            conn.execute(createweek2)
            conn.execute(createweek3)
            
            conn.executemany('INSERT INTO for_sale_week1 (Name, Sold, Available) VALUES (?,?,?)', purchases)
            conn.executemany('INSERT INTO for_sale_week2 (Name, Sold, Available) VALUES (?,?,?)', purchases)
            conn.executemany('INSERT INTO for_sale_week3 (Name, Sold, Available) VALUES (?,?,?)', purchases)
            #self.close()
    
    def readfromdatabase(week_number):
        
        if week_number == 1:
            with sqlite3.connect('databases/vikingsdatabase.db') as conn:
                conn = conn.cursor()
                conn.execute('SELECT * FROM for_sale_week1')

                return conn.fetchall()
            
        elif week_number == 2:
            with sqlite3.connect('databases/vikingsdatabase.db') as conn:
                conn = conn.cursor()
                conn.execute('SELECT * FROM for_sale_week2')

                return conn.fetchall()
            
        elif week_number == 3:
            with sqlite3.connect('databases/vikingsdatabase.db') as conn:
                conn = conn.cursor()
                conn.execute('SELECT * FROM for_sale_week3')

                return conn.fetchall()
                
    def readsold():
    
        with sqlite3.connect('databases/vikingsdatabase.db') as conn:
                conn = conn.cursor()
                conn.execute('SELECT * FROM sold')

                return conn.fetchall()
        
    def insertBought(merchandise, colorname, custname, locationname, amount, timestamp):
    
        dataEnter = ("INSERT INTO sold (MerchName, Color, BuyerName, Location, Quantity, Date ) VALUES (?, ?, ?, ?, ?, ?);")
        
        with sqlite3.connect('databases/vikingsdatabase.db') as conn:
            conn = conn.cursor()
            conn.execute(dataEnter, (merchandise, colorname, custname, locationname, amount, timestamp))
            
    def deleteOrder(id):
        with sqlite3.connect('databases/vikingsdatabase.db') as conn:
            conn = conn.cursor()
            conn.execute("DELETE FROM sold WHERE ID=?", (id,))
            conn.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='sold'")
    
    def close(self): 
        """Close the SQLite3 database."""

        self.connection.commit()
        self.connection.close()
        self.connected = False