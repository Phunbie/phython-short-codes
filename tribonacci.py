def tribonacci(signature, n):
	if n < 3 and n >0:
		sig = signature[0:n]
	elif n == 0:
		sig = []
	else:
		for i in range(n-3):
			 signature.append(sum(signature[-3: ]))
		sig = signature
	return sig
			
signature =[2,1,3]
print(tribonacci(signature,1))
	