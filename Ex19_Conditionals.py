# Create a program to calculate the BMI (Body mass index) of a person.
# Ask the user for his height in meters and his weight in kg.
# Print BMI in the classification:
#     - Underweight: Less or equal to 18.5
#     - Normal Weight: Greater than 18.5 or less than or equal to 24.9
#     - Overweight: Greater than 24.9 or less than or equal to 29.9
#     - Obesity: Greater than or equal to 30

print("This program calculates your Body Mass Index")
height = float(input("Your height (mts): "))
weight = float(input("Your weight (kgs): "))

bmi = round(weight / (height * height), 2)

print("Your BMI: ", bmi)

if (bmi <= 18.5):
    classification = "Underweight"
elif (bmi > 18.5 and bmi <= 24.9):
    classification = "Normal weight"
elif (bmi > 24.9 and bmi <= 29.9):
    classification = "Overweight"
else:
    classification = "Obesity"


print("The calssification of your BMI is: ", classification)
