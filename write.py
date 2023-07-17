import datetime

time = datetime.datetime.now()
year = str(time.year)
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
sec = str(time.second)

def print_bill_sold(name, phone, laptops_sold,delivery_cost, employee_name):
    """
        print_bill_sold function is for priting bill after sales of laptop/s
        when called it takes few paramters and prints the bill
        the bill is printed in both terminal and a unique file is also created
    """
    print("\n")
    print("\t  GadgetBit Technologies")
    print("\n")
    print("\t9807654321, Kamalpokhari, KTM")
    print("\t\t **Sales Bill**")
    print("------------------------------------------")
    print("Name : " + name )
    print("\n")
    print("Phone : " + phone)
    print("------------------------------------------")
    print("Sold by : " + employee_name)
    print("Date : " + year + "/" + month + "/" + day)
    print("Time : "+ hour + ":" + minute + ":" + sec)
    Grandtotal = 0
    print("------------------------------------------")
    print("MODEL\t   QUANTITY\tAMOUNT\t TOTAL")
    print("------------------------------------------")
    for i in laptops_sold:
        print(i[0] + "\t\t" + str(i[1]) + "\t" + str(i[2] + "\t $" + str(i[3])))
        Grandtotal += int(i[3]) 
    print("------------------------------------------")
    print("Sub total \t\t\t$" + str(Grandtotal))
    print("Shipment cost \t\t\t$" + str(delivery_cost))   
    
    print("------------------------------------------")
    print("Grand Total \t\t\t$" + str(Grandtotal + delivery_cost))
    print("------------------------------------------")

    file = open("Sold_to_" + name + "_" + year + month + day + hour + minute + sec + ".txt","w")
    file.write("\n")
    file.write("\t  GadgetBit Technologies")
    file.write("\n")
    file.write("\t9807654321,Kamalpokhari,KTM\n")
    file.write("\t\t **Sales Bill**\n")
    file.write("--------------------------------------------")
    file.write("\n")
    file.write("Name : " + name)
    file.write("\n")
    file.write("Phone : " + phone)
    file.write("\n")
    file.write("---------------------------------------------\n")
    file.write("Sold by : " + employee_name +"\n")
    file.write("Date : " + year + "/" + month + "/" + day + "\n")
    file.write("Time : "+ hour + ":" + minute + ":" + sec + "\n")
    file.write("---------------------------------------------\n")
    Grandtotal = 0
    file.write("MODEL\t   QUANTITY\tAMOUNT\t TOTAL\n")
    file.write("\n")
    for i in laptops_sold:
        file.write(i[0] + "\t\t" + str(i[1]) + "\t" + str(i[2] + "\t $" + str(i[3]) + "\n"))
        Grandtotal += int(i[3])

    file.write("----------------------------------------------\n")
    file.write("Sub total    \t\t\t$" + str(Grandtotal) + "\n")
    file.write("Shipment cost \t\t\t$" + str(delivery_cost) + "\n")   
    
    file.write("----------------------------------------------\n")
    file.write("Grand Total \t\t\t$" + str(Grandtotal+delivery_cost) + "\n")
    file.write("----------------------------------------------\n")
    file.close()


def print_bill_purchased(laptops_bought, vat, employee_name,laptop_dealer):
    """
        print_bill_purchased function is for priting bill after purchase of laptop/s
        when called it takes few paramters and prints the bill
        the bill is printed in both terminal and a unique file is also created
    """
    print("\n")
    print("\t  GadgetBit Technologies")
    print("\n")
    print("\t9807654321, Kamalpokhari, KTM")
    print("\t\t**Purchase Bill**")
    print("------------------------------------------")
    print("Bought by  : " + employee_name)
    print("Bought from : " + laptop_dealer)
    print("Date : " + year + "/" + month + "/" + day)
    print("Time : " + hour + ":" + minute + ":" + sec)
    print("------------------------------------------")
    Grandtotal = 0
    print("MODEL\t   QUANTITY\tAMOUNT\t TOTAL")
    print("------------------------------------------")
    for i in laptops_bought:
        print(i[0] + "\t\t" + str(i[1]) + "\t" + str(i[2] + "\t " + str(i[3])))
        Grandtotal += int(i[3]) 

    vatamount = Grandtotal * vat 

    print("------------------------------------------")
    print("Sub total\t\t\t$" + str(Grandtotal))
    print("VAT\t\t\t\t13%")
    print("VAT amount \t\t\t$" + str( vatamount))  
    print("------------------------------------------")
    print("Grand Total\t\t\t$"+ str(Grandtotal+vatamount))
    print("------------------------------------------")



    file = open("purchased_by_"+employee_name+"_"+year+month+day+hour+minute+sec+".txt","w")
    file.write("\n")
    file.write("\t  GadgetBit Technologies")
    file.write("\n")
    file.write("\t9807654321, Kamalpokhari, KTM\n")
    file.write("\t\t**Purchase Bill**\n")
    file.write("------------------------------------------\n")
    file.write("Bought by  : " + employee_name + "\n")
    file.write("Bought from : " + laptop_dealer +"\n")
    file.write("Date : " + year + "/" + month + "/" + day + "\n")
    file.write("Time : " + hour + ":" + minute + ":" + sec + "\n")
    file.write("------------------------------------------\n")
    Grandtotal = 0
    file.write("MODEL\t   QUANTITY\tAMOUNT\t TOTAL\n")
    print("------------------------------------------")
    file.write("\n")
    for i in laptops_bought:
        file.write(i[0] + "\t\t" + str(i[1]) + "\t" + str(i[2] + "\t " + str(i[3]) + "\n"))
        Grandtotal += int(i[3]) 
    file.write("------------------------------------------\n")
    file.write("Sub total\t\t\t$" + str(Grandtotal) + "\n")
    vatamount = Grandtotal * vat 
    file.write("VAT \t\t\t\t13%\n")   
    file.write("VAT amount \t\t\t$" + str(vatamount) + "\n")  
    file.write("------------------------------------------\n")
    file.write("Grand Total\t\t\t$" + str(Grandtotal+vatamount) +"\n")
    file.write("------------------------------------------\n")
    file.close()
    