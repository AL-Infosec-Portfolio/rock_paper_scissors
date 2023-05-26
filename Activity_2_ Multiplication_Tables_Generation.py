# Display welcome message
print("Welcome Multiplication Game!")
print()

# ask user to input their name
user = input("Enter your name: ").upper()
print()

# ask user to enter a number for the multiplier
multiplier = input("Enter a number for the multiplier: ")
print(f"You chose {multiplier} as the multiplier" )
print()
# confirm if the user enter the number they wanted
check_multiplier = input("Is this correct? Type 'y' for yes or 'n' for no: ").lower()

# control structure to make sure that the multiplier is the correct one you want
if check_multiplier != "y":
    # checks if the user inputted the correct number and only exist when user confirms
    while check_multiplier != "y":
        print()
        multiplier = input("Enter a number for the multiplier: ")
        check_multiplier = input("Is this correct? Type 'y' for yes or 'n' for no: ").lower()
               

print()
print(f"The multiplier is {multiplier}")
print()


for multiplicand in range(1,13):
    product = multiplicand * int(multiplier)
    print(f"{multiplicand} x {multiplier} = {product}")

print()
print(f"Thank you {user} for playing!")


