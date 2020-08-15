import pandas as pd
import json
import ipdb

excel_2001 = pd.read_excel("India districts geocode 2001, 2011, 2019.xlsx", sheet_name=0)
excel_2011 = pd.read_excel("India districts geocode 2001, 2011, 2019.xlsx", sheet_name=1)
excel_2019 = pd.read_excel("India districts geocode 2001, 2011, 2019.xlsx", sheet_name=2)

state_name_changes = {"Jammu and Kashmir": "Jammu & Kashmir", "Andaman & Nicobar Island": "Andaman & Nicobar Islands", "Arunanchal Pradesh": "Arunachal Pradesh", "Chhattisgarh": "Chhatisgarh", "Dadara & Nagar Havelli": "Dadra & Nagar Haveli", "Odisha": "Orissa", "Pondicherry": "Puducherry", "Delhi  & NCR": "NCT of Delhi"}

# changes between 2011 to 2019. These are not real changes. These are only caused by alternative names or misspelling
alt_2011_to_2019 = {"Bauda": "Baudh", "Chamrajnagar": "Chamarajanagar", "Data Not Available": "DATA NOT AVAILABLE", "East Nimar": "Khandwa (East Nimar)", "Garhchiroli": "Gadchiroli", "Hyderabad": "Hydrabad", "Janjgir-champa": "Janjgir-Champa", "Kaimur (bhabua)": "Kaimur (Bhabua)", "Kansiram Nagar": "Kanshiram Nagar", "Lawangtlai": "Lawngtlai", "Leh (ladakh)": "Leh (Ladakh)", "Maharajganj": "Mahrajganj", "Mahbubnagar": "Mahabubnagar", "Marigaon": "Morigaon", "Nagappattinam": "Nagapattinam", "Nicobar": "Nicobars", "North & Middle Andaman": "North  & Middle Andaman", "North 24 Parganas": "North Twenty Four Parganas", "Pashchim Medinipur": "Paschim Medinipur", "Ri Bhoi": "Ribhoi", "Sant Ravi Das Nagar(bhadohi)": "Sant Ravidas Nagar (Bhadohi)", "Saraikela-kharsawan": "Saraikela-Kharsawan", "Saran (chhapra)": "Saran", "Siddharth Nagar": "Siddharthnagar", "South 24 Parganas": "South Twenty Four Parganas", "Virudunagar": "Virudhunagar", "West Nimar": "Khargone (West Nimar)", "Y.s.r.": "Kadapa"}

# list of names that changed or disappeared from 2011 to 2019
# {'Jaintia Hills', 'Warangal'}
# "Jainta Hills" became -> "East Jainta Hills" and "West Jainta Hills"
# "Warangal" became -> "Warangal (R)" and "Warangal (U)"


# Since we do this after changing 2011 to 2019, we don't have to check 2001 to 2019 too.
# changes between 2001 to 2011. These are not real changes. These are only caused by alternative names or misspelling
alt_2001_to_2011 = {"Data Not Available": "DATA NOT AVAILABLE", "East Nimar": "Khandwa (East Nimar)", "Hyderabad": "Hydrabad", "Janjgir - Champa": "Janjgir-Champa", "Mahbubnagar": "Mahabubnagar", "Marigaon": "Morigaon", "Ri Bhoi": "Ribhoi", "Sant Ravidas Nagar Bhadohi": "Sant Ravidas Nagar (Bhadohi)", "South  Twenty Four Parganas": "South Twenty Four Parganas", "West Nimar": "Khargone (West Nimar)", "Barabanki": "Bara Banki", "Cuddapah": "Kadapa", "Dantewada": "Dakshin Bastar Dantewada", "Hathras": "Mahamaya Nagar", "Kawardha": "Kabeerdham", "Mumbai (Suburban)": "Mumbai Suburban", "Nawanshahr": "Shahid Bhagat Singh Nagar", "Nellore": "Sri Potti Sriramulu Nellore", "North Cachar Hills": "Dima Hasao", "Pakaur": "Pakur", "Pondicherry": "Puducherry", "Rajauri": "Rajouri", "Rangareddi": "Rangareddy", "Senapati (Excl. 3 sub-divisions)": "Senapati", "Sibsagar": "Sivasagar", "Sonapur": "Subarnapur", "Kanker": "Uttar Bastar Kanker"}

# list of names that changed or disappeared from 2001 to 2011
# {'Andamans', 'Medinipur'}
# "Andamans" -> maybe became "South Andaman" and "North  & Middle Andaman" but I'm not sure
# "Medinipur" became -> "Paschim Medinipur" and "Purba Medinipur"

for k,v in state_name_changes.items():
    excel_2001.loc[excel_2001.State == k, "State"] = v

for k,v in state_name_changes.items():
    excel_2011.loc[excel_2011.State == k, "State"] = v

for k,v in alt_2011_to_2019.items():
    excel_2011.loc[excel_2011.District == k, "District"] = v

for k,v in alt_2001_to_2011.items():
    excel_2001.loc[excel_2001.District == k, "District"] = v

# Latest state name is puducherry apparently
excel_2019.loc[excel_2019.State == "Pondicherry", "State"] = "Puducherry"
excel_2019.loc[excel_2019.District == "Kadapa(YSR)", "District"] = "Kadapa"

excel_2019 = excel_2019.drop(excel_2019[excel_2019.District == "DATA NOT AVAILABLE"].index)
excel_2011 = excel_2011.drop(excel_2011[excel_2011.District == "DATA NOT AVAILABLE"].index)
excel_2001 = excel_2001.drop(excel_2001[excel_2001.District == "DATA NOT AVAILABLE"].index)

