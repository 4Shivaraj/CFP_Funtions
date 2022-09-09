#----------------------------------------------LIST MANIPULATION--------------------------------------------------------
letters = ["a", "b", "c"]
print(letters)  # ['a', 'b', 'c']
print(type(letters))  # <class 'list'>

zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

combined = letters + zeros
print(combined)  # ['a', 'b', 'c', 0, 0, 0, 0, 0]

numbers = list(range(20))
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

char = list("Hello world")
print(char)  # ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

print(len(char))  # 11

# Slicing of list

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#            0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#          -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# list[start:end:step]
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0])  # A
print(letters[0: 3])  # ['A', 'b', 'c']
print(letters[0:])  # ['A', 'b', 'c', 'd']
print(letters[:])  # ['A', 'b', 'c', 'd']
print(letters[::2])  # ['A', 'c']

numbers = list(range(20))
print(numbers[::-1])  # [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(numbers[::-2])  # [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

sample_url = 'http://coreyms.com'
print (sample_url)

# # Get the top level domain
print (sample_url[-4:])

# # Print the url without the http://
print (sample_url[7:])

# # Print the url without the http:// or the top level domain
print (sample_url[7:-4])

# List unpacking
numbers = [1, 2, 33, 78, 89]
first, second, *other = numbers
print(first)  # 1
print(second)  # 2
print(other)  # [33, 78, 89]

# Looping Over list
letters = ["a", "b", "c", "d"]

for letters in enumerate(letters):
    print(letters)
    # (0, 'a')
    # (1, 'b')
    # (2, 'c')
    # (3, 'd')

for index, letter in enumerate(letters):
    print(index, letter)
    # 0 a
    # 1 b
    # 2 c
    # 3 d

letters = ["a", "b", "c", "d"]

# Add
letters.append("e")
print(letters)  # ['a', 'b', 'c', 'd', 'e']

# Insert
letters.insert(0, "-")
print(letters)  # ['-', 'a', 'b', 'c', 'd', 'e']

# Remove
letters.pop()
print(letters)  # ['-', 'a', 'b', 'c', 'd']

letters.pop(0)
print(letters)  # ['a', 'b', 'c', 'd']

letters.remove("b")
print(letters)  # ['a', 'c', 'd']

del letters[0:2]
print(letters)  # ['d']

letters.clear()
print(letters)  # []

# Finding Objects in a list

letters = ["a", "b", "c", "d", "a", "a"]

print(letters.count("a"))  # 3

print(letters.index("a"))  # 0

# print(letters.index("e"))  # ValueError: 'e' is not in list

if "e" in letters: print(letters.index("e"))

# Sorting list
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)  # [2, 3, 6, 8, 51]

numbers.sort(reverse=True)
print(numbers)  # [51, 8, 6, 3, 2]

print(sorted(numbers))  # need to store it in variable


