def calculate_total():
    #we are setting the prices in this section 
    coffee_price = 5.00
    muffin_price = 4.00
    tax_rate = 0.06
    
    #User inputs numbers here
    print("****************************")
    print("My Coffee and Muffin Shop")
    num_coffees = int(input("Enter the number of coffees: "))
    num_muffins = int(input("Enter the number of muffins: "))
    print("****************************")

    #calculate subtotal
    subtotal_coffees = num_coffees * coffee_price
    subtotal_muffins = num_muffins * muffin_price
    subtotal = subtotal_coffees + subtotal_muffins

    #tax calculation
    tax = subtotal * tax_rate

    #total calculation
    total = subtotal + tax

#display receipt
    print("My Coffee and Muffin Shop Receipt")
    print(f"{num_coffees} Coffee at ${coffee_price} each: ${subtotal_coffees:.2f}")
    print(f"{num_muffins} Muffins at ${muffin_price} each: ${subtotal_muffins:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("***************************************")

#run program
    calculate_total
