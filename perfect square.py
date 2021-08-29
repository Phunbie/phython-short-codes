def is_square(n):
		if n < 0:
			num1=False
		else:
			import math
			num1 = n**0.5
			num2 = math.floor(num1)
			if num1 == num2:
				num1 = True
			else:
				num1 = False
		return num1
		
print(is_square(5))