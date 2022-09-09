# ----------------------------- MAP FUNCTION-----------------------------
"""map(func, *iterables) –> map object Make an iterator that computes the function using arguments from each of the
iterables. Stops when the shortest iterable is exhausted.
"""
numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))
numbers[2] = numbers[2] + 1
print(numbers[2])  # 65

"""
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers[2] = numbers[2] + 1
print(numbers[2])
"""

# -----------------------------MAP WITH LAMDA FUNCTION-----------------------------

items = [
    ("product1", 10),
    ("product2", 8),
    ("product3", 12),
]

"""prices = []
for item in items:
    prices.append(item[1])
print(prices)  # [10, 8, 12]"""

x = list(map(lambda item: item[1], items))
print(x)  # [10, 8, 12]

# ----------------------------------------------------------------------------------

number = [2, 3, 4, 5, 7, 89, 64, 3, 23, 4, 56]
square = list(map(lambda x: x * x, number))
print(square)  # [4, 9, 16, 25, 49, 7921, 4096, 9, 529, 16, 3136]

"""
def square_fun(a):
    return a*a

num = [2,3,4,5,7,89,64,3,23,4,56]
square = list(map(square_fun, num))
print(square)
"""


def square(a):
    return a * a


def cube(a):
    return a * a * a


func = [square, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)

# [0, 0]
# [1, 1]
# [4, 8]
# [9, 27]
# [16, 64]


# -----------------------------LAMDA FUNCTIONS OR ANONYMOUS FUNCTION-----------------------------
"""
def substract(x, y):
    return x - y
"""

substract = lambda x, y: x - y
print(substract(9, 5))  # 4

# -------------------------------------------------------------------------------------------------


items = [
    ("product1", 10),
    ("product2", 8),
    ("product3", 12),
]

"""
def sort_item(items):
    return items[1]
"""

items.sort(key=lambda item: item[1])
print(items)  # [('product2', 8), ('product1', 10), ('product3', 12)]

# -----------------------------LAMDA FUNCTIONS WITH SORT FUNCTION-----------------------------


# def a_first(a):
#     return a[1]
#
# a = [[1,26], [5,8], [9, 15], [8, 5]]
# a.sort(key=a_first)
# print(a) # [[8, 5], [5, 8], [9, 15], [1, 26]]

a = [[1, 26], [5, 8], [9, 15], [8, 5]]
a.sort(key=lambda x: x[1])
print(a)  # [[8, 5], [5, 8], [9, 15], [1, 26]]

# -----------------------------FILTER FUNCTION-----------------------------
"""filter(function or None, iterable) –> filter object Return an iterator yielding those items of iterable for which 
function(item) is true. If function is None, return the items that are tru """
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_5(num):
    return num > 5


gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)  # [6, 7, 8, 9]

# -------------------------------------------------------------------------------
items = [
    ("product1", 10),
    ("product2", 8),
    ("product3", 12),
]

x = list(filter(lambda item: item[1] >= 10, items))
print(x)
# [('product1', 10), ('product3', 12)]


# -----------------------------REDUCE FUNCTION-----------------------------
"""reduce(function, iterable[, initial]) -> value Apply a function of two arguments cumulatively to the items of a 
sequence or iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda 
x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the 
iterable in the calculation, and serves as a default when the iterable is empty. """

from functools import reduce

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num = reduce(lambda x, y: x + y, list_1)
print(num)  # 45

"""
num = 0
for i in list_1:
    num = num + i
print(num)
"""

# -----------------------------LIST COMPREHENSIONS-----------------------------
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
power_of_two = [x ** 2 for x in number if x % 2 == 0]
square_of = [x ** 2 for x in [x ** 2 for x in number if x % 2 == 0]]
print(power_of_two)
print(square_of)

"""
my_list=[]
for letter in 'abcd':
    for n in range(4):
        my_list.append((letter,n))
print(my_list)
"""

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)
# [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2),
# ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

# -----------------------------------------------------------------------------------
items = [
    ("product1", 10),
    ("product2", 8),
    ("product3", 12),
]

# [expression for item in items]
price = [item[1] for item in items]
print(price)
# [10, 8, 12]

filtered = [item for item in items if item[1] >= 10]
print(filtered)
# [('product1', 10), ('product3', 12)]


# -----------------------------DICTIONARY COMPREHENSIONS-----------------------------
dict = {"Maths": 180, "Physics": 170, "CS": 185, "Chemistry": 175}
dict1 = {key for key in dict.keys()}
print(dict1)
dict2 = {value // 2 for value in {value for value in dict.values()}}
print(dict2)
dict3 = {key: value for key, value in dict.items() if value % 2 == 0 if value <= 170}
print(dict3)

# -----------------------------SET COMPREHENSIONS-----------------------------

nums = [1, 2, 4, 1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 7, 8]
"""
my_sets=set()
for n in nums:
    my_sets.add(n)
print(my_sets)
"""

my_sets = {num for num in nums}
print(my_sets)  # {1, 2, 3, 4, 5, 6, 7, 8}

my_set = {num for num in nums if num % 2 == 0}
print(my_set)  # {8, 2, 4, 6}

# -----------------------------TUPLE COMPREHENSIONS-----------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
def gen_num(nums):
    for n in nums:
        # used to return from a function without destroying the states of its local variable
        yield n * n
my_gens = gen_num(nums)

for i in my_gens:
    print(i)
"""

my_tuple = (n * n for n in nums)
print(tuple(my_tuple))  # (1, 4, 9, 16, 25, 36, 49, 64, 81)
