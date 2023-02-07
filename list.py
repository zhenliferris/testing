# practice list

print("Welcome to my real estate average price calculator!")
neighborhood = input("Enter the neighborhood name: ")
price_list = [0]
house_count_adding = "y"
while house_count_adding.lower() != "n":
    house_count_adding = input(
        "Would you like to add the price of one more house? (y/n): ")
    if house_count_adding.lower() == "y":
        price_list.append(input("Enter house price: "))
    elif house_count_adding.lower() != "n":
        print("please enter y/n")
del price_list[0]

total_price = 0
number_of_house = len(price_list)
for x in price_list:
    unit_price = float(x)
    total_price += unit_price
try:
    average_price = total_price / number_of_house
except ZeroDivisionError:
    average_price = 0


print("The average house price in the",
      neighborhood, "nighborhood is", average_price)
