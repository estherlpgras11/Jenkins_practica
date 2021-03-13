from unittest import TestCase
from mock import Mock, patch
from app import app


class BasicTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
    # executed after each test
    def tearDown(self):
        pass

    def test_config(self):
        self.assertEqual(app.debug, False)

    def _test_items(self, mock_sql, fetch_data, app_response):
        mock_fetchall = Mock()
        mock_fetchall.fetchall.return_value = fetch_data
        mock_cursor = Mock()
        mock_cursor.cursor.return_value = mock_fetchall
        mock_sql.connect.return_value = mock_cursor
        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)
        expected_response = '{"error":false,"result":%s}\n' % app_response
        self.assertEqual(response.data, expected_response.encode('ascii'))

    @patch('app.mysql')
    def test_items_empty(self, mock_sql):
        self._test_items(mock_sql, None, 'null')

    @patch('app.mysql')
    def test_items_with_record(self, mock_sql):
        image_url = 'https://1.bp.blogspot.com/_e5rLQEpqOEM/SLiHfcEx-5I/AAAAAAAAISc/dxNkUCAE2UA/s1600-h/acme1.jpg'
        fetch_data = [['yunke', 'yunke para destruir', image_url]]
        app_response= '[["yunke","yunke para destruir","%s"]]' % image_url
        self._test_items(mock_sql, fetch_data, app_response)
