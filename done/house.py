import csv

line_count = 0
max_price = 0.0
average_price = 0.0
sq_feet, num_bedrooms, num_bathrooms, sale_price = [], [], [], []

# read the csv file and put data into the 4 lists, set line count
with open('house_data.csv') as house_file:
    house_data = csv.reader(house_file, delimiter=',')
    for row in house_data:
        sq_feet.append(row[0])
        num_bedrooms.append(row[1])
        num_bathrooms.append(row[2])
        sale_price.append(row[3])
        line_count += 1

# convert the string to float values for calculations
# remove the title from the data structure
num_bedrooms_f = [float(x) for x in num_bedrooms[1:]]
num_bathrooms_f = [float(x) for x in num_bathrooms[1:]]
sq_feet_f = [float(x) for x in sq_feet[1:]]
sale_price_f = [float(x) for x in sale_price[1:]]
data_line_count = line_count - 1

# get the max price and average price ready for the whole list
for order in range(data_line_count):
    if max_price < sale_price_f[order]:
        max_price = sale_price_f[order]
    average_price += sale_price_f[order]
average_price = average_price / data_line_count if data_line_count != 0 else 0

# define a function to print user chooices for operations


def select_list():
    print(
        "1 for exact\n"
        "2 for greater than or equal\n"
        "3 for less than or equal\n"
    )


# define function for exact comparison
def exact(feature, user_choice, house_feature):
    feature_price, count = 0, 0
    for i in range(len(house_feature)):
        if float(user_choice) == house_feature[i]:
            feature_price += sale_price_f[i]
            count += 1

    print(
        "there are", count, "House has", feature, "of ", user_choice,
        " with average_price of ", feature_price/count if count != 0 else 0
    )


# define function for greater than or equal to
def greater(feature, user_choice, house_feature):
    feature_price, count = 0, 0
    for i in range(len(house_feature)):
        if float(user_choice) <= house_feature[i]:
            feature_price += sale_price_f[i]
            count += 1

    print(
        "there are", count, "House has ", feature, "of more than or equal to", user_choice,
        " with average_price of ", feature_price/count if count != 0 else 0
    )


# define function for less than or equal to
def less(feature, user_choice, house_feature):
    feature_price, count = 0, 0
    for i in range(len(house_feature)):
        if float(user_choice) >= house_feature[i]:
            feature_price += sale_price_f[i]
            count += 1

    print(
        "there are", count, "House has ", feature, "of less than or equal to", user_choice,
        " with average_price of ", feature_price/count if count != 0 else 0
    )


# define a function for if the user choose size to research
def size():
    size_choice = input("Choose size of house : ")
    select_list()
    size_calculations = input(">>")
    feature_price, count = 0, 0

    if size_calculations == "1":
        exact("size", size_choice, sq_feet_f)

    if size_calculations == "2":
        greater("size", size_choice, sq_feet_f)

    if size_calculations == "3":
        less("size", size_choice, sq_feet_f)

# define a function to calculate the bedrooms data


def bedrooms():
    bed_choice = input("Choose a number of bedrooms: ")
    select_list()
    bed_calculations = input(">>")
    bed_price, count = 0, 0

    if bed_calculations == "1":
        exact("bedrooms", bed_choice, num_bedrooms_f)

    if bed_calculations == "2":
        greater("bedrooms", bed_choice, num_bedrooms_f)

    if bed_calculations == "3":
        less("bedrooms", bed_choice, num_bedrooms_f)

# define a function to calculate the bathrooms data


def bathrooms():
    bath_choice = input("Choose a number of bathrooms: ")
    select_list()
    bath_calculations = input(">>")
    bath_price, count = 0, 0

    if bath_calculations == "1":
        exact("bathrooms", bath_choice, num_bathrooms_f)

    if bath_calculations == "2":
        greater("bathrooms", bath_choice, num_bathrooms_f)

    if bath_calculations == "3":
        less("bathrooms", bath_choice, num_bathrooms_f)


# Welcome screen
print("Welcome to the House price dataset analyzer!\n"
      "The dataset contains data for", data_line_count, "House price data.\n"
      "The maximum price is", max_price,
      "and the average price is", average_price)

# main function for user menu
user_choice = "y"
while user_choice.lower() != "n":
    if user_choice.lower() == "y":
        # menu choice"
        print(
            "Choose an attribute!\n 1 for size of square foot\n 2 for bedrooms\n 3 for number of bathrooms\n")
        attribute_choice = input(">")
        if attribute_choice == "1":
            size()
        elif attribute_choice == "2":
            bedrooms()
        elif attribute_choice == "3":
            bathrooms()
        else:
            print("Wrong Attribute!!")
    user_choice = input("\nDo the research again? (y/n)")
