from pet_record import Pet

name = input("Name of the Pet:")
type_of_animal = input("Type of Animal:")
pet_age = input("Age of the Pet:")

my_pet = Pet(name, type_of_animal, pet_age)

print("\nPet Information")
print("Name:", my_pet.get_name())
print("Animal Type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())