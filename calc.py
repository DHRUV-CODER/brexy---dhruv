
print("operators uses:- ")
print(" for -ADDING press:-{+}")
print(" for - SUBTRACTING press:-{-}")
print(" for -  MULTIPLYING press :-(*}")
print(" for - DIVIDING press :-{/}")
print(" for - POWERS press :-(**} 'basically *SQAURING* ' ")

num1 = float(input("ENTER THE FIRST NUMBER = "))
op = input("ENTER THE OPERATOR : ")
num2 = float(input("ENTER THE SECOND NUMBER = "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "**":
    print(num1 ** num2)
else:
    print("invalid operator")

 
