class bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        a = input()
        self.deposit = int(a)
        self.balance += self.deposit

    def withdraw(self, withdraw):
        self.withdraw = withdraw
        if self.balance >= self.withdraw:
            self.balance = self.balance - self.withdraw
        else:
            print("Sorry, u dont have any money")
    def account(self):
        return self.owner, self.balance


name = input()
money = input()
human = bank(str(name), int(money))
print(human.account())
human.deposit()
human.withdraw(200)
print(human.account())