"""
Coffee Shop Simulator

This program simulates a coffee and muffin shop where the user can input the number of coffees 
and muffins they wish to purchase. The program calculates the subtotal, applies a 6% tax, 
and displays a formatted receipt.

Prices:
- Coffee: $5.00 each
- Muffin: $4.00 each
- Tax: 6% of the subtotal

Vicente Miranda Leon
October 3rd, 2024
"""


COFFEE_PRICE = 5.00
MUFFIN_PRICE = 4.00
TAX_RATE = 0.06

def main():
    
    print("***************************************")
    print("My Coffee and Muffin Shop")

    
    num_coffees = int(input("Number of coffees bought? "))
    num_muffins = int(input("Number of muffins bought? "))

    
    subtotal_coffees = num_coffees * COFFEE_PRICE
    subtotal_muffins = num_muffins * MUFFIN_PRICE
    subtotal = subtotal_coffees + subtotal_muffins

    
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{num_coffees} Coffee at ${COFFEE_PRICE:.2f} each: $ {subtotal_coffees:.2f}")
    print(f"{num_muffins} Muffins at ${MUFFIN_PRICE:.2f} each: $ {subtotal_muffins:.2f}")
    print(f"6% tax: $ {tax:.2f}")
    print("---------")
    print(f"Total: $ {total:.2f}")
    print("***************************************")


if __name__ == "__main__":
    main()
