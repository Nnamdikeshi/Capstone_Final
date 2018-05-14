from unittest import TestCase
from unittest.mock import patch, Mock
import stats_Api
from stats_Api import

class Test_stats_API(TestCase):

    def setUp(self):
        url = 'https://api.mysportsfeeds.com/v1.2/pull/nfl/2017-regular/cumulative_player_stats.json',
        
    def test_find_not_Api_credentials(self):
        
        