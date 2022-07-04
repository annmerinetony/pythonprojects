class Bank:
    bankname='SBI'
    def account(self,name,acnum):
        self.name=name
        self.acnum=acnum
        self.minbalance=2000
        self.balance=self.minbalance
    def deposit(self,cash):
        self.cash=cash
        self.balance=self.balance+self.cash
        print('your',Bank.bankname,'acc credited',self.cash)
        print('balance is',self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print('insufficient')
        else:
            self.balance=self.balance-self.amount
            print('account debited with',self.amount)

            print('balance is',self.balance)
x=Bank()
x.account('ann',34567)
x.deposit(5000)
x.withdraw(6000)
