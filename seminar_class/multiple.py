class Prey:
    def flee(self):
        print("The prey is fleeing")

class Predator:
    def hunt(self):
        print("The predator is hunting")

class Rabbit(Prey):
    pass

class Eagle(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
eagle = Eagle()
fish = Fish()

rabbit.flee()
eagle.hunt()
fish.flee()
fish.hunt()

