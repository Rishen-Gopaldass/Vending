
def Vendor():

    products = { 
    "A" : {"name": "coke" , "price": 20 },
    "B" : {"name": "fanta" , "price": 10 },
    "C" : {"name": "sprite" , "price": 25}  }
    print (products)

    while True:
        selection = input ( "\nEnter a product:\n").upper()
        price = int(products[selection]["price"])
        credit = 0

        while (credit < price):
            credit = credit + (int(input("Please insert: R" + str(price - credit)+ "\n\n")))
        else:
            print( "Your refund is: R" + str(credit - price) +  "\n and your item has been dispatched. \n\nBuy something else?      y/n")
            reponse = input()
            if reponse == "n":
                print("Thanks for shopping at Vendor. Have a great day!!!")
                exit()

Vendor()
