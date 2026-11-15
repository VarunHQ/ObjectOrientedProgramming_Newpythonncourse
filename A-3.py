class Parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

gre = Parrot("gre", 5)
too = Parrot("too", 10)

print(f"gre is a {gre.species}")
print(f"too is also a {too.species}")

print(f"{gre.name} age is {gre.age}")
print(f"{too.name} age is {too.age}")