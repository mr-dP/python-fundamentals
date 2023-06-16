# Databricks notebook source
class Account:
    def __init__(self, account_number, account_type, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited ${amount}")
            print(f"New balance is: ${self.balance}")
        else:
            print(f"{amount} is an invalid number")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrawl: ${amount}")
            print(f"New Balance: ${self.balance}")
        else:
            if amount < 0:
                print(f"{amount} is an invalid number")
            else:
                print("Insufficient funds.")
                print(f"Current balance is ${self.balance}")

# COMMAND ----------

my_account = Account("123-890", "savings", 1_000.00)

# COMMAND ----------

my_account.account_number

# COMMAND ----------

my_account.account_type

# COMMAND ----------

my_account.balance

# COMMAND ----------

my_account.deposit(100)

# COMMAND ----------

my_account.withdraw(600)

# COMMAND ----------

my_account.withdraw(10_000)

# COMMAND ----------



# COMMAND ----------

10 + 15

# COMMAND ----------

(10).__add__(45)

# COMMAND ----------

0.125

# COMMAND ----------

(0.125).as_integer_ratio()

# Out[12]: (1, 8)

# COMMAND ----------

# Floats do not have exact representations as binary fractions becasuse we have a finite amount of memory. But that does mean that that representation is finite in the computer. And the the representation is finite in the computer, it is a number that can be expressed always as a ratio of 2 integers.

# COMMAND ----------

(0.1).as_integer_ratio()

# Out[14]: (3602879701896397, 36028797018963968)

# COMMAND ----------


