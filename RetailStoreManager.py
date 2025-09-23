#This will be a script where you can manage or add specific items or change values to a stores stock

# btw this is unrelated to the PreWork I just wanted to code something ᕦ(⩾﹏⩽)ᕥ


# for some reason tabulate defining doesn't work in the repository (I promise you it worked completely fine before) I'm not sure what changed but it doesn't work at all now...
# I actually have no idea why... D: so the table formatting of it when its printed looks.. really crappy to be honest but atleast it works! ٩(◕‿◕)۶


#from tabulate import tabulate



RetailStock = [
    ["Apples", 2.50, 100],
    ["Oranges", 1.50, 100],
    ["Water", 1.99, 75],
    ["LotteryTicket", 9.99, 50],
    ["PizzaSlice", 2.99, 40]
]

StockFormat = ("Product", "Price", "Stock") #Format for which the Stock table will be displayed in


def StockViewingFunction():
    print("Welcome to the stock viewer menu Here is your stock displayed")
    print(RetailStock, StockFormat, "\n")
    print("Now going back to MainMenu")
    MainMenu()


def RemoveStockOrAddStock():
    print("Welcome to the Remove Stock Or Add Stock Menu. Choose a option below \n AddStock \n RemoveStock \n MainMenu")
    UserInput = input()
    if UserInput != "AddStock" and UserInput != "RemoveStock" and UserInput != "MainMenu":
        print("Try again you need to spell them correctly they are case sensetive")
        RemoveStockOrAddStock()

    elif UserInput == "AddStock":
        IndexesOfTable = 5
        NextIndexNumber = IndexesOfTable + 1
        print("Alright first type in your item name")
        StockName = input()
        print("Alright now type in your price")
        PriceInput = input()
        print("Okay great now type in how much we have in stock!")
        StockInput = input()
        LuhFormatted = [StockName, PriceInput, StockInput]
        print("okay it has been inserted! going back to MainMenu")
        RetailStock.insert(NextIndexNumber ,LuhFormatted)
        MainMenu()


    elif UserInput == "RemoveStock":
        print("Alright type in the name of the stock you'd like to delete here are all the stock items")
        print(tabulate (RetailStock, StockFormat, tablefmt = "grid"))
        StockChoice = input()

        ItemFound = False

        for Item in RetailStock:
            if StockChoice == Item[0]:
                RetailStock.remove(Item)
                print(f"{Item[0]} has been successfully removed returning to MainMenu")
                MainMenu()
                ItemFound = True

        if ItemFound == False:
            print("Item was not found going back to main menu")
            MainMenu()

    elif UserInput == "MainMenu":
        print("Going back to main menu no changes made.")
        MainMenu()




def MainMenu():
    print("\n Welcome to the Retail Store Stock management System! Where would you like to go? \n ViewStock \n RemoveOrAddStock \n Quit")
    UserInput = input()
    if UserInput != "ViewStock" and UserInput != "RemoveOrAddStock" and UserInput != "Quit":
        print("Try again you need to type it exactly how its spelt its case sensetive")
        MainMenu()
    elif UserInput == "ViewStock":
        StockViewingFunction()
    elif UserInput == "RemoveOrAddStock":
        RemoveStockOrAddStock()
    elif UserInput == "Quit":
        print("Alright no worries have a good rest of your day!")

MainMenu()