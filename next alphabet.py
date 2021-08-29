def return_nx_alp(x):
	import string
	alpha = string.ascii_lowercase
	if x in alpha[:-1]:
		n = alpha.index(x)+1
		return alpha[n]
	return alpha[0]
print(return_nx_alp('z'))


def pairIndex(word):
										if n_word.count(j) >1:
										jj= word.rfind(j)
										pairIndex.append(jj)

#def replace_with(word):
	#	n_word = list(word)
	#	pairIndex = []
	#	for i,j in enumerate(n_word):
								
								#	if n_word.count(j) >1:
									#	jj= word.rfind(j)
									#	pairIndex.append(jj)
									#	n_word[i] = return_nx_alp(j)
							#	pairIndex.reverse()
						#		for i in pairIndex:
							#n_word.remove(word[i])
		#word = ''.join(n_word)
	#	return n_word
							
	
def pairIndex(word):
    neord = word[:]
    unique= []
    for i in word:
        for j in word:
            if i == j and word.count(j) > 1 and j not in unique:
               unique.append(j)
               rem = word.count(j)//2
               for i in range(rem):
               	neord.replace(j,return_nx_alp(j))
               	neord.remove(j)
     return neord
word = pairIndex(word)				
	
p = 'aabbccddd'
replace_with(p)
	
	