"""Tests for the correct word and line counts from wordcount.count.

Words are separated by any whitespace. A trailing newline ends the last line
and does not add another one.
"""

import unittest

from wordcount import count


class WordSplitTests(unittest.TestCase):
    def test_repeated_spaces_do_not_create_empty_words(self):
        self.assertEqual(count("one  two   three")["words"], 3)

    def test_tab_separates_words(self):
        self.assertEqual(count("one\ttwo")["words"], 2)

    def test_newline_separates_words(self):
        self.assertEqual(count("one\ntwo")["words"], 2)

    def test_mixed_whitespace_is_one_separator(self):
        self.assertEqual(count("  one \t two \n three  ")["words"], 3)


class LineCountTests(unittest.TestCase):
    def test_line_without_trailing_newline(self):
        self.assertEqual(count("hello")["lines"], 1)

    def test_trailing_newline_is_not_an_extra_line(self):
        self.assertEqual(count("hello\n")["lines"], 1)

    def test_several_lines_with_trailing_newline(self):
        self.assertEqual(count("one\ntwo\nthree\n")["lines"], 3)

    def test_several_lines_without_trailing_newline(self):
        self.assertEqual(count("one\ntwo\nthree")["lines"], 3)

    def test_blank_line_counts_and_trailing_newline_does_not(self):
        self.assertEqual(count("one\n\ntwo\n")["lines"], 3)


class CombinedCountTests(unittest.TestCase):
    def test_double_space_and_trailing_newline(self):
        result = count("one  two\n")
        self.assertEqual(result["words"], 2)
        self.assertEqual(result["lines"], 1)


if __name__ == "__main__":
    unittest.main()
