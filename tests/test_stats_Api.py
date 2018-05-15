from unittest import TestCase
from unittest.mock import patch, Mock
import stats_Api
from stats_Api import find

class Test_stats_API(TestCase):

    @mock.patch('requests.get', autospec=True
    def test_get_example_passing(mocked_get):
       mocked_form_obj = 2017 + '-regular'
       mocked_req_obj = mock.Mock()
       mocked_req_obj.status_code = 200
       mocked_get.return_value = mocked_req_obj
       assert(get_example())

       mocked_get.assert_called()
       mocked_get.assert_called_with('https://api.mysportsfeeds.com/v1.2/pull/nfl/%s-regular/cumulative_player_stats.json' % mocked_form_obj)
        
    def test_find_not_Api_credentials(self):
        mocked_req_obj.status_code = 400
        mocked_get.return_value = mocked_req_obj
        
        username = 'Nnamdikeshi'
        password = 'thismightnotwork'
        mocked_get.assert_called()
        mocked_get.assert_called_with  requests.get(
                url = 'https://api.mysportsfeeds.com/v1.2/pull/nfl/%s-regular/cumulative_player_stats.json' % sp,
                headers = {"Authorization": "Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
                }
            )
        