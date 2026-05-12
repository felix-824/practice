"""CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE
(3) POLIMORPHISM
"""

print("==== ENCAPSULATION ====")
# ENCAPSULATION > public __private _protected


class Account:
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self._owner = owner
        self._amount = amount
    
    # method
    def get_balance(self):
        print(f"the _owner {self._owner} has {self._amount} usd")
    
    def deposit(self, amount):
        print("deposit:", amount)
        self._amount += amount
    
    def withdraw(self, amount):
        print("withdraw:", amount)
        self._amount -= amount     
     
    @property
    def holder(self):
        return self._owner
    
    
    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self._owner = new_owner
    
    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self._owner = new_owner
            
        
my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-----")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()        
        
print("-----")   

try:
    result = my_account._amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)
    
    #getter vs setter
print("owner before:", my_account.holder) #state 
my_account.holder = "Martin"
print("owner after:", my_account.holder)