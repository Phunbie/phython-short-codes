primary_list = [1]
list = [1]

for i in range(8):
	add_to_list = sum(list)
	if len(list) > 1:
		list.remove(list[0])
	primary_list.append(add_to_list)
	list.append(add_to_list)
print(primary_list)
	
	