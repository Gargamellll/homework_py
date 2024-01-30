class BankAccount:
    def __init__ (self,account_holder):
        self.account_holder=account_holder
        self.balance=0

    def balance(self,amount):
        self.balance=self.balance + amount
        print (self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount  
            print (self.balance)     

        else:
            print ("Insufficient funds on the card")

costumer=BankAccount("XXX XXXXXXX") 
costumer.()
print(costumer.balance)
# print(costumer.balance(input("enter amount"))) 



