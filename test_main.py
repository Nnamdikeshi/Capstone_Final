from unittest import TestCase
from unittest.mock import patch, Mock
import main
from main import login

class TestMain(TestCase):

    test_db_url = 'test_quit.db'

    """
    Before running this test, create test_quit.db
    Create expected user table
    create table user (username text, password text);
    """

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        # Overwrite the mileage
        quit.db_url = self.test_db_url
        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('DELETE FROM quit')
        conn.commit()
        conn.close()


    def test_add_new_user(self):
        login.add_user('Test', 'thisworks')
        expected = { 'Test': 'thisworks' }
        self.compare_db_to_expected(expected)

        mileage.add_miles('Admin', '123456')
        expected['Admin'] = '123456'
        self.compare_db_to_expected(expected)
    