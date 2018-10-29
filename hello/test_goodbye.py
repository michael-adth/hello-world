import unittest

from hello import hello


class TestGoodbye(unittest.TestCase):
    """sample test"""

    def test_moon(self):
        """sample test"""
        self.assertEqual(hello('world'), 'hello world')

    def test_sun(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'world'), u'hello world')

    def test_mars(self):
        """sample test with failure"""
        self.assertEqual(2+2, 5)

    def test_mars(self):
        """sample test with failure"""
        syntax error code
        self.assertEqual(2+2, 5)
    
    