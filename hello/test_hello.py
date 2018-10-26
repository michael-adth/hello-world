"""sample test"""
import unittest

from hello import hello


class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello('world'), 'hello world')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'world'), u'hello world')

    def test_world_Faile(self):
        """sample test with failure"""
        self.assertEqual(2+2, 3)
    
    def test_world_Faile_Whale(self):
        """sample test with failure"""
        self.assertEqual(2+2, 5)


    def test_world_Faile_Whale2(self):
        """sample test with failure"""
        self.assertEqual(2+2, 5)

    def test_world_Faile_Whale3(self):
        """sample test with failure"""
        self.assertEqual(2+2, 5)

    def test_world_Faile_Whale4(self):
        """sample test with failure"""
        self.assertEqual(2+2, 5)