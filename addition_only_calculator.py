print("This program will return the sum of the 2 numbers you enter.")
num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")
result = float(num1) + float(num2) #converts the 2 string inputs of the user into a float

print("The sum of " + num1 + " and " + num2 + " is " + str(result)) #prints the result in a legible way and converts the float back to a string to enbale it to be added like this here.

print("Press enter to close the program")
input()