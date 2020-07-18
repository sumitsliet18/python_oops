class Customer:
    #code for class goes here
    pass
c1=Customer()
c2=Customer()

#Add method to a class
class Customer:
    def identify(self,name):
        print('I am customer ' +name)
cust=Customer()
cust.identify('sumit')
#Add attribute to a class
class Customer:
    def set_name(self,new_name):
        self.name=new_name
cust=Customer()
cust.set_name('sumit')
print(cust.name)