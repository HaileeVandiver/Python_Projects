
#parent class pokemon 
class Pokemon:
    name = "Unknown"
    temperment = "Unknown" 

    def information(self):
        print("Hello my name is {}".format(self.name))


# child class water type
class Water_Type(Pokemon):
    name = "squirtle"
    attack = "water cannon"
    health = 90
#polymorphism
    def information(self):
        print("Hello my name is {} and I'm a water type pokemon".format(self.name))

    def water_cannon(self):
        print("Squirtle uses water attack!")

#child class grass type
class Grass_Type(Pokemon):
    name = "bulbasaur"
    attack = "thorn whip"
    health = 80

#polymorphism

    def thorn_whip(self):
        print("bulba uses thorn whip!")

    def information(self):
        print("Hello my name is {} and I'm a grass type pokemon".format(self.name))

Clefairy = Pokemon()
Clefairy.information()

Squirtle = Water_Type()
Squirtle.information()
        
        


    
