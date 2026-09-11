"""Classify an entered integer as prime, composite, or neither."""

from math import isqrt


def classify_number(number: int) -> str:
	"""Return the classification of *number*."""
	if number < 2:
		return "neither"
	if number in (2, 3):
		return "prime"
	if number % 2 == 0 or number % 3 == 0:
		return "composite"

	# Check only possible factors of the form 6k - 1 or 6k + 1.
	for factor in range(5, isqrt(number) + 1, 6):
		if number % factor == 0 or number % (factor + 2) == 0:
			return "composite"
	return "prime"


def main() -> None:
	value = input("Enter an integer: ").strip()
	try:
		number = int(value)
	except ValueError:
		print("Invalid input: please enter a whole integer.")
		return

	print(f"{number} is {classify_number(number)}.")


if __name__ == "__main__":
	main()
