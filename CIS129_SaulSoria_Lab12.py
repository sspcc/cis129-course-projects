# Module 11 Lab
# Saul Soria
# 07/29/24
# Program that retrieves the name, type and age of a pet utilizing a class and object
# Define the Pet class
class Pet:
    def __init__(self, name='', pet_type='', age=0):
        self.name = name
        self.pet_type = pet_type
        self.age = age

    def setName(self, name):
        self.name = name.title()

    def setType(self, pet_type):
        self.pet_type = pet_type.lower()

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getType(self):
        return self.pet_type

    def getAge(self):
        return self.age

# Main module
def main():
    # Create the Pet object
    animal = Pet()

    # Retrieve the pet's name from the user
    while True:
        inputName = input("Enter a pet name: ").strip()
        if inputName:
            animal.setName(inputName)
            break
        else:
            print("Invalid input. The pet name cannot be empty.")

    # Retrieve the pet's type from the user
    while True:
        inputType = input("Enter a pet type: ").strip()
        if inputType:
            animal.setType(inputType)
            break
        else:
            print("Invalid input. The pet type cannot be empty.")

    # Retrieve the pet's age from the user
    while True:
        inputAge = input("Enter a pet age: ").strip()
        if inputAge.isdigit() and int(inputAge) > 0:
            animal.setAge(int(inputAge))
            break
        else:
            print("Invalid input. The pet age must be a positive integer.")

    # Print the pet's data
    print("The pet name is", animal.getName())
    print("The pet type is", animal.getType())
    print("The pet age is", animal.getAge())

# Call the main function
if __name__ == "__main__":
    main()
