# test_hello.py
import unittest
from hello import hello_world

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
