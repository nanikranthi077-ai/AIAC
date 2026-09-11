def main():
	while True:
		value = input("Enter an integer: ").strip()
		try:
			number = int(value)
			# Reject inputs such as 3.0 or 1e2, which are not integer literals.
			if str(number) != value and value not in {f"+{number}", f"-{abs(number)}"}:
				raise ValueError
			break
		except ValueError:
			print("Invalid input. Please enter a whole number.")

	print("Even" if number % 2 == 0 else "Odd")


if __name__ == "__main__":
	main()
