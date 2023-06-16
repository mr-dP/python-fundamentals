# Databricks notebook source
#               =     ->   Assignment Operator

# COMMAND ----------

a = 100

# COMMAND ----------

a

# COMMAND ----------

a + 11

# COMMAND ----------

b = a + 90

# COMMAND ----------

b

# COMMAND ----------

10 = 10

# SyntaxError: cannot assign to literal (, line 1)

# COMMAND ----------

a = 2.14

# COMMAND ----------

a

# COMMAND ----------

test = 100
test_1 = 1001
_test_1_ = 10
__test__ = 909
TEST = 11011

# COMMAND ----------

test, TEST

# SyntaxError: cannot assign to literal (, line 1)

# COMMAND ----------

1_test = 1001

# SyntaxError: invalid decimal literal (, line 1)

# COMMAND ----------

if = 101

# SyntaxError: invalid syntax (, line 1)

# COMMAND ----------

a = float(10)

# COMMAND ----------

a

# COMMAND ----------

float = 105.09

# COMMAND ----------

float

# COMMAND ----------

a = float(101)

# TypeError: 'float' object is not callable

# COMMAND ----------

del float

# COMMAND ----------

a = float(101)
a

# COMMAND ----------

current_balance = 100.05

# COMMAND ----------

currentBalance = 109.09  # Not recommneded

# COMMAND ----------

currentBalance

# COMMAND ----------

current_balance = 100.90        # meaningful
cb = 110.80                     # NOT meaningful

# COMMAND ----------

x = 100
y = 0.1
z = 10

r = x * ((1 + y / 12) ** (z * 12))

print(r)

# COMMAND ----------

principal = 100
apr = 0.1
year = 10

future_value = principal * ((1 + apr / 12) ** (year * 12))

print(future_value)

# COMMAND ----------


