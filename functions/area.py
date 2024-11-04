
def area():
    
    length=float(input("enter the length\t"))
    width_in=input("Enter the width  \t")

    if width_in=="":
        width=length
    
    else:
        width=float(width_in)

    return(length*width)

print("The area is ",area())