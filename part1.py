


# part1.py

import json
from restaurant import Restaurant

def read_restaurants(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        restaurants = []
        for item in data:
            
            restaurants.append(Restaurant(item['business_id'],item["name"], item['address'],item['city'],item['state'],item['postal_code'],item['latitude'],item['longitude'],item['is_open'],item['categories'],item['hours']))
        return restaurants

def get_open(restaurants, day, time):
    return [restaurant for restaurant in restaurants if restaurant.check_open(day, time)]

def get_category(restaurants, category):
    return [restaurant for restaurant in restaurants if restaurant.is_category(category)]

#open at time in some of the categories
def filter_open_by_categories(restaurants, day, time, categories):
    open_restaurants = get_open(restaurants, day, time)
    return [restaurant for restaurant in open_restaurants if any(category in restaurant.categories for category in categories)]

def run_tests():
    restaurants = read_restaurants("restaurants.json")

    assert len(restaurants) > 0, "There should be some restaurants from the file"

    assert restaurants[0].name == "Abby Rappoport, LAC, CMQ"
    assert restaurants[0].state == "CA"
    assert restaurants[0].is_open == False
    
    open_restaurants = get_open(restaurants, 'Monday', '09:00')
    assert isinstance(open_restaurants, list), "get_open should return a list"

    open_restaurants = get_open(restaurants, 'Monday', '10:00')
    assert len(open_restaurants) > 1, "There should be one open restaurant"
    assert len(open_restaurants) > 1, "There should be more than one restaurant open"

    t_restaurants = get_open(restaurants, 'Monday', '18:00')
    assert len(t_restaurants) >1, "There should be more than 1 open restaurants"
    
    category_restaurants = get_category(restaurants, "Traditional Chinese Medicine")
    assert len(category_restaurants) > 1, "There should be many restaurants in the category restaurants"
    assert len(category_restaurants[0].name) > 1, "Restaurants in that category should be more than 1"

    assert len(get_open(restaurants, 'Monday', '08:00')) > 1, "Restaurants should be open at 08:00 on Monday"
    assert len(get_open(restaurants, 'Monday', '09:00')) > 1, "Restaurants should be open at 09:00 on Monday"
    assert len(get_open(restaurants, 'Monday', '12:00')) > 1, "Restaurants should be open at 12:00 on Monday"
    assert len(get_open(restaurants, 'Monday', '16:59')) > 1, "Restaurants should be open at 16:59 on Monday"
    assert len(get_open(restaurants, 'Monday', '17:01')) > 1, "Restaurants should be open at 17:01 on Monday"

    assert len(get_category(restaurants, "Fashion")) > 1, "More than 1 restaurant should be in Fashion category"
    assert len(get_category(restaurants, "Vietnamese")) > 1, "More than 1 restaurant should be in Vietnamese category"
    assert len(get_category(restaurants, 'Non-existent')) == 0, "No restaurant should be in Non-existent category"

    assert len(filter_open_by_categories(restaurants, 'Monday', '09:00', ["Fashion"])) > 0, "Fashion places on monday"

    len(filter_open_by_categories(restaurants, 'Friday', '09:00', ["Dark Web"])) == 0, "No dark web, no no!"

    len(filter_open_by_categories(restaurants, 'Monday', '00:00', ["Vietnamese"])) == 0, "No Vietnamese food on Monday midnight"

    print("All tests passed!")

    
if __name__ == "__main__":
    run_tests()
