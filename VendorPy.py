def Vendor():
        Ls1 = "\n"
        Ls2 = "\n\n"

        products = { 
        "A" : {"name": "coke" , "price": 20 },
        "B" : {"name": "fanta" , "price": 10 },
        "C" : {"name": "sprite" , "price": 25}
        }

        productDisplayToUser = 'A: Coke' + Ls1 + 'B: Fanta' + Ls1 + 'C: Sprite'
        print ( productDisplayToUser )

        while True:
                userSelection = input ( Ls2 + 'Please select a product' + Ls1 ).upper()
                price = int( products [ userSelection ] ["price"] )
                credit = 0

                while ( credit < price ):
                        credit = credit + ( int ( input ( Ls2 + "Please insert: R" + str ( price - credit ) + Ls1 ) ) )
                else:
                        print( Ls2 + "Your refund is: R" + str ( credit - price ) + " and your item has been dispatched." + Ls1 + "Would you like to buy another? .......... Y/N" )
                        reponse = input ()
                        if reponse == "n":
                                print( Ls2 +  "Thanks for shopping at Vendor. Have a great day!!!" )
                                exit()

Vendor()