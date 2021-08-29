def return_nx_alp(x):
	import string
	alpha = string.ascii_lowercase
	if x in alpha[:-1]:
		n = alpha.index(x)+1
		return alpha[n]
	return alpha[0]

def replace_with(word):
	while len(word) != len(set(word)):
		for i in word:
			if word.count(i) > 1:
				#word = word.replace(i,return_nx_alp(i),1)
				word =list(word)
				word.remove(i)
				word=''.join(word)
				word = word.replace(i,return_nx_alp(i),1)
	return word
	
p = 'aabbccdd'
print(replace_with(p))
	
	