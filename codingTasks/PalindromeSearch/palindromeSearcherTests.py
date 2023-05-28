import unittest
from palindromeSearcher import PalindromeSearcher

class PalindromeSearcherTests(unittest.TestCase):
	def test_search_text_is_set_string_is_returned(self):
		# arrange
		searcher: PalindromeSearcher = PalindromeSearcher()

		# act
		result: str = searcher.search("text")

		# assert
		self.assertTrue(isinstance(result, str))

	def test_search_text_is_empty_string_raise_value_error(self):
		# arrange
		searcher: PalindromeSearcher = PalindromeSearcher()

		# act && assert
		with self.assertRaises(ValueError) as context:
			searcher.search("")

		# assert
		self.assertEqual("text doesn't have value.", str(context.exception))

	def test_search_text_is_none_string_raise_value_error(self):
		# arrange
		searcher: PalindromeSearcher = PalindromeSearcher()

		# act && assert
		with self.assertRaises(ValueError) as context:
			searcher.search(None)

		# assert
		self.assertEqual("text doesn't have value.", str(context.exception))

	def test_search_text_is_whitespace_string_raise_value_error(self):
		# arrange
		searcher: PalindromeSearcher = PalindromeSearcher()

		# act && assert
		with self.assertRaises(ValueError) as context:
			searcher.search("   ")

		# assert
		self.assertEqual("text doesn't have value.", str(context.exception))

	def test_search_txt(self):
		# arrange
		searcher: PalindromeSearcher = PalindromeSearcher()

		# act
		result: str = searcher.search("text")

		# assert
		self.assertTrue(isinstance(result, str))
