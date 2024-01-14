class BalanceException(Exception):
    pass



class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance: .2f}")

    def getbalance(self):
        print(f"\nAccount'{self.name}' balance = ${self.balance: .2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\n Deposit Complete.")
        self.getbalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account'{self.name}' only has balance of ${self.balance:.2f} "
            )
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawn Complete.")
            self.getbalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")

    def transfer(self,amount,account):
        try:
            print('\n*****************\n\n Beginning Transfer...🚀🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!!✅✅\n\n*********')
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")

class InterestRewardedAcc(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.04)
        print("\n Deposit Complete")
        self.getbalance()

class SavingsAcc(InterestRewardedAcc):
    def __init__(self,initialAmount,acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5 

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount +self.fee)
            print("\nWithdraw Complete.")
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error} ")

