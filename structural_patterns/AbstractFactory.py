class Dog:
    def speak(self):
        return "Woof"

    def __str__(self):
        return "Dog"

class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"

class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Say hello to my pet, {pet}.\nSay hi, {pet}...\n\"{pet.speak()}!\"\nThis {pet} eats {pet_food}")


factory = DogFactory()
store = PetStore(factory)
store.show_pet()