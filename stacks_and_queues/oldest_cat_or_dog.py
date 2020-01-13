class Animal:
    def __init__(self, name: str):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class AnimalShelter:
    def __init__(self):
        self.cats = list()
        self.dogs = list()

    def enqueue(self, animal):
        if animal.__class__ == Cat:
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_dog(self):
        if self.dogs:
            dog = self.dogs[0]
            self.dogs = self.dogs[1:]
            return dog.name

    def dequeue_cat(self):
        if self.cats:
            cat = self.cats[0]
            self.cats = self.cats[1:]
            return cat.name

    def dequeue_any(self):
        if not len(self.cats):
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue(Cat("Hanzack"))
    shelter.enqueue(Dog("Pluto"))
    shelter.enqueue(Cat("Garfield"))
    shelter.enqueue(Cat("Tony"))
    shelter.enqueue(Dog("Clifford"))
    shelter.enqueue(Dog("Blue"))

    print(shelter.dequeue_dog())
    print(shelter.dequeue_dog())