# Databricks notebook source
# To see if two objects are the same object                                     ->      is
# To see two (comparable) obkects are equal in value (in some cases)            ->      ==

# COMMAND ----------

# The "is" operator is purely concerned with the memory address (identity) of the objects

# COMMAND ----------

# The "==" operator, is, like "+", actually implemented by the type itself
#       __eq__ method

# COMMAND ----------

# Membership operator:      in      not in

# "in" operator uses equality to test whether something is in the collection
#           s = {1, 2, 3.14, True, 5.1}
#           1 in s      ->      True

# COMMAND ----------



# COMMAND ----------

a = 10
b = 10

# COMMAND ----------

a == b
# Out[6]: True

# COMMAND ----------

c = 10.0

# COMMAND ----------

a == c
# Out[8]: True

# COMMAND ----------

a is c
# Out[9]: False

# COMMAND ----------

id(a)
# Out[10]: 140257505192528

# COMMAND ----------

id(c)
# Out[11]: 140256866447216

# COMMAND ----------

a = 10
b = 10.0

# COMMAND ----------

a == b
# Out[13]: True

# COMMAND ----------

a is b
# Out[14]: False

# COMMAND ----------

id(a), id(b)
# Out[15]: (140257505192528, 140256866446096)

# COMMAND ----------

a = 10

# COMMAND ----------

b = 10

# COMMAND ----------

a is b
# Out[18]: True

# For small numbers, Python pre-creates them ahead of time and whenever you want to use, say 10, it will re-use the existing one

# COMMAND ----------

id(a), id(b)
# Out[19]: (140257505192528, 140257505192528)

# COMMAND ----------

a = 10_000

# COMMAND ----------

b = 10_000

# COMMAND ----------

a is b
# Out[22]: False

# COMMAND ----------

id(a), id(b)
# Out[23]: (140256866445392, 140256866444944)

# COMMAND ----------

10 != 12

# COMMAND ----------

10.5 != 10.5

# COMMAND ----------

10 >= 5

# COMMAND ----------

10.5 < 100

# COMMAND ----------

(10.5).__lt__(100)

# COMMAND ----------

(10).__eq__(10)

# COMMAND ----------

a = 1 + 1j
b = 1 + 1j
c = 2 + 2j

# COMMAND ----------

a == b
# Out[31]: True

# COMMAND ----------

a is b, id(a), id(b)
# Out[32]: (False, 140256041016016, 140256041013648)

# COMMAND ----------

a < c
# TypeError: '<' not supported between instances of 'complex' and 'complex'

# COMMAND ----------

# Because Floats rarely have exact representations in Python, we should really not "==" to test if 2 Float values are the same

0.1 * 3 == 0.3
# Out[35]: False

# COMMAND ----------

0.1 * 3
# Out[36]: 0.30000000000000004

# COMMAND ----------



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
v2 = Vector(1, 1)
v3 = Vector(2, 3)

# COMMAND ----------

id(v1), id(v2), id(v3)
# Out[38]: (140334612294240, 140334612293760, 140334612294192)

# COMMAND ----------

v1 is v2
# Out[39]: False

# COMMAND ----------

v1 == v2
# Out[40]: False

# By default, when you create your own custom types, Python will basically use Identity Comparison for the equality (==)

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

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

# COMMAND ----------

v1 = Vector(1, 1)
v2 = Vector(1, 1)
v3 = Vector(2, 3)

# COMMAND ----------

id(v1), id(v2), id(v3)
# Out[43]: (140240053871664, 140241433744000, 140240053872768)

# COMMAND ----------

v1 is v2
# Out[44]: False

# COMMAND ----------

v1 == v2
# Out[45]: True

# COMMAND ----------

v2 == v3
# Out[46]: False

# COMMAND ----------


