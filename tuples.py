"""Tuple
(1) What is tuple: typle vs list
(2) Unpacking arguments
(3) zip
"""

print("==== What is tuple: typle vs list ====")
# Java/PHP/NodeJs array => list

# literal
numbs = [3, 5, 1, 2]

# constractor
letters = list("Hello World!")


fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# we can not mutate tuple
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
#animals[0] = "brid"

#try avoid thse
people = "Anderew", "John"
animals = "dog",


print("==== Unpacking arguments ====")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}") 
print(f"z:", z) # list


# *args > tuple
def calculate(*args):
    print("*args", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


#CALL  
calculate(1, 7, 2, 3)
calculate(0, 2, 300)
calculate(5, 7)    

print("----")
# **kwargs > dictionary
def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi I am {kwargs["name"]} and I am {kwargs["age"]} years old!")
    pass


#CALL
introduce(name="Justin", age=25)
introduce(name="Shawn", age=30, single=True)