# Databricks notebook source
1

# COMMAND ----------

-10

# COMMAND ----------

1.0

# COMMAND ----------

-10.6

# COMMAND ----------

True

# COMMAND ----------

False

# COMMAND ----------

0.1

# COMMAND ----------

format(0.1, ".25f")

# COMMAND ----------

format(0.125, ".25f")

# COMMAND ----------

1 + 1 + 1 == 3

# COMMAND ----------

0.125 + 0.125 + 0.125 == 0.375

# COMMAND ----------

0.1 + 0.1 + 0.1 == 0.3

# Out[12]: False

# COMMAND ----------

format(0.1 + 0.1 + 0.1, ".25f")

# Out[13]: '0.3000000000000000444089210'

# COMMAND ----------

format(0.3, ".25f")

# Out[14]: '0.2999999999999999888977698'

# COMMAND ----------

# Do not compare floats using equality (==). It is not going to work as expected.
# Instead look at the difference between the 2 numbers, look at the absolute value of the difference and see if that is less than some tolerance

# COMMAND ----------

abs(0.1 + 0.1 + 0.1 - 0.3)

# Out[16]: 5.551115123125783e-17

# COMMAND ----------

abs(0.1 + 0.1 + 0.1 - 0.3) < 0.001

# Out[17]: True

# COMMAND ----------


