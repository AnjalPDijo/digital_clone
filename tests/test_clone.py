import os
import unittest
from src.main import DigitalClone

class TestDigitalClone(unittest.TestCase):
    def setUp(self):
        self.clone = DigitalClone(data_file='tests/test_data.json')

    def tearDown(self):
        os.remove('tests/test_data.json')

    def test_add_like(self):
        self.clone.add_like("Ice Cream")
        self.assertIn("ice cream", self.clone.get_data()['likes'])

    def test_add_dislike(self):
        self.clone.add_dislike("Broccoli")
        self.assertIn("broccoli", self.clone.get_data()['dislikes'])

    def test_set_behavior(self):
        self.clone.set_behavior("Jogging", "Goes for a jog every morning")
        self.assertEqual(self.clone.describe_behavior("Jogging"), "Goes for a jog every morning")

    def test_remove_like(self):
        self.clone.add_like("Ice Cream")
        self.clone.remove_like("Ice Cream")
        self.assertNotIn("ice cream", self.clone.get_data()['likes'])

    def test_remove_dislike(self):
        self.clone.add_dislike("Broccoli")
        self.clone.remove_dislike("Broccoli")
        self.assertNotIn("broccoli", self.clone.get_data()['dislikes'])

    def test_update_behavior(self):
        self.clone.set_behavior("Jogging", "Goes for a jog every morning")
        self.clone.update_behavior("Jogging", "Jogging every evening")
        self.assertEqual(self.clone.describe_behavior("Jogging"), "Jogging every evening")

if __name__ == '__main__':
    unittest.main()
