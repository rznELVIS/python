class PalindromeSearcher:
	def search(self, text: str) -> str:
		if not text or text.isspace():
			raise ValueError("text doesn't have value.")

		for i in range(0, len(text)):
			result: str = self.__search(text, i)

		return ""

	def __search(self, text: str, start_index: int) -> str:
		result: str = ""

		for index in range(start_index, len(text)):
			result = result + text[index]

		return result

