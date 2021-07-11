class Organism:
    alive = True
    pass

class Animal(Organism):
    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")

class Cat(Animal):
    def meow(self):
        print("The cat is meowing")

animal = Animal()
cat = Cat()

print(animal.alive)
# animal.eat()
# animal.sleep()

print(cat.alive)
# cat.eat()
# cat.sleep()
# cat.meow()