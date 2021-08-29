class Account:
	def __init__(self,name):
		self.name = name
		self.balance = 0
	def my_bal(self):
		return self.balance
	def deposit(self,depo):
		self.balance = self.balance + depo
		return depo
	def withdrawl(self,wit):
		self.balance = self.balance - wit
		return wit
Acc = Account('Funbi')
print(Acc.balance)