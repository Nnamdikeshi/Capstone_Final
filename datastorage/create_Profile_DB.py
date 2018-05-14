import sqlite3


class CreateDB(object):    
    """DB initializes and manipulates SQLite3 databases."""
    # Set up our DB
    def setup(name):
        # Some default variables
        NAME = name
        Username = name
        AGE = ''
        EMAIL = ''
        FAVPLAYER = ''

        createsqlite = 'CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL ,name TEXT NOT NULL,age INT NOT NULL, email TEXT NOT NULL, favplayer TEXT NOT NULL)'.format(Username, NAME, AGE, EMAIL, FAVPLAYER)
        
        # Establish connection to db
        with sqlite3.connect('databases/profiles.db') as conn:
            conn.execute(createsqlite)
            self.close()
            
    # Close function (Not implemented yet)
    def close(self): 
        """Close the SQLite3 database."""

        self.connection.commit()
        self.connection.close()
        self.connected = False
        
    # Function for updating the table
    def update(name, age, email, favplayer):
        """Update the table users where username"""
        
        updates = ('UPDATE users SET name = ?, age = ?, email = ?, favplayer = ? WHERE username = ?;')
          
        with sqlite3.connect('databases/profiles.db') as conn:
            conn = conn.cursor()
            conn.execute(updates, (name, age, email, favplayer, name))
        
        # Return our data
        return name, age, email, favplayer
        
    # Fucntion to excecute show our db data            
    def showAll(pname):
        """Show our row where username"""
        
        pn = pname
        with sqlite3.connect('databases/profiles.db') as conn:
            conn = conn.cursor()
            conn.execute('SELECT * FROM users WHERE username =?', (pn,))
            # Return our data
            return conn.fetchall()
    
    