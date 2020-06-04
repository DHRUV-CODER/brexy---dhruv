a = int(input("Enter the first no: \n"))
b = int(input("Enter the second no: \n"))

if (a > b):
    min = a
else:
    min = b
while(1):
    if(min%a== 0 and min % b == 0):
        print("LCM id: \n", min)
        break
    min = min + 1
