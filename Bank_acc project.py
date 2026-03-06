class Bank_acc:
    def __init__(Self,Amount_Deposit,Amount_Withdraw,Check_Balance):
        self.Amount_Deposit = Amount_Deposit
        self.Amountr_Withdraw = Amount_Withdraw
        self.__Check_Balance = Check_Balance #private variable
    def Deposit(self,Amount_Deposit):
        if Amount_Deposit > 0:
            print("Amount Deposited:", Amount_Deposit)
        else:
            print("Invalid deposit amount")
        print("Deposit")
    def Withdraw(self,Amount_Withdraw):
        if Amount_Withdraw > 0:
            print("Amount Withdrawn:", Amount_Withdraw)
        elif Amount_Withdraw > self.__Check_Balance:
            print("Insufficient funds")
        else:
            print("Invalid withdrawal amount")
    def Check_Balance(self,Check_Balance):
        print("Check Balance:", Check_Balance)

a = Bank_acc(200,300,400)
a.Deposit(200) 
a.Withdraw(300)
a.Check_Balance(1200)

