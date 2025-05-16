price = input("Regular price: ")
sale = input("Sale: ")
disc_price = float(price) * ((100 - float(sale)) / 100)

print("Your discounted price is " + str(disc_price))