class PalindromeSearcher:
	def search(self, text: str) -> str:
		if not text or text.isspace():
			raise ValueError("text doesn't have value.")

		for i in range(0, len(text)):
			self.__search(text, i)

		return ""

	def __search(self, text: str, start_index: int) -> str:
		result: str = ""

		for i in range(start_index, len(text)):
			reverse_index: int = len(text) - i - 1

			if text[i] == text[reverse_index]:
				result = result + text[i]

		return result