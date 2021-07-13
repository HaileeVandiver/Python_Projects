class Pokemon:
    def __init__(self,name,species,power):
        self.name = name
        self.species = species
        self.power = power



    def information(self):
        print("Hello my name are " + self.name)



Squirtle = Pokemon("Squirtle", "Water", 100)
Squirtle.information()



# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True


    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs:{} \nArms: {}\nDNA: {}".format(self.name,self.species,self.legs,self.arms,self.dna)
        return msg
#child class instance
class Human(Organism):
    name = "Hailee"
    species = "Human"
    legs = 2
    arms = 2
    origin = "Earth"

    def smarts(self):
        msg = "\n Hailee is so smart"
        return msg

# another child class instance

class Dog(Organism):
    name = "Chrono"
    species = "Doggo"
    legs = 4
    arms = 0
    dna = "Sequence b"
    origin = "Earth"


    def bite(self):
        msg= "\n oooh so scary"
        return msg






if __name__ =="__main__" :
    human = Human()
    print(human.information())
    print(human.smarts())

    dog = Dog()
    print(dog.information())
    print(dog.bite())



    
