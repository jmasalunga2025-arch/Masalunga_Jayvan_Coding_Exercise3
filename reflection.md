Reflection

Phase 1: Conceptual Check & Code Diagnosis

1. Conceptual Distinction

Encapsulation is when we keep the data and functions together inside a class and control how the data can be accessed. Abstraction is when we hide the complicated parts of a program and only show the important parts to the user.

A good example is an ATM. Encapsulation keeps the account balance and other information inside the bank system. Abstraction is when we can just choose deposit, withdraw, or check balance without knowing how the bank system works in the background.

An attribute with one underscore like `_balance` is called non-public because it is only a naming convention in Python. It tells other programmers that the variable is supposed to be used inside the class. However, Python does not completely stop us from accessing it.

When we use two underscores like `__pin`, Python uses name mangling. For example, if the class is called `ATM`, `__pin` becomes `_ATM__pin` internally. This makes it harder to access directly from outside the class.

2. Code Diagnosis

1. The `self` parameter is used incorrectly. The `__init__` method uses `wallet` instead of `self`, and `add_funds()` does not have `self`.

2. The naming is not following the usual Python convention. `wallet.Owner` should normally be something like `wallet.owner` because instance attributes usually use lowercase names.

3. The `balance` function should use `@property` and `@balance.setter`. This makes it easier to get and change the balance while still checking if the new value is valid.

Phase 4: Final Reflection Questions

1. What error occurred when trying to access `atm.__pin` directly? Why does Python behave this way?

I got an `AttributeError` when I tried to access `atm.__pin` directly. This happens because Python changes the name of attributes that start with two underscores. In the ATM class, `__pin` is changed internally to `_ATM__pin`. This is called name mangling.

2. How did using `@property` allow you to change internal data structures or add validation without altering the public API for the caller?

Using `@property` allowed me to access the balance using `account.balance` even though the actual variable is `_balance`. I can also put validation in the setter. For example, I can prevent the balance from becoming negative without changing how the user accesses the balance.

3. How did the ATM class demonstrate abstraction relative to the underlying BankAccount logic?

The ATM showed abstraction because it gave simple methods like `check_balance()`, `perform_deposit()`, and `perform_withdrawal()`. The user does not need to know all the code inside the BankAccount class. The ATM handles the process and calls the needed functions in the background.
