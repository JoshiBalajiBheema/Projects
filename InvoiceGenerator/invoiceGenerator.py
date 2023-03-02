# Press 'c' to exit the program any time.
print('                     *** WELCOME TO OUR STORE. ***                     ')
print("[ Please press 'c', after you add all the items to the cart.]")


def check_int():
    total = 0
    x = []
    while True:
        Product_Entry = input("Enter the Price : ")
        if Product_Entry != "c":
            total += int(Product_Entry)
            x.append(Product_Entry)

        else:
            print("--*****  THE STORE  *****--")
            print('Number of items :', len(x))
            print('Price per item :', x)
            print(f'Total Amount of the CART : Rs. {total}')
            discount_value = int(input("Enter percentage of Discount : "))
            if discount_value >= 50:
                discount_value = 50
            else:
                discount_value = discount_value
            discounted_price = (total * (discount_value / 100))
            final_discount = total - discounted_price
            print('YOU SAVED {}% on your Purchase, which is Rs. {}'.format(discount_value, discounted_price))
            print(f'Total Amount Payable, AFTER DISCOUNT is : Rs. {final_discount}')
            print('Thanks for visiting, have a GREAT day.')

            break


if __name__ == "__main__":
    check_int()

