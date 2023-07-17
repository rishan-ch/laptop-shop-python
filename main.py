# importing modules with specific roles for easier programming
import operations, read , write

print("\n")
print("\t\t\t\t\t  GadgetBit Technologies")
print("\n")
print("\t\t\t\t\t9807654321, Kamalpokhari, KTM")
print("\n")
print("-----------------------------------------------------------------------------------------------------------------")
print("\n")
print("------------------------------------------------ Welcome --------------------------------------------------------")
print("\n")
print("\n")

def main():
    """
        main()method is where all the logic takes place
        this module imports operations, read and write modules 
    """

    # main loop which will be continued after every purchase or sell and only exits when instructed to 
    loop = True
    while loop:
        print("What operations do you want to continue?(BUY/SELL/EXIT)")
        print("\n")
        print("*SELL - Sell laptops to customer*")
        print("*BUY - Buy laptops from mdealer*")
        print("*EXIT - Exit the system*")
        print("\n")
        activity = input("Your input : ").upper()

        if activity == "SELL":
            # selling laptops to customers
            laptops_sold = []
                
            # prints every laptops and information available in the laptop.txt file
            read.table()

            # customer name and phone number for bill generation
            print("\n")
            fname = input("Enter customer's first name : ").capitalize()
            while not fname.isalpha():
                print("\n")
                print("Please enter valid name")
                print("\n")
                fname = input("Enter customer's first name : ").capitalize()
                print("\n")

            lname = input("Enter customer's last name : ").capitalize()
            while not lname.isalpha():
                print("\n")
                print("Please enter valid name")
                print("\n")
                lname = input("Enter customer's last name : ").capitalize()
                print("\n")
            name = fname + " " + lname
            print("\n")
                
            Try = False
            while not Try:
                try:
                    phone = int(input("Enter phone number : "))
                    phone = str(phone)
                    print("\n")

                    if len(phone) == 10:
                        Try = True
                    else:
                        print("Enter valid phone number")
                        print("\n")
                        Try = False

                except ValueError:
                    print("\n")
                    print("Invalid phone number")
                    print("\n")
            
            #loop incase multiple laptops are to sold
            add_items = "Yes"
            while  add_items == "Yes":
                #empty dictionary to store the value of another module
                overall_laptops = {}
                overall_laptops = read.read_file()
                valid_laptopid = len(overall_laptops)

                # validating laptop id and quantity entered by the user
                quantity_available = True
                while quantity_available:
                    laptopID = operations.id_validation(valid_laptopid)

                    #if laptop is out of stock the programs goes into unexitable loop
                    available_quantity = int(overall_laptops[laptopID][3])

                    if available_quantity == 0:
                        print("\t\tLaptop is out of stock")
                        print("\n")
                    else:
                        break
                    
                quantity = operations.quantity_validation(available_quantity)
                    
                # assigning sale information to variables 
                laptop_name = overall_laptops[laptopID][0]
                quantity_sold = quantity
                price_per_unit = overall_laptops[laptopID][2]
                price_of_unit = price_per_unit.replace("$","")
                total_price = int(price_of_unit) * quantity_sold

                # Storing above vaiables in a list incase the customer wants to add more items
                laptops_sold.append([laptop_name, quantity_sold, price_per_unit,total_price])

                # deducting quantity from laptop.txt
                activity = "deduct"
                operations.quantity_update(laptopID,quantity, available_quantity,overall_laptops, activity)
                
                # if customers wants to buy more laptops
                add_items_condition = False
                while not add_items_condition:

                    add_items = input("Do you want to add items?(Yes/No) : ").capitalize()
                    print("\n")
                    if add_items == "Yes" or add_items == "No":
                        
                        add_items_condition = True
                        break
                    else:
                        print("Please check the data you are entering")
                    print("\n")

                if add_items == "Yes":
                    read.table()
                    #prints the available stock once again
                else:
                    break
                
            # delivery cost is constant 
            delivery_condition = False
            while not delivery_condition:

                delivery = input("Do you want yout item/s to be delivered? (Yes/No)").capitalize()
                print("\n")
                if delivery == "Yes" or delivery == "No":
                    delivery_condition = True
                    break
                else:
                    print("Please check the data you are entering")
                    print("\n")
            
            delivery_cost=0
            print("\n")

            if delivery =="Yes":
                delivery_cost = 100

            #get employee's name
            employee_id = operations.employee_id()
            if employee_id == 1:
                employee_name = "Shreyash Ghale"
            elif employee_id == 2:
                employee_name = "Swagat Gautam"

            # generate bill
            write.print_bill_sold(name, phone, laptops_sold, delivery_cost, employee_name)
            print("\n")
            print("\n")

        elif activity == "BUY":
            
            #to buy laptops from dealershop
            laptops_bought=[]
            add_items = "Yes"
            read.table()

            laptop_dealer = input("Enter the name of Manufacturer/Dealer shop : ").capitalize()
            while not laptop_dealer.isalpha():
                print("\n")
                print("Please enter valid name")
                print("\n")
                laptop_dealer = input("Enter the name of dealer shop : ").capitalize()
                print("\n")

            while add_items== "Yes":
                overall_laptops = read.read_file()
                valid_laptopid = len(overall_laptops)
                Try = False
                while not Try:
                    try:
                        laptopID = operations.id_validation(valid_laptopid)
                        print("\n")
                        
                        Try = True
                    except ValueError:
                        print("\n")
                        print("Invalid input detected")
                        print("\n")

                valid_quantity = False
                while not valid_quantity:
                    try:
                        quantity = int(input("How many units do you want to buy? : "))
                        print("\n")
                        valid_quantity = True
                        while quantity<=0:
                            print("\n")
                            quantity = int(input("how many units do you want to buy? : "))
                            print("\n")
                    except ValueError:
                        print("\n")
                        print("Invalid input detected")
                        print("\n")
                
                available_quantity = int(read.read_file()[laptopID][3])
                
                    
                # assigning purchase information to variables 
                laptop_name = overall_laptops[laptopID][0]
                quantity_bought = quantity
                price_per_unit = overall_laptops[laptopID][2]
                price_of_unit = price_per_unit.replace("$","")
                total_price = int(price_of_unit) * quantity_bought

                # Storing above vaiables in a list incase the customer wants to add more items
                laptops_bought.append([laptop_name, quantity_bought, price_per_unit,total_price])

                # adding quantity to laptop.txt
                activity = "Add"
                operations.quantity_update(laptopID,quantity, available_quantity,overall_laptops,activity)
                

                # if more laptops is to be bought
                add_items_condition = False
                while not add_items_condition:
                    add_items = input("Do you want to add items?(Yes/No) : ").capitalize()
                    print("\n")
                    if add_items == "Yes" or add_items == "No":

                        add_items_condition = True
                        break
                    else:
                        print("Please check the data you are entering")
                        print("\n")

                print("\n")


                if add_items == "Yes":
                    read.table()
                elif add_items == "No":
                    employee_id = operations.employee_id()
                    if employee_id == 1:
                        employee_name = "Shreyash Ghale"
                    elif employee_id == 2:
                        employee_name = "Swagat Gautam"
                    vat = 0.13
                    print("\n")
                    write.print_bill_purchased(laptops_bought, vat, employee_name, laptop_dealer)
                    print("\n")
                    break
            
        elif activity == "EXIT":
            loop = False
            print("\n")
            print("\n")
            print("---------------------------------Have a great day-------------------------------------")

        # incase any invalid data is entered
        else:
            print("\n")
            print("Enter valid operation")
            print("\n")
main()


