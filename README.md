# To add a new country
## Must have a district_coords_dict.json!
TODO: Populate here with information about how to create this dictionary.
## Adding place names to alternatives and other lists
### Start with creating the district, state and foreing alternatives.
- Foreign alternative should be relatively easy. Just grab some other country's foreign_alternatives file and delete target country's name and its cities if there are any. Viola!
    - Focus on adding more obvious foreign places (capitals, countries, provinces etc.). Avoid adding famous place or building names such as white house, woodstock etc., because one might refer to these in text even if they are not the focus.
- For state alternatives:
    - Start out with states in district_coords_dict.json.
    - Usual additions are: removing punctuations, no spaces etc. Stuff that you can add with a regex.
    - State names usually don't change over time or don't have that much alternative names.
- For district alternatives:
    - Start out with districts in district_coords_dict.json.
    - Usual additions are: removing punctuations, no spaces etc. Stuff that you can add with a regex.
    - Find known alternative names using wikipedia. You can check old census data to see if some names changed, or some districts were merged into one, or annexed by one etc.
    - You can check the extracted places data. Start from frequent place names.

### After initial completion of district, state and foreing alternatives, it is time for manual error analysis. Run construct_event_database script and check out the output. You should always check the output in the commonness order.
- You can copy some other country's ignore_list.json directly
- You can check geopy_places.json -> These places are supposedly place names and are supposedly in South Africa. Conlficts here usually go to geopy_false_positives.json, but sometimes they are actually place names in south africa, but they are not in the address that geopy returns. In this case you put this place name in to district alternatives with the proper district.
    - Check for common place names or generic names to see if they are indeed in the target country and are a place name. For example: Market place, Church square, Union buildings etc.
    - Check for place names that feels out of ordinary or feels like it's breaking a pattern in naming according to the target country.
    - Check for person names
    - Check if the returned address from geopy actually refers or contains the given place name.
    - If the geopy returned address is longer than usual, definitely investigate.
- You can check not_found_names.json -> These places are not in our foreign, district or state alternatives lists. They are also either not a place or not in target country according to geopy.
    - You can add places from this list to foreign alternatives
    - You can add names to ignore_list. Some names will be generic stuff like river, street, south etc.
    - Check for place names that feel like it belongs to target country
    - Check the place names whose geopy returned address are None