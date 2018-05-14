from unittest import TestCase
from unittest.mock import patch, Mock
import main
from main import changeprofiles

class TestProfiles(TestCase):

    test_db_url = 'test_profiles.db'
    
    def setUp(self):
        profiles.db_url = self.test_profiles_db_url
        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.test_profiles_db_url)
        conn.execute('DELETE FROM test_profiles')
        conn.commit()
        conn.close()

    def test_change_profiles(self):
        changeprofiles.
    
