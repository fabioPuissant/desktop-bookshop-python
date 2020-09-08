class Account:
    _balance: int = 0
    _type: str = None

    def __init__(self, filepath, type='base-account'):
        self._type = type

        with open(filepath, 'r') as file:
            self._balance = int(file.read())

    def withdraw(self, amount):
        before = self._balance
        self._balance = self._balance - amount if self._balance - amount >= 0 else self._balance
        if self._balance == before:
            raise Exception("Insufficient funds")

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def get_type(self):
        return self._balance

    def commit(self):
        with open('balance.txt', 'w') as file:
            file.write(str(self._balance))


class Checking(Account):
    _fee: int = 0

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath, 'checking-account')
        self._fee = fee

    def transfer(self, amount):
        self._balance = self._balance - amount - self._fee\
            if self._balance - amount - self._fee > 0 \
            else 0

    def get_type(self):
        return 'checking-account'


account = Account('balance.txt')
print(account.get_balance())
account.withdraw(5)
print(account.get_balance())
account.deposit(10)
print(account.get_balance())
account.commit()
account = Account('balance.txt')
print(account.get_balance())

# Working with checking account
checkin_account = Checking('balance.txt', 4)
print(checkin_account.get_balance())
print(checkin_account.get_type())
checkin_account.deposit(100)
checkin_account.transfer(200)
print(checkin_account.get_balance())
checkin_account.commit()
