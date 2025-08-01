a = int(input("Enter the year :"))
if a % 4 == 1:
    if (a+3) % 100 == 0:
        if (a+3) % 400 == 0:
            print("The coming leap year is :",a+3)
        else:
            print("The coming leap year is :",a+7)
    else:
        print("The coming leap year is :",a+3) 
            
     
elif a % 4 == 2:
    if (a+2) % 100 == 0:
        if (a+2) % 400 == 0:
            print("The coming leap year is :",a+2)
        else:
            print("The coming leap year is :",a+6)
    else:
        print("The coming leap year is :",a+2)  

    
elif a % 4 == 3:
    if (a+1) % 100 == 0:
        if (a+1) % 400 == 0:
            print("The coming leap year is :",a+1)
        else:
            print("The coming leap year is :",a+5)
    else:
        print("The coming leap year is :",a+1)  

    


elif a % 4 == 0:
    if (a+4) % 100 == 0:
        if (a+4) % 400 == 0:
            print("The coming leap year is :",a+4)
        else:
            print("The coming leap year is :",a+8)   
    else:
        print("The coming leap year is :",a+4)
        

    