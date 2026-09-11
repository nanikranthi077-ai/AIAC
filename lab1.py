"""Determine whether an entered integer is a palindrome."""


def is_palindrome(number: int) -> bool:
	"""Return True if number reads the same forward and backward."""
	if number < 0:
		return False

	text = str(number)
	return text == text[::-1]


def main() -> None:
	try:
		number = int(input("Enter an integer: ").strip())
	except ValueError:
		print("Please enter a valid integer.")
		return

	if is_palindrome(number):
		print(f"{number} is a palindrome.")
	else:
		print(f"{number} is not a palindrome.")


if __name__ == "__main__":
	main()
