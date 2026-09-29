class BankAccount:
    def __init__(self, account_holder, initial_deposit=0.0):
        self.account_holder = account_holder

        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        self._balance = initial_deposit
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")

        self._balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self._balance += amount
        self._transactions.append(f"Deposited: {amount:.2f}")

        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")

        if self._balance < amount:
            raise ValueError("Insufficient balance.")

        self._balance -= amount
        self._transactions.append(f"Withdrawn: {amount:.2f}")

        return amount

    def get_transaction_history(self):
        return self._transactions.copy()


class ATM:
    def __init__(self, bank_account):
        if not isinstance(bank_account, BankAccount):
            raise TypeError("bank_account must be a BankAccount.")

        self._account = bank_account
        self.__pin = "1234"
        self._is_authenticated = False

    def authenticate(self, entered_pin):
        if entered_pin == self.__pin:
            self._is_authenticated = True
            return True

        return False

    def check_balance(self):
        if not self._is_authenticated:
            raise PermissionError("Please authenticate first.")

        return self._account.balance

    def perform_deposit(self, amount):
        if not self._is_authenticated:
            print("Please authenticate first.")
            return None

        try:
            new_balance = self._account.deposit(amount)
            print(f"Deposit successful. New balance: {new_balance:.2f}")
            return new_balance

        except ValueError as error:
            print("Deposit error:", error)
            return None

    def perform_withdrawal(self, amount):
        if not self._is_authenticated:
            print("Please authenticate first.")
            return None

        try:
            withdrawn_amount = self._account.withdraw(amount)
            print(f"Withdrawal successful: {withdrawn_amount:.2f}")
            print(f"Remaining balance: {self._account.balance:.2f}")
            return withdrawn_amount

        except ValueError as error:
            print("Withdrawal error:", error)
            return None

    def print_mini_statement(self):
        if not self._is_authenticated:
            print("Please authenticate first.")
            return

        transactions = self._account.get_transaction_history()

        print("\n--- MINI STATEMENT ---")

        if not transactions:
            print("No transactions yet.")
        else:
            for transaction in transactions[-3:]:
                print(transaction)

        print(f"Current Balance: {self._account.balance:.2f}")


if __name__ == "__main__":
    account = BankAccount("Jayvan", 1000.0)

    print("Account Holder:", account.account_holder)
    print("Balance:", account.balance)

    # Test invalid balance
    try:
        account.balance = -500
    except ValueError as error:
        print("Invalid balance:", error)

    # Create ATM
    atm = ATM(account)

    # Test direct access to private PIN
    try:
        print("PIN:", atm.__pin)
    except AttributeError as error:
        print("PIN access error:", error)

    # Test authentication
    print("\nWrong PIN:", atm.authenticate("9999"))
    print("Correct PIN:", atm.authenticate("1234"))

    # Check balance
    print("ATM Balance:", atm.check_balance())

    # Deposit
    print("After Deposit:", atm.perform_deposit(500))

    # Withdrawal
    print("Withdrawn:", atm.perform_withdrawal(200))

    # Test invalid withdrawal
    atm.perform_withdrawal(5000)

    # Mini statement
    atm.print_mini_statement()