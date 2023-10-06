def factorial(num):
	product = 1
	if num == 0:
		return 1
	else:
		while num>0:
			product=product*num
			num=num-1
	return product

print(factorial(0))