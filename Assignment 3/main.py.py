# Private variable starts with double underscore
# Protected variable starts with single underscore
# Public variable doesn't start with underscore

class Animals:

    def __init__(self):
        self.__eyes = 2       
        self._living = True   
        self.arms = 4         

    def seteyes(self, eyes):
        self.__eyes = eyes

    def geteyes(self):
        return self.__eyes

    def getliving(self):
        return self._living

    def setliving(self, living):
        self._living = living

    def getlegs(self):
        return self.legs
    
    def setlegs(self, legs):
        self.legs = legs
        


# Following are the child classes of Animal class
# They are Mammoth, Tiger, Cat, Rat, Deer, Elephant, Kangaroo, Monkey, Giraffe and Fox

class Mammoth(Animals):

    def eats(self):
        print("Mammoth eats meat!")

    def color(self):
        print("Color of Mammoth is Brown!")

    def sound(self):
        print("Mammoth produces sound")

    def typeOfAnimal(self):
        print("Mammoth is a carnivorous animal")


class Tiger(Animals):

    def eats(self):
        print("A tiger eats meat!")

    def color(self):
        print("Color of Tiger is orange with black stripes!")

    def sound(self):
        print("A tiger roars!")

    def typeOfAnimal(self):
        print("Tiger is a carnivorous animal")

class Giraffe(Animals):

    def eats(self):
        print("Giraffe eats leaves off the trees!")

    def color(self):
        print("Giraffe has patterns of dark brown, orange, or chestnut spots broken up by white or cream-coloured stripes!")

    def sound(self):
        print("A giraffe makes a flute like sound!")

    def typeOfAnimal(self):
        print("Giraffe is a herbivorous animal")

class Elephant(Animals):

    def eats(self):
        print("Elephant eat grass!")

    def color(self):
        print("An Elephant has greyish black color")

    def sound(self):
        print("Elephant trumpet")

    def typeOfAnimal(self):
        print("Elephant is a herbivorous animal")

class Monkey(Animals):

    def eats(self):
        print("Monkey eats vegetables and fruits")

    def color(self):
        print("Color of monkey is brown")

    def sound(self):
        print("A monkey makes a screeching sound!")

    def typeOfAnimal(self):
        print("Monkey is a herbivorous animal")

class Cat(Animals):

    def eats(self):
        print("A cat eats meat, veggies, dog-food etc.!")

    def color(self):
        print("A cat could be of any color, it depends on the breed.")

    def sound(self):
        print("A cat Meows!")

    def typeOfAnimal(self):
        print("cat is an omnivorous animal")

class Rat(Animals):

    def eats(self):
        print("Rat eats anything including garbage!")

    def color(self):
        print("Rats can be white, black or gray in color!")

    def sound(self):
        print("A rat squeaks!")

    def typeOfAnimal(self):
        print("Rat is an omnivorous animal")

class Kangaroo(Animals):

    def eats(self):
        print("A Kangaroo eats vegetables, plants, leaves!")

    def color(self):
        print("A Kangaroo is blue-grey or brown in color!")

    def sound(self):
        print("A Kangaroo growls or barks!")

    def typeOfAnimal(self):
        print("Kangaroo is a herbivorous animal")

class Fox(Animals):

    def eats(self):
        print("Fox eats meat!")

    def color(self):
        print("Color of Fox is brown")

    def sound(self):
        print("A fox makes sounds like hissing, growling or champing of teeth!")

    def typeOfAnimal(self):
        print("Fox is a carnivorous animal")

class Deer(Animals):

    def eats(self):
        print("A deer eats plants, leaves!")

    def color(self):
        print("Color of Lion is Reddish brown or Grayish brown!")

    def sound(self):
        print("A Deer makes a grunting sound or a bleating sound!")

    def typeOfAnimal(self):
        print("Deer is a herbivorous animal")