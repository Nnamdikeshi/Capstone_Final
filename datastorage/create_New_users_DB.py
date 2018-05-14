import sqlite3


class CreateDB(object):    
    """DB initializes and manipulates SQLite3 databases."""
    
    def setup(name):
        NAME = name
        Username = name
        AGE = ''
        EMAIL = ''
        FAVPLAYER = ''