class PalindromeSearcher:
	def search(self, text: str) -> str:
		if not text or text.isspace():
			raise ValueError("text doesn't have value.")


		result: str = self.__search(text, 0)

		return ""

	def __search(self, text: str, start_index: int) -> str:
		palindrome: str = ""

		end_index_decrement: int = 0
		for index in range(start_index, len(text)):
			end_index = len(text) - end_index_decrement - 1

			start_char: str = text[index]
			end_char: str = text[end_index]
			if start_char == end_char:
				palindrome = palindrome + text[index]
			else:
				new_palindrome: str = self.__search(text, index)

				if len(new_palindrome) > len(palindrome):
					palindrome = new_palindrome

			end_index_decrement += 1

		return palindrome

