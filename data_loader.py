import csv

def load_places_data(filename):
    data = {
        "States": {},  #Store cities by state
        "HousingCost": {},  #Storeshousing cost for each city
        "Climate": {}  #Store climate for each city
    }

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  #Skip the header row
            for row in reader:
                city_state = row[0].strip('"')  #Get city and state name
                climate = int(row[1])  #Get the climate score
                housing_cost = float(row[2])  #Get the housing cost

                city, state = city_state.rsplit(',', 1)  #Split into city and state

                if state not in data["States"]:
                    data["States"][state] = []  #Create an entry for the state if it doesn't exist
                data["States"][state].append(city)  #Add the city to the state's list

                data["HousingCost"][city_state] = housing_cost  #Store housing cost
                data["Climate"][city_state] = climate  #Store climate score
    except Exception as e:
        print(f"Error loading file: {e}")  #Print an error if there's one

    return data  #Return the loaded data
