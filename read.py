# module to read the file's information


def read_file():
    """
        this function reads the laptop.txt file and 
        stores the information in a dictionary stock
        whenever its called it returns details of laptop.txt in a dictionary
    """
    stock_file = open("laptop.txt", "r")
    stock = {}
    laptopID = 1

    for i in stock_file:
        i = i.replace("\n", "")
        stock.update({laptopID: i.split(",")})
        laptopID += 1
    stock_file.close()
    return stock



def table():
    """
        this function prints the informations of laptop.txt 
        whenever called, it prints the laptops vailable in laptop.txt in a tabular format
    """
    print("\n")
    print("ID\tMODEL\t\tBRAND\t\tPRICE\t\tUNITS\t\tCPU\t\tRAM\t\tGPU")
    print("-----------------------------------------------------------------------------------------------------------------")
    stock_file = open("laptop.txt", "r")
    i = 1
    for j in stock_file:
        print(i, "\t" + j.replace(",", "\t\t"))
        i += 1
    stock_file.close()
    


