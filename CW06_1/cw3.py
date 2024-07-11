class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance


    def get_value(self):
        return self.balance

    def set_value(self,balance):
        
        self.balance = balance


obj = BankAccount(2,3000)
print(obj.get_value())
obj.set_value(6000)
print(obj.get_value())