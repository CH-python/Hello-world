import unittest
from testmessage import TestMessage

class MyTestCase(unittest.TestCase):
    def test_default(self):
        text = TestMessage()
        self.assertEqual(text.message, 'Hello world!')
        print(text.message)

if __name__ == '__main__':
    unittest.main()
