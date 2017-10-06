import unittest
from unique_chars import unique_characters

class UniqueCharacterTestCase(unittest.TestCase):
    def test_unique(self):
        self.assertTrue(unique_characters('alma'))

    def test_unique_characters_empty_string(self):
        self.assertFalse(unique_characters(''))

    def test_unique_characters_None(self):
        self.assertFalse(unique_characters())


if __name__ == '__main__':
    unittest.main()