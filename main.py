sum = 0 
while(True):
    number = input("enter the number")
    if(number!='q'):
        sum = sum + int(number)
        print(f"order total so far: {sum}")
    else:
        print(f"your total bill is {sum},Thank you for shopping with us ")
        break
    
    