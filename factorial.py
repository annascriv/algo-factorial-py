def factorial(num):
	product = 1

	while num>0:
		product=product*num
		num=num-1
	return product

print(factorial(5))