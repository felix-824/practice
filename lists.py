"""List
(1) Working with lists
(2) List methods
(3) Lambda function
(4) enumarate, map and filter
"""

print("==== Working with list ====")
# Java/PHPNodeJS array => Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")


# constructor
result = list("Hello World!")
print(f"the letters: {result} and size: {len(result)}")


print("------")
fruits = ["apple", "orange", "lemon", "kiwi", "melon"]

a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a) 
print("b:", b) 
print("c:", c) 
print("d:", d) 

print("==== List method ====")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b",] 

letters.append("c") # add behind 
print(f"the append letters: {letters}") 

letters.insert(0, "z") # add front
print(f"the insert letters: {letters}")

size = len(letters) - 1
result = letters.pop(size) # pop behind
print(f"the pop result: {result} and letters: {letters}")

result2 = letters.pop(0) # pop front
print(f"the pop result2: {result2} and letters: {letters}")


print("------")
animals = ["dog", "cat", "capybara", "fish", "lion",]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animal clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")    
    
print("------")
numbers = [2, 200, 63, 8, 57]
numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

#immutable >sorted function & index() method
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")



print("==== Lambda function ====") 
# lambda is samall anonymus function!
def calculate(x, y): return x * y 


result = calculate(3, 5)
print("result:", result)

people = [
    ("robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michel", 30),
    ("Ali", 40)
]   
people.sort()
print("people(1)", people)

#sort by age via lamba
people.sort(key=lambda person: person[1])
print("people(2)", people)