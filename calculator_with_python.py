
def addition(a,b):
   print(f"Additon: {a} + {b} =",a+b)
def multiplication(a,b):
    print(f"Multiplication: {a} * {b} =",a*b)
def subtraction(a,b):
    print(f"Subtraction: {a} - {b} =",a-b)
def divison(a,b):
 try:
    result=a/b
    print(f" Divison: {a} / {b} =",a/b)
 except (ZeroDivisionError, ValueError):
    print('Please enter number greater than zero')
def modulus(a,b):
    print(f"Modulus: {a} % {b} =",a%b)

print("""Select operation:
 1. Add
 2. Subtract
 3. Multiply
 4. Divide
 5. Modulus""")

choice=input("Enter a choice:")
choice=int(choice)

if choice==1:
    number_one=input("Enter a number: ")
    number_two=input("Enter another number:")
    number_one=int(number_one)
    number_two=int(number_two)
    addition(number_one,number_two)
elif choice==2:
    number_one=input("Enter a number: ")
    number_two=input("Enter another number:")
    number_one=int(number_one)
    number_two=int(number_two)
    subtraction(number_one,number_two)
elif choice==3:
    number_one=input("Enter a number: ")
    number_two=input("Enter another number:")
    number_one=int(number_one)
    number_two=int(number_two)
    multiplication(number_one,number_two)
elif choice==4:
    number_one=input("Enter a number: ")
    number_two=input("Enter another number:")
    number_one=int(number_one)
    number_two=int(number_two)
    divison(number_one,number_two)
elif choice==5:
    number_one=input("Enter a number: ")
    number_two=input("Enter another number:")
    number_one=int(number_one)
    number_two=int(number_two)
    modulus(number_one,number_two)
else:
    print("Invalid choice.Try again")
