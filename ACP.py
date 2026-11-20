class Pet:
    print("Hi, I am a pet profile class!")
pet_object = Pet()
class PetProfile:
    category = "pet"
 
    def __init__(self, name, animal_type,breed, age, favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.breed = breed
        self.age = age
        self.favourite_food = favourite_food
 
pet1 = PetProfile("timmi", "dog", "french bulldog", 5, "chicken")
pet2 = PetProfile("milo", "cat", "ginger", 3, "fish")
 
print("timmi is a", pet1.category)
print("milo is also a", pet2.category)

print("timmi is a", pet1.animal_type, "and is", pet1.age, "years old.", "his breed is", pet1.breed)
print("timmi likes eating", pet1.favourite_food)

print("milo is a", pet2.animal_type, "and is", pet2.age, "years old.", "her breed is", pet2.breed)
print("milo likes eating", pet2.favourite_food)
