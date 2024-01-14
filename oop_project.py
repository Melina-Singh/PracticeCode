from bank_accounts import *

Mele = BankAccount(1000, "Mele")
Bela = BankAccount(5000, "Bela")

Bela.getbalance()
Mele.getbalance()

Mele.deposit(6000)

Bela.withdraw(1000)

Mele.transfer(40000, Bela)
Mele.transfer(1000, Bela)

jim = InterestRewardedAcc(1000, "jim")

jim.getbalance()
jim.deposit(100) 
jim.transfer(100,Bela) 


Bllaze = SavingsAcc(1000, "Bllaze")

Bllaze.getbalance()

Bllaze.deposit(100)
Bllaze.transfer(1500, Bela)
