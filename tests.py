import unittest
import hello as tested_app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get(self):
        r = self.app.get('/')
        self.assertEqual(r.data.decode('utf-8'), 'У меня получилось!')

    def test_post(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)

    def test_get_second(self):
        r = self.app.get('/seconds')
        self.assertEqual(r.data.decode('utf-8'), 'Здесь так же все работает!')

    def test_post_second(self):
        r = self.app.post('/seconds')
        self.assertEqual(r.status_code, 405)


if __name__ == '__main__':
    unittest.main()