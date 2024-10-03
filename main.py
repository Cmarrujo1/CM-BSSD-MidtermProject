#https://www.kaggle.com/datasets/sanjanchaudhari/places-dataset

from data_loader import load_places_data  #Import the function to load data from file
from sort_functions import find_closest_place  #Import the function to find the closest city


def get_valid_input(prompt, valid_options):
    user_input = input(prompt).strip()  #Ask user for input
    if user_input not in valid_options:
        raise ValueError(f"Invalid input! Choose from {valid_options}")  #Show error if input is invalid
    return user_input  #Return the valid input


def main():
    places_data = load_places_data('places.txt')  #Load the data from file

    try:
        available_states = list(places_data["States"].keys())  #Get all states from the data
        state = get_valid_input(f"Enter a state {available_states}: ", available_states)  #Ask for state

        available_cities = places_data["States"][state]  #Get cities in the selected state
        city = get_valid_input(f"Enter a city in {state} {available_cities}: ", available_cities)  #Ask for city

        category = get_valid_input("Select (HousingCost/Climate): ", ["HousingCost", "Climate"])  #Select category

        city_state = f"{city},{state}"  #Combines city and state
        closest_city, closest_value, base_value = find_closest_place(category, city_state,
                                                                     places_data)  #Find closest city

        if closest_city:
            #Print the result with a dollar sign if chosen HousingCost
            if category == "HousingCost":
                print(f"The housing cost of {city_state} is ${base_value:.2f}.")
                print(f"The closest city to {city_state} based on {category} is {closest_city}, ${closest_value:.2f}.")
            else:
                print(f"The climate score of {city_state} is {base_value}.")
                print(f"The closest city to {city_state} based on {category} is {closest_city}, {closest_value}.")
        else:
            print("No comparison found.")  #Print if there's no city to compare

    except ValueError as e:
        print(e)  #Show error
        print("Try again.")  #Ask the user to try again

    restart = get_valid_input("Would you like to try again? (yes/no): ", ["yes", "no"])  #Ask to restart
    if restart == "yes":
        main()  #Run the program again if they want to restart
    else:
        print("Goodbye!")  #Exit if they don't want to


if __name__ == "__main__":
    main()
