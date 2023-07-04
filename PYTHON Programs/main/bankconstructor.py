class BankAccount:
    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "successful.")
        self.display_balance()

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal of", amount, "successful.")
            self.display_balance()

    def display_balance(self):
        print("Account balance:", self.balance)

# Create a BankAccount object and test the deposit and withdrawal methods
bank_account = BankAccount("123456789", "John Doe", "Savings", 5000)
bank_account.display_balance()
bank_account.deposit(2000)
bank_account.withdraw(1000)