# Add "Delhi" to the end of district names except New Delhi (They have generic names like West,East etc.)
excel_2001.loc[excel_2001.State == "NCT of Delhi", "District"] = excel_2001.loc[excel_2001.State == "NCT of Delhi", "District"].apply(lambda x: x + " Delhi" if x != "New Delhi" else x)
excel_2011.loc[excel_2011.State == "NCT of Delhi", "District"] = excel_2011.loc[excel_2011.State == "NCT of Delhi", "District"].apply(lambda x: x + " Delhi" if x != "New Delhi" else x)
excel_2019.loc[excel_2019.State == "NCT of Delhi", "District"] = excel_2019.loc[excel_2019.State == "NCT of Delhi", "District"].apply(lambda x: x + " Delhi" if x != "New Delhi" else x)

# Fix Sikkim districts (They have generic names like West,East etc.)
excel_2001.loc[excel_2001.State == "Sikkim", "District"] = excel_2001.loc[excel_2001.State == "Sikkim", "District"].apply(lambda x: x + " Sikkim")
excel_2011.loc[excel_2011.State == "Sikkim", "District"] = excel_2011.loc[excel_2011.State == "Sikkim", "District"].apply(lambda x: x + " Sikkim")
excel_2019.loc[excel_2019.State == "Sikkim", "District"] = excel_2019.loc[excel_2019.State == "Sikkim", "District"].apply(lambda x: x.replace("District", "Sikkim"))

# Some district names are not unique, so we make them unique.
dups_2019 = excel_2019[excel_2019.District.duplicated()].District.tolist() # 2001 and 2011 dups are only subsets of this list
excel_2019.loc[excel_2019.District.isin(dups_2019), "District"] = excel_2019.loc[excel_2019.District.isin(dups_2019)].apply(lambda row: row.District + " (" + row.State + ")", axis=1)
excel_2011.loc[excel_2011.District.isin(dups_2019), "District"] = excel_2011.loc[excel_2011.District.isin(dups_2019)].apply(lambda row: row.District + " (" + row.State + ")", axis=1)
excel_2001.loc[excel_2001.District.isin(dups_2019), "District"] = excel_2001.loc[excel_2001.District.isin(dups_2019)].apply(lambda row: row.District + " (" + row.State + ")", axis=1)

excel_2019.to_json("2019_fixed.json", orient="records", lines=True, force_ascii=False)
excel_2011.to_json("2011_fixed.json", orient="records", lines=True, force_ascii=False)
excel_2001.to_json("2001_fixed.json", orient="records", lines=True, force_ascii=False)

# NOTE : Some states have districts with same names as theirs! (Ex: "Puducherry state" and "Puducherry district") -> prioritize district names? (if you just see "Puducherry" then call it district. Only if you see "Puducherry state" then call it state)

# TODO : Add class as a key, and introduce state coords too!

out_json = {}
for dist in list(set(excel_2019.District.tolist() + excel_2011.District.tolist() + excel_2001.District.tolist())):
    coords_2019 = []
    coords_2011 = []
    coords_2001 = []

    match_2019 = excel_2019[excel_2019.District == dist]
    match_2011 = excel_2011[excel_2011.District == dist]
    match_2001 = excel_2001[excel_2001.District == dist]

    if len(match_2019) != 0:
        coords_2019 = [match_2019.iloc[0].COORD_X, match_2019.iloc[0].COORD_Y]
    if len(match_2011) != 0:
        coords_2011 = [match_2011.iloc[0].COORD_X, match_2011.iloc[0].COORD_Y]
    if len(match_2001) != 0:
        coords_2001 = [match_2001.iloc[0].COORD_X, match_2001.iloc[0].COORD_Y]

    out_json[dist] = {"2001":coords_2001, "2011":coords_2011, "2019":coords_2019}

with open("district_coords_dict.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(out_json))

# TODO: Play with geopy and determine if there is a pattern in its output

# TODO: Flow is like this:
#  - Check if a name is in state name list (with alternatives)
#    - If so, get its coordinates from state_coords dict (Unfortunately we have no dicts for 2001 and 2011). Break
#  - Check if a name is in district name list (with alternatives)
#    - If so, get its coordinates from district_coords dict given its year. Break
#  - Give the place name to geopy
#    - If returned value is not None
#      - Unsure what to here???
#      - Check the district part in district name list (with alternatives)???
#    - If returned value is None, exit


# Current known exceptions, ambiguities, new districts etc. in geopy_outs.txt
dist_ambiguities = ["Bijapur", "Hamirpur", "Aurangabad", "Balrampur", "Pratapgarh", "Raigarh", "Bilaspur"]
dist_unknowns = ["Jhargram", "Charaideo", "East Karbi Anglong", "West Karbi Anglong", "Purba Bardhaman", "Paschim Bardhaman", "Kalimpong", "Thodupuzha", "Hojai", "Jiribam", "Noney", "Alipurduar", "Narayanpet", "Bishwanath", "Longding", "Agar Malwa", "Tengnoupal", "Devikulam", "Peerumade", "Roorkee", "Udumbanchola", "Kangpokpi", "Sohna", "Kamjong", "Haldwani", "Phungyar", "Kakinada (Rural)", "Dhari", "Majuli", "Pherzawl", "South Salmara-Mankachar"]
dist_new_ones = ["Tenkasi", "Kallakurichi", "Tirupattur", "Chengalpattu", "Sholinganallur", "Ranipet", "Mulugu"]
national_parks = ["Manas National Park", "Bandipur National Park/Tiger Reserve", "Nallamala Forest", "Nagarahole (Rajiv Gandhi) National Park/Tiger Reserve", "Kaziranga National Park/Tiger Reserve", "Bannerghatta National Park", "Rajaji National Park/Tiger Reserve", "Kudremukh National Park"]
