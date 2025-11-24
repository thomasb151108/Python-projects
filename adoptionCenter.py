import time
import os
import time

class Pet:
    def __init__(self, name, species, age, is_adopted):
        self.name = name
        self.species = species
        self.age = int(age)
        self.is_adopted = bool(is_adopted)
    
    def display_details(self):
        if self.is_adopted:
            a = "adopted"
        else:
            a = "available for adoption"
        print("-----PET DETAILS-----"  )
        print(self.name,"is a", self.species+ ", he is", self.age,"years old and their adoption status is", a)
        print()
    
    def adopt(self):
        self.is_adopted = True
    
    def return_to_shelter(self):
        self.is_adopted = False

class Adopter:
    def __init__(self, name, adopter_id, adopted_pets=None):
        self.name = str(name)
        self.adopter_id = str(adopter_id)
        self.adopted_pets = []
    
    def adopt_pet(self, pet_object):
        self.adopted_pets.append(pet_object.name)
        pet_object.adopt()
      
    def return_pet(self, pet_object):
        if pet_object.name in self.adopted_pets:
            self.adopted_pets.remove(pet_object.name)
            pet_object.return_to_shelter()
    
    def display_details(self):
        print("-----ADOPTER DETAILS-----")
        print("name: "+self.name)
        print("adopter ID: "+self.adopter_id)
        print("adopted pets: "+", ".join(self.adopted_pets))
        print()

class Shelter:
    def __init__(self, pets, adopters):
        self.pets = []
        self.adopters = []
    
    def add_pet(self, name, species, age):
        pet = Pet(name, species, age, False)
        self.pets.append(pet)
    
    def add_adopter(self, name, adopter_id):
        adopter = Adopter(name, adopter_id)
        self.adopters.append(adopter)

    def find_pet(self, name):
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                return pet
        return None

    def find_adopter(self, adopter_id):
        for adopter in self.adopters:
            if adopter.adopter_id == adopter_id:
                return adopter
        return None

    def process_adoption(self, adopter_id, pet_name):
        adopter = self.find_adopter(adopter_id)
        pet = self.find_pet(pet_name)
        
        if not adopter:
            print(f"Error: Adopter with ID '{adopter_id}' not found.")
            return
        
        if not pet:
            print(f"Error: Pet '{pet_name}' not found.")
            return
        
        if pet.is_adopted:
            print(f"Error: Pet '{pet_name}' is already adopted.")
            return
        
        pet.adopt()
        adopter.adopt_pet(pet)
        print(f"Success: {adopter.name} has adopted {pet.name}!")

    def process_return(self, adopter_id, pet_name):
        pet = self.find_pet(pet_name)
        adopter = self.find_adopter(adopter_id)
        if pet and adopter:
            adopter.return_pet(pet)
            print(f"Success: {adopter.name} has retuned {pet.name}!, goodybe {pet.name}!")

def printMenu():
    print("========== ADOPTION CENTER MENU ==========")
    print("1. Add Pet")
    print("2. Register Adopter")
    print("3. Process Adoption")
    print("4. Process Return")
    print("5. Display Pet Details")
    print("6. Display Adopter Details")
    print("7. List of pets")
    print("8. List of adopters")
    print("9. Exit")
    print("==========================================")

my_shelter = Shelter([], [])

while True:
    os.system("clear")
    printMenu()
    choice = input("Enter option (1-9): ")
    
    if choice == "9":
        print("Thank you for using the Adoption Center. Goodbye!")
        break
    
    if choice not in ["1","2","3","4","5","6","7","8"]:
        print("Invalid option. Please try again.")
        continue
    
    if choice == "1":
        name = input("Enter pet name: ")
        species = input("Enter pet species: ")
        age = input("Enter pet age: ")
        my_shelter.add_pet(name, species, age)
        print(f"pet {name} added successfully!")
        time.sleep(2)
    
    elif choice == "2":
        name = input("Enter adopter name: ")
        adopter_id = input("Enter adopter ID: ")
        my_shelter.add_adopter(name, adopter_id)
        print(f"Adopter {name} registered successfully!")
        time.sleep(2)
   
    elif choice == "3":
        id = input("Enter adopter id: ")
        name = input("Enter pet name: ")
        my_shelter.process_adoption(id, name)
        time.sleep(2.5)
   
    elif choice == "4":
        id = input("Enter adopter id: ")
        name = input("Enter pet name: ")
        my_shelter.process_return(id, name)
        time.sleep(2.5)
   
    elif choice == "5":
        name = input("Enter pet name: ")
        pet = my_shelter.find_pet(name)
        if pet:
            pet.display_details()
            time.sleep(3.5)
        else:
            print(f"Error: Pet '{name}' not found.")
            time.sleep(2)
   
    elif choice == "6":
        id = input("Enter adopter ID: ")
        adopter = my_shelter.find_adopter(id)
        if adopter:
            adopter.display_details()
            time.sleep(3.5)
        else:
            print(f"Error: Adopter with ID '{id}' not found.")
            time.sleep(2)
  
    elif choice == "7":
        print("-----LIST OF PETS-----")
        for pet in my_shelter.pets:
            status = "Adopted" if pet.is_adopted else "Available"
            print(f"{pet.name} ¦ {species} ¦ {status}")
        time.sleep(1.5*len(my_shelter.pets))
        print()
  
    elif choice == "8":
        print("-----LIST OF ADOPTERS-----")
        for adopter in my_shelter.adopters:
            print(f"{adopter.name} ¦ ID: {adopter.adopter_id}")
        time.sleep(1.5*len(my_shelter.adopters))
        print()

#test code:
#my_shelter.add_pet("max", "Dog", 3)
#my_shelter.add_adopter("Alice", "A123")
#my_shelter.process_adoption("A123", "max")

#my_shelter.find_pet("max").display_details()
#my_shelter.find_adopter("A123").display_details()
#my_shelter.process_return("A123", "max")
#my_shelter.find_adopter("A123").display_details()
#my_shelter.find_pet("max").display_details()