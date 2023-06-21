# Databricks notebook source
# Python integer division:      //
# Remainder:                    Use Python "mod" operator     %

# COMMAND ----------

# (a // b) is the floor of (a / b)
# floor(x)  ->  the largest integer number <= x

# COMMAND ----------

# a / b = a // b + (a % b) / b
# a % b = a - b (a // b)

# COMMAND ----------

#   12 % 5        ->    2
#   12 % -5       ->    -3
#   -12 % 5       ->    3
#   -12 % -5      ->    -2

# COMMAND ----------

a = 10
b = 3

# COMMAND ----------

a / b

# COMMAND ----------

a // b

# COMMAND ----------

-12 / 5

# COMMAND ----------

-12 // 5

# COMMAND ----------

a % b

# COMMAND ----------

4 % 2

# COMMAND ----------

5 % 2

# COMMAND ----------

13567 % 2

# COMMAND ----------

elapsed_minutes = 165

# COMMAND ----------

165 / 60

# COMMAND ----------

165 - (2 * 60)

# COMMAND ----------

165 - (165 // 60 * 60)

# COMMAND ----------

165 % 60

# COMMAND ----------

elapsed_minutes = 165
hours = elapsed_minutes // 60
remaining_minutes = elapsed_minutes % 60

print(hours, remaining_minutes)

# COMMAND ----------

total = 0
for i in range(1, 1_001):
    total += i
    print(f"total = {total}...")
print(f"Final total = {total}")

# COMMAND ----------

total = 0
for i in range(1, 1_001):
    total += i
    if i % 100 == 0:
        print(f"total = {total}...")
print(f"Final total = {total}")

# COMMAND ----------


