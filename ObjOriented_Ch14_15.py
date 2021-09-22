#This is the template for makingPArtyAnimal Objects (an exampleof OO)
class PartyAnimal:
    x=0 #Each PartyAnimalobject has a bit of data

# Each PartyAnimal object has a bit of code
    def party(self):
        self.x = self.x + 1
        print("So Far", self.x)

#Construct a PartyAnimal object and store in 'an' variable
# "Mints" the class
an = PartyAnimal() # Moment of construction

 # Tell the an object to run the party() code within it.
 #Calls the function
an.party() # an.party() is a contraction of PartyAnimal.party(an)
an.party() # Invokes the method
an.party()


#Inheritance

class PartyAnimal:
    x = 0
    name = ""
    def _init_(self, nam):
        self.name = Nam
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

##Child (Inheritance) - FootballFan is a class which extends PartyAnimal.
##It has all the capabilities of PartyAnimal and more.
##It's like an extension
## "Class FootballFan extends PartyAnimal plus more"
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
