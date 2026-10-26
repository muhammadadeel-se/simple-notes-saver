import unittest
from app import generate_summary

class TestSummaryRule(unittest.TestCase):

    def test_more_than_20_words(self):
        # Note with 30 words — should extract only first 20 words
        words = ["word" + str(i) for i in range(1, 31)]
        note = " ".join(words)
        expected = " ".join(words[:20])
        self.assertEqual(generate_summary(note), expected)

    def test_fewer_than_20_words(self):
        # Note with less than 20 words — should return all words
        note = "Technician replaced the main router power supply cleanly."
        self.assertEqual(generate_summary(note), note)

    def test_empty_string(self):
        # Empty string case
        self.assertEqual(generate_summary(""), "")

if __name__ == '__main__':
    unittest.main()