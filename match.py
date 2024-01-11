# this is match case tutorial, !! very much similar to switch

x = int(input("Enter x : "))

match x:
    case 1:
        print("match the number x 1")
    
    case 2:
        print("case is 2")
    case 3:
        print("case is 3")
    case 4:
        print("case is 4")
    case 5:
        print("case is 5")
    case _: 
        print("not found")
        