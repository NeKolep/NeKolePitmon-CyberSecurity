#Ne'Kole Pitmon 10/28/2023
#this is my flower code
class Flower:#define an object called flower
    def __init__(self, name):#method
        self.name = name

    def grow(self):#method
        print("The " +self.name + " is growing.")

    def bloom(self):#method
        print("The " + self.name + " is blooming.")
#rose,daisy, and tulip are the attributes. They are the name of the object flower.
def main():#main is here to do....
    flower1 = Flower("Rose")#create object flower1 from flower
    flower1.grow()
    flower1.bloom()
    flower2 = Flower("Daisy")#create object flower2 from flower
    flower2.grow()
    flower2.bloom()
    flower3 = Flower("tulip")#create object flower3 from flower
    flower3.grow()
    flower3.bloom()

if __name__ == "__main__":#this is telling the program to execute the main
  main()
