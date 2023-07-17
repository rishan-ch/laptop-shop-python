


def id_validation(valid_laptopid):
    """
        id_validation method takes valid_laptopid
        it is the total length of our dictionary
        when this method is called it asks user for laptop id
        returns the laptop id only if it is valid
        else it keeps on the loop
    """
    loop = True
    while loop:
        try:
            laptopID = int(input("Enter laptop ID : "))
            print("\n")
            while laptopID<=0 or laptopID>valid_laptopid:
                print("\n")
                print("Recheck the value and enter again")
                print("\n")
                laptopID = int(input("Enter laptop ID : "))
                print("\n")
            break
        except ValueError:
            print("\n")
            print("Enter valid data")
            print("\n")
    return laptopID


def quantity_validation(available_quantity):
    """
        quantity_validation method takes available_quantity
        it is the total quantity of our laptop in dictionary
        when this method is called it asks user for quantity
        returns the quantity only if it is valid
        else it keeps on the loop
    """
    loop = True
    while loop:
        try:
            quantity = int(input("Enter units of laptop to be sold : "))
            print("\n")
            while quantity <= 0 or quantity > available_quantity:
                print("invalid quantity")
                print("\n")
                quantity = int(input("Enter the quantity of Laptop to be sold : "))
                print("\n")
            break
        except ValueError:
            print("\n")
            print("Enter valid data")
            print("\n")
    return quantity

def quantity_update(laptopID,quantity, available_quantity,overall_laptops,activity):
    """
        quantity_update function is for adding or deducting quantity after every sales and purchases
        this method rewrites the whole laptop.txt with updated dictionary
    """
    if activity == "Add":
        updated_quantity = available_quantity + quantity
    else:
        updated_quantity = available_quantity - quantity
     
    Dict = overall_laptops
    Dict[laptopID][3] = updated_quantity

    file = open("laptop.txt", "w")
    for values in Dict.values():
        file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + ","
        + str(values[4]) + "," + str(values[5])+ "," + str(values[6]))
        file.write("\n")
    file.close()    

def employee_id():
    """
        employee_id function for getting employee's id
        with the id the name of the employee will be printed in the bill
    """
    print("---------------------------Select your name----------------------------")
    print("1 - Shreyash Ghale")
    print("2 - Swagat Gautam")
    print("\n")
    
    valid_employee_id = False
    while not valid_employee_id:
        try:
            employee_id = int(input("Enter the code for your name : "))

            while employee_id in [1, 2]:
                valid_employee_id = True
                break

        except ValueError:
            print("\n")
            print("Please enter the numeric value corresponding to your name.")
            print("\n")
    return employee_id
