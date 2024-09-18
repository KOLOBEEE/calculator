
welcomeNote = input("Enter your name: ")
print("Welcome to KOL calculator,", welcomeNote)
        


def calculator():

    choice = input("Please enter choice(yes/no): ")
    while choice == "yes":

        operation_keys = ["+","-","*","/"]
        print(operation_keys)
        operation = input("Enter one operation to use: ")
        print("You entered: ",operation)

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if  operation == '+':
         print("{} + {} =".format(num1,num2))
         print(num1 +num2)

        elif  operation == "*":
         print("{} * {} =".format(num1,num2))
         print(num1*num2) 

        elif operation == "/":
         print("{} / {} =".format(num1,num2))
         print(num1/num2)

        elif operation == "-":
         print("{} - {} =".format(num1,num2))
         print(num1-num2)

        else:
         print("Entered incorrect key.")

        choice = input("Would you like to continue?: ")

         
calculator()











