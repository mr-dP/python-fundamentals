# Databricks notebook source
1 + 0.5

# COMMAND ----------

1.0 + 0.5

# COMMAND ----------

2 * 1.125

# COMMAND ----------

18 / 4

# COMMAND ----------

2 ** 8

# COMMAND ----------

2 ** -8

# COMMAND ----------

2 ** (-8)

# COMMAND ----------

1 / (2 ** 8)

# COMMAND ----------

4.0 ** 0.5

# COMMAND ----------

(-4) ** 0.5

# COMMAND ----------

c = (-4) ** 0.5

# COMMAND ----------

c
# Out[12]: (1.2246467991473532e-16+2j)

# COMMAND ----------

type(c)
# Out[13]: complex

# COMMAND ----------

type(10)

# COMMAND ----------

type(10.0)

# COMMAND ----------

c.real
# Out[16]: 1.2246467991473532e-16

# COMMAND ----------

c.imag
# Out[17]: 2.0

# COMMAND ----------

c = 10 + 4j

# COMMAND ----------

c

# COMMAND ----------

(10).__add__(20)

# COMMAND ----------

(10).__mul__(3)

# COMMAND ----------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# COMMAND ----------

v1 = Vector(1, 1)
v2 = Vector(2, 3)

# COMMAND ----------

v1

# COMMAND ----------

v2

# COMMAND ----------

v1 + v2

# TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'

# COMMAND ----------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# COMMAND ----------

v1 = Vector(1, 1)
v2 = Vector(2, 3)

# COMMAND ----------

v1 + v2
# Out[30]: Vector(3, 4)

# COMMAND ----------


