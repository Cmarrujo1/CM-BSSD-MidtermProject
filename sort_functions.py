def find_closest_place(category, base_place, places_data):
    base_value = places_data[category].get(base_place)  #Get the value for housing cost or climate of the base city
    if base_value is None:
        return None  #Return None if the base city doesn't exist

    #Sort all the cities based on how close they are to the selected city
    sorted_places = sorted(
        places_data[category].items(),
        key=lambda x: abs(x[1] - base_value)  # ort by absolute difference from base city
    )

    #Return the first closest city
    for place, value in sorted_places:
        if place != base_place:
            return place, value, base_value  #Return the closest city, its value, and the base city's value
