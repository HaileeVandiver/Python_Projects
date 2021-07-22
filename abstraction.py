from abc import ABC, abstractmethod
class pokemon(ABC):
#regular method
    def regularmethod(self):
        print("stay out of the tall grass") 
#abstract method
    @abstractmethod
    def type(self):
        pass

#child class
class charmander(pokemon):
#defines the implementation of parent's abstract method
    def type(self):
        print("I am a fire type")
    def attack(self):
        print("charmander used flamethrower") 

#object utilizing both parent and child methods
obj = charmander()
obj.type()
obj.attack()
obj.regularmethod()



