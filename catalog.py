def catalog():
    item1_price = 200.0
    item2_price = 150.0
    item3_price = 300.0
    combo1_price = item1_price + item2_price - 0.1*(item1_price + item2_price)
    combo2_price = item2_price + item3_price - 0.1*(item2_price + item3_price)
    combo3_price = item1_price + item3_price - 0.1*(item1_price + item3_price)
    gift_pack_price = item1_price + item2_price + item3_price - 0.25*(item1_price + item2_price + item3_price)

    print("Online Store")
    print("--------------------------------------")
    print("Product(s)                                                   Price")    
    print(f"Item 1                                                       {item1_price}")
    print(f"Item 2                                                       {item2_price}")
    print(f"Item 3                                                       {item3_price}")
    print(f"Combo 1 (Item 1 + 2)                                         {combo1_price}")
    print(f"Combo 2 (Item 2 + 3)                                         {combo2_price}")
    print(f"Combo 3 (Item 1 + 3)                                         {combo3_price}")
    print(f"Combo 4 (Item 1 + 2 + 3)                                     {gift_pack_price}")
    print("——————————————————————————————————————")
    print("For delivery contact: 98764678899")
