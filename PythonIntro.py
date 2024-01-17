# python intro
str = '''python is an interesting language
in the world of web development and
in the world of data science as well.'''
print(str)

# data types
data_type = 'there are basically five data types in python namely: \n\
1. numeric\n\
2. boolean\n\
3. sequence\n\
4. set\n\
5. dictionary'

# variables, identifiers, expressions, statements
age = 9 # age is variable
def info(): # info is identifier
    pass
x = 9 + 10 # expression
for i in range(age): # statement
    b = []
    b.append(x)

# types of operators
# airthmetic operators
9 + 10 # addition
9 - 10 # subtraction
9 * 10 # multiplication
9 / 10 # division
9 % 10 # modulo division
9 // 10 # floor division
9 ** 10 # exponentiation

# assignment operators
a = 9
a += 9
a -= 9
a /= 9
a *= 9
a %= 9
a //= 9
a **= 9
a = 9
a &= 0
a |= 0
a ^= 0
a >>= 0
a <<= 0

# logical operators
a and x # logical and
a or x # logical or
not x # logical not

# comparison operators
9 > 10 # greater than
9 < 10 # less than
9 >= 10 # greater than or equal to
9 <= 10 # less than or equal to
9 == 10 # equal to
9 != 10 # not equal to

# bitwise operators
9 & 10 # bitwise and
9 | 10 # bitwise or
9 >> 10 # bitwise right shift
9 << 10 # bitwise left shift
~ 10 # bitwise not
9 ^ 10 # bitwise xor

# identity operator
a is x # a == x
a is not x # a != x

# membership operator
9 in b # a belongs to b
9 not in b # a does not belong to b

# file handling
f = open("GamesOfArena.py",'r')
string = f.readline()
print("printing first text of GamesOfArena.py: " + string)

# built-in data structures
my_list = [1,2,3,4,4] # mutable,ordered and duplicates allowed
my_tuple = (1,2,3,4,4) # immutable,ordered and duplicates allowed
my_set = {1,2,3,4} # mutable,unordered and duplicates not allowed
my_dict = {1:'a',2:'b'} # mutable,ordered and duplicates not allowed
print(f"{type(my_list)}\n{type(my_tuple)}\n{type(my_set)}\n{type(my_dict)}")

# list methods
print(my_list)
print(my_list.insert(2,4))
print(my_list.remove(4))
print(my_list.extend([8,9]))
print(my_list.reverse())
print(my_list.sort())
print(my_list.append(5))
print(my_list.pop())
print(my_list.index(4))
print(my_list.count(4))
my_list1 = my_list.copy()
my_list1.clear()

# tuple methods
print(my_tuple)
print(my_tuple.index(4))
print(my_tuple.count(4))

# set methods
print(my_set)
print(my_set.add(5))
print(my_set.discard(5))
print(my_set.update({7,9}))
print(my_set.union({11,12}))
print(my_set.intersection({4,5}))
print(my_set.difference({1,2,3}))
print(my_set.pop())
my_set1 = my_set.copy()
my_set1.clear()

# dictionary methods
print(my_dict)
print(my_dict.update({3:'ab'}))
print(my_dict.pop(3))
print(my_dict.popitem())
print(my_dict.get(1))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.setdefault(0))
my_dict2 = my_dict.fromkeys({1},0)
my_dict1 = my_dict.copy()
my_dict1.clear()
print(my_dict,my_dict1,my_dict2)