# Create a program with a predefined dictionary for a person
# Include the following information: name, gender, age, address and phone.
# Ask the user what information he wants to know about the person
# then print the value associated to that key or display a message in case the key is not found

person = {"name": "emmanuel casas", "gender": "male", "age": 33,
          "address": "San Fracnsico Av 23342", "phone": "55 1243 1243"}

key = input("What you want to know: ").lower()

value = person.get(key, 'Invalid key')

print(value)