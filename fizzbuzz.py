def fizzbuzz(return_num): 
	list = [0]*100
	for i in range(1,101):

		if i % 3 == 0 and i % 5 == 0:
			list[i-1] = "FizzBuzz" 
		
		elif (i)%3 == 0: 
			list[i-1] = "Fizz"

		elif i % 5 == 0: 
			list[i-1] = "Buzz"

		else:
			list[i-1] = i

	print(list)

	if return_num == None:
		return list
	else: 
		return list[return_num-1]

fizzbuzz(None)