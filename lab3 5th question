def main():
	try:
		number = int(input("Enter a positive integer: ").strip())
		if number <= 0:
			print("Invalid input")
			return
	except (ValueError, EOFError):
		print("Invalid input")
		return

	divisor_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)
	print("Perfect Number" if divisor_sum == number else "Not a Perfect Number")


if __name__ == "__main__":
	main()

