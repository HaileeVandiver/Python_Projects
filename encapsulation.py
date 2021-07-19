
# program to illustrate protected
# data members in a class 
  
  
# Defining a class
class Geek: 
      
    # protected data members 
    _name = "Dustfinger Capricorn"
    _roll = 20
      
    # public member function 
    def displayNameAndRoll(self): 
  
        # accessing protected data members 
        print("Name: ", self._name) 
        print("Roll: ", self._roll) 
  
  
# creating objects of the class         
obj = Geek() 
  
# calling public member 
# functions of the class 
obj.displayNameAndRoll() 
