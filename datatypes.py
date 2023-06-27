# Python has 4 primitive datatype
a: int = 10  # Integer
print(f"a : {type(a)}")
b: float = 5.5  # Float
print(f"b : {type(b)}")
c: str = "Hello"  # String
print(f"c : {type(c)}")
d: bool = True  # Boolean
print(f"d : {type(d)}")

# Python also has 3 collections namely , List, Dictionary and Tuple

# A list is defined using square brackets
list1: list = [1, 2, 3, 4, 5, 6]
print(f"list1 : {type(list1)}")

# A Dictionary is a collection similar maps , it is a collection of key-value pair
info: dict = {"Name": "Chethan", "Branch": "CSE", "Semester": 3}
print(f"info : {type(info)}")

# A tuple is an immutable list i.e, the data in the tuple can not be changed in any manner
prime_nums: tuple = (1, 2, 3, 5, 7)
print(f"prime_nums : {type(prime_nums)}")
