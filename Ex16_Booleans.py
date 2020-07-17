# Create a program and sotore your age in a variable
# Then ask the user for his age and print whether:
#   - He's older than you
#   - He's younger than you
#   - You two have the same age

my_age = 33
his_age = int (input("What is your age: "))

if(his_age > my_age):
    print ("You are older tah me")
elif(his_age == my_age):
    print("We are the same age")
else:
    print("You are younger than me")