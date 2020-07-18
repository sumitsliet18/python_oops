class Customer:
    def __init__(self,name):
        self.name=name
        print("The __init__ method was called")
cust=Customer("Sumit Kumar")
print(cust.name)
