# Databricks notebook source
not True

# COMMAND ----------

not False

# COMMAND ----------

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# COMMAND ----------

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# COMMAND ----------

balance = 1000.00
withdrawal = 50.00
withdrawal_limit = 500.00

# COMMAND ----------

(withdrawal < withdrawal_limit) and (withdrawal <= balance)
# Out[6]: True

# COMMAND ----------

balance = 1000.00
withdrawal = 1200.00
withdrawal_limit = 1500.00

# COMMAND ----------

(withdrawal < withdrawal_limit) and (withdrawal <= balance)
# Out[8]: False

# COMMAND ----------

a = 20
b = 10

# COMMAND ----------

a / b > 1
# Out[10]: True

# COMMAND ----------

a = 20
b = 0

# COMMAND ----------

a / b > 1
# ZeroDivisionError: division by zero

# COMMAND ----------

b != 0 and a / b > 1

# COMMAND ----------

a = 20
b = 30

# COMMAND ----------

b != 0 and a / b > 1
# Out[15]: False
