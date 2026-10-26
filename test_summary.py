import unittest
from app import generate_summary

class TestSummaryRule(unittest.TestCase):

    def test_long_note_truncates_to_20_words(self):
        # Note with 30 words — extracts only the first 20 words
        words = ["word" + str(i) for i in range(1, 31)]
        note = " ".join(words)
        expected = " ".join(words[:20])
        self.assertEqual(generate_summary(note), expected)

    def test_short_note_retains_all_words(self):
        # Note with fewer than 20 words — returns full note
        note = "Technician replaced the router power supply cleanly."
        self.assertEqual(generate_summary(note), note)

    def test_empty_note(self):
        # Empty string case
        self.assertEqual(generate_summary(""), "")

if __name__ == '__main__':
    unittest.main()