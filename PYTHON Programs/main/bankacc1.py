class BankAccount:
    def __init__(self, name, account_number, account_type, balance=0):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "successful. New balance is", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "successful. New balance is", self.balance)
        else:
            print("Insufficient balance.")

    def display_details(self):
        print("Account details:")
        print("Name:", self.name)
        print("Account number:", self.account_number)
        print("Account type:", self.account_type)
        print("Balance:", self.balance)

# Example usage
account = BankAccount("John Doe", "1234567890", "Savings")
account.display_details()  # Account details: Name: John Doe, Account number: 1234567890, Account type: Savings, Balance: 0
account.deposit(1000)  # Deposit of 1000 successful. New balance is 1000
account.withdraw(500)  # Withdrawal of 500 successful. New balance is 500
account.display_details()  # Account details: Name: John Doe, Account number: 1234567890, Account type: Savings, Balance: 500

