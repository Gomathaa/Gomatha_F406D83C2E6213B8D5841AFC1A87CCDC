class Bank_Account:
   def _init(self):
     self.balance=0
     print("Hello!!! Welcome to the deposit& Withdrawal Machine")
   def deposit(self):
     amount=float(input("Enter the amount to be Deposited:" ))
     self.balance += amount
     print("\n Amount Deposited:",amount)
   def withdraw (self):
      amount = float(input("Enter amount to be withdrawan:"))
      if self.balance>=amount:
        self.balance-=amount
        print("\nYou withdraw:",amount)
      else:
        print("\n Insufficent balance")
   def display(self):
      print("\n Net Available Balance=", self.balance)
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()



