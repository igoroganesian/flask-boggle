from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            # test that you're getting a template
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Homepage Template', html)


    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            resp = client.post('/api/new-game')
            data = resp.get_json()

            self.assertIsInstance(data["board"], list)
            self.assertTrue(type(data["board"][0]) == list)
            self.assertIsInstance(data["gameId"], str)
            self.assertTrue(games)

            # self.assertIsInstance(games)

            print(data["gameId"])
            print("RESPONSE", data)

            # breakpoint()

            # write a test for this route


    def test_score_word(self):

        # with app.test_client() as client:
        #     resp = client.post('/api/new-game',json={'gameId': 'blue'})
        #     data = resp.get_json()

        with self.client as client:
            resp = client.post('/api/new-game')
            data = resp.get_json()

            resp2 = client.post('/api/score-word', json={"gameId": data["gameId"], "word": "test"})


            self.assertEqual({'message': 'blue is best!'}, data)
