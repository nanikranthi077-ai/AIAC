def is_armstrong(number):
	"""Return True if number is an Armstrong number."""
	digits = str(number)
	power = len(digits)
	return number >= 0 and sum(int(digit) ** power for digit in digits) == number


for number in (153, 370, 123):
	result = "Armstrong" if is_armstrong(number) else "Not Armstrong"
	print(f"{number}  {result}")
