"""FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
"""

print("===DEFINE vs CALL ====")
# build in function > print() type()
# Function - reusable block of code! malum bir mantiqni ishga tushirib beradigan kod blok
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet("David")
print("result1:", result1)

result2 = greeting("Jastin")
print("result2:", result2)
