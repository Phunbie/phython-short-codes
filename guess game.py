import random
score = 0
loop = 1
print('Guessing number from 1 to 10')
print('enter  any other character to stop')
num = random.randint(1,10)
for i in range(3):
	
	while loop == 1:
		print('you have ',3-i,' lives left')
		enter = int(input('Gess a number from 1 to 10  '))
		if num == enter:
			score += 10
			print('your score is ',score)
			loop = 1
		else:
			print ('Wrong guess')
			break
import time
print('Game over')
time.sleep(2)
print(20*'*')
time.sleep(2)
print('your total score is ',score)