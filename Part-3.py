side1 = float(input("Please enter side 1 : "))
side2 = float(input("Please enter side 2 : "))
side3 = float(input("Please enter side 3 : "))
if side1 >= (side2 + side3) or side2 >= (side1 + side3) or side3 >= (side1 + side2) or side1 <= 0 or side2 <= 0 or side3 <= 0 :
    flag = False
else :
    flag = True
print("Result that it means you can make rectangle or no is :",flag)