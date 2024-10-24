print("!!*******************************BASIC CALCULATOR****************************!!")
print("\n")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")
print("5. Remainder(modulous)")
print("6. Power")
ch='y'
while ch=='y':
    operation=int(input("\nChoose Operation to perform : "))
    if(operation==1):
        print("1. Addition ")
        n1=float(input("Enter 1st number : "))
        n2=float(input("Enter 2nd number : "))
        print("The Sum is : ",n1+n2)
        
    elif(operation==2):
        print("2. Subtraction ")
        n1=float(input("Enter 1st number : "))
        n2=float(input("Enter 2nd number : "))
        print("The Result is : ",n1-n2)
        
    elif(operation==3):
        print("3. Multiplication ")
        n1=float(input("Enter 1st number : "))
        n2=float(input("Enter 2nd number : "))
        print("The Product is : ",n1*n2)
        
    elif(operation==4):
        print("4. Division ")
        n1=float(input("Enter Dividend number : "))
        n2=float(input("Enter Divisor number : "))
        print("The Result is : ",n1/n2)
        
    elif(operation==5):
        print("5. Remainder ")
        n1=float(input("Enter Dividend number : "))
        n2=float(input("Enter Divisor number : "))
        print("The Remainder is : ",n1%n2)
        
    elif(operation==6):
        print("6. Power ")
        n1=float(input("Enter base number : "))
        n2=float(input("Enter power number : "))
        print("The Result is : ",n1**n2)
        
    else:
        print("Invalid Choice of Operation! TRY OR Start Again")
    ch=input("\nDo you want to continue : enter y(for yes)/n(for no) : ")
print("THANKS FOR USING!")