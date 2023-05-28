class PalindromeSearcher:
	def search(self, text: str) -> str:
		if not text or text.isspace():
			raise ValueError("text doesn't have value.")

		return ""