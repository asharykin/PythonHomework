class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def makesound(self):
        pass


class Cat(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def makesound(self):
        print(f"Кошка говорит '{self.sound}'")


class Dog(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def makesound(self):
        print(f"Собака говорит '{self.sound}'")
