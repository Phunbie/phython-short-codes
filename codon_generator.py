codon_list = []
nucleotides = ['A','T','G','C']
for i in nucleotides:
	for j in nucleotides:
		for k in nucleotides:
			codon = i + j + k
			codon_list.append(codon)
print(codon_list)