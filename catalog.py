def menu():
    # Prices for individual items
    fried_chicken_price = 82.00
    fries_price = 50.00
    burger_price = 40.00
    coke_price = 53.00

    # Prices for combo meals with a 10% discount
    combo_one_price = (fried_chicken_price + fries_price) * 0.90
    combo_two_price = (fries_price + burger_price) * 0.90
    combo_three_price = (fried_chicken_price + burger_price) * 0.90

    # Price for the gift pack with a 25% discount
    gift_pack_price = (fried_chicken_price + fries_price + burger_price + coke_price) * 0.75

    # Print catalog header
    print(" ")
    print("Kyu's Restaurant")
    print("--------------------------------------------------------------")
    print("Product(s)                                           Price")

    # Print individual item prices
    print("Fried Chicken                                         ", fried_chicken_price)
    print("Fries                                                 ", fries_price)
    print("Burger                                                ", burger_price)
    print("Coke                                                  ", coke_price)

    # Print combo meal prices and descriptions
    print("Combo Meal One                                        ", combo_one_price)
    print("     (Fried Chicken and Fries)")
    print("Combo Meal Two                                        ", combo_two_price)
    print("     (Fries and Burger)")
    print("Combo Meal Three                                      ", combo_three_price)
    print("     (Fried Chicken and Burger)")

    # Print gift pack price and description
    print("Gift Pack                                             ", gift_pack_price)
    print("     (Fried Chicken, Fries, Burger and Coke)")

    # Print catalog footer
    print("—————————————————————————————————————————————————————————————")
    print("visit kyusrestaurantdelivery.com for deliveries!")
    print(" ")


while True:
    print("Hello! Welcome to Kyu's Restaurant!")
    input("Please Enter to Continue... \n " )

    options = input("Do you want to see the menu? \n yes \n no \n ")
    if options.lower() in ['yes', 'y']:
        menu()
    elif options.lower() in ['no', 'n']:
        print("Okay! Have a good day!")
        break
    else:
        print("I don't understand")

    exit_choice = input("Do you want to exit? \n yes \n no \n ")
    if exit_choice.lower() in ['yes', 'y'] :
        break
