import sqlite3
from unittest import TestCase
from datastorage.create_Profile_DB import CreateDB

class TestCreateProfileDB(TestCase):
    test_db_url = 'test_Profile.db'
    
    def setUp(self):
        # Overwrite the mileage
        mileage.db_url = self.test_db_url
        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('DELETE FROM users')
        conn.commit()
        conn.close()
          
        
    def compare_db_to_expected(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM users').fetchall()

        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])

        conn.close()