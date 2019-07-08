
# unittest uses camelCase, hence the mixed snake_- and camelCase
import unittest

from project import app

class ProjectTests(unittest.TestCase):
    #execute prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    #execute after each test_client
    def tearDown(self):
        pass

    # helper methods

    #tests
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'HOME page', response.data)
        self.assertIn(b'topic 1', response.data)
        self.assertIn(b'topic 2', response.data)
        self.assertIn(b'topic 3', response.data)

if __name__ == '__main__':
    unittest.main()
