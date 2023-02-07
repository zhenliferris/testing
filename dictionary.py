# dictionary practice with the state information
# dictionary
# state_capitals_Population = {"michigan": ["Lansing", 112644],
#                              "alabama": ["Montgomery", 200603],
#                              "alaska": ["Juneau", 32255],
#                              "arizona": ["Phoenix", 1608139],
#                              "arkansas": ["Little Rock", 202591],
#                              "aalifornia": ["Sacramento", 524943],
#                              "colorado":	["Denver", 715522]
#                              }
state_capitals_population = dict(michigan=["Lansing", 112644],
                                 alabama=["Montgomery", 200603],
                                 alaska=["Juneau", 32255],
                                 arizona=["Phoenix", 1608139])
# add new entry
state_capitals_population["florida"] = ["Tallahassee", 196169]

print("welcome to state information system!")
user_choice = "y"
while user_choice.lower() != "n":
    if user_choice.lower() == "y":
        # menu choice"

        print(
            "Please input the name of the state: ")
        state_name = input(">")
        if state_name.lower() in state_capitals_population:
            search_item = input("1 for capital 2 for population:")
            if search_item == "1":
                captal_name = state_capitals_population[state_name.lower()][0]
                print("the capital of " + state_name + " is " + captal_name)
            elif search_item == "2":
                population = state_capitals_population[state_name.lower()][1]
                print("the population of " + state_name + " is ", population)
            else:
                print("Wrong Attribute")
        else:
            print("No state information exist!!")
    user_choice = input("Check again? (y/n)")
