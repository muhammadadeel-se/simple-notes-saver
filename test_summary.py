import unittest
from app import generate_summary

class TestSummaryRule(unittest.TestCase):

    def test_first_complete_sentence(self):
        # Case 1: Multiple sentences — should extract only the first complete sentence
        note = "Technician replaced the router power supply. All lights are green now."
        expected = "Technician replaced the router power supply."
        self.assertEqual(generate_summary(note), expected)

    def test_truncation_without_punctuation(self):
        # Case 2: Long note with no punctuation — should truncate to 120 chars
        note = "A" * 150
        expected = ("A" * 120) + "..."
        self.assertEqual(generate_summary(note), expected)

    def test_short_note_without_punctuation(self):
        # Case 3: Short note without sentence ending — should return as-is
        note = "System maintenance ongoing"
        expected = "System maintenance ongoing"
        self.assertEqual(generate_summary(note), expected)

if __name__ == '__main__':
    unittest.main()