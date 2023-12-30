# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

updated_damages = []
for damage in damages:
    if damage == "Damages not recorded":
        updated_damages.append(damage)
        continue
    elif "M" in damage:
        damage = damage.removesuffix("M")
        damage = float(damage) * conversion["M"]
    elif "B" in damage:
        damage = damage.removesuffix("B")
        damage = float(damage) * conversion["B"]
    
    updated_damages.append(damage)

# print(updated_damages)

# Sub-Task 2: Create a Dictionary function for each attribute of the hurricanes

def hurricane_data(name_list, month_list, year_list, wind_list, area_list, damage_list, death_list):
    # Create the inner dictionary for each attribute and data_point and outer dictionary to wrap all information
    primary_dict = {}
    secondary_dict = {}
    # Loop through each data point as per index to get all data points added and then overall data added into the secondary dictionary
    for index in range(len(name_list)):
        primary_dict['Name'] = name_list[index]
        primary_dict['Month'] = month_list[index]
        primary_dict['Year'] = year_list[index]
        primary_dict['Max Sustained_Wind'] = wind_list[index]
        primary_dict['Areas Affected'] = area_list[index]
        primary_dict['Damage'] = damage_list[index]
        primary_dict['Deaths'] = death_list[index]
        
        # With primary dictionary appended and complete, update the secondary dictionary then refresh the primary dictionary
        secondary_dict[name_list[index]] = primary_dict
        primary_dict = {}

    return secondary_dict

hurricanes = hurricane_data(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)

def key_change(hurricane_dict, year_list):
    yearly_data = {}
    hurricane_dict_value = list(hurricane_dict.values())

    for index in range(len(year_list)):
        current_year = year_list[index]
        current_cane = hurricane_dict_value[index]
        if not current_year in yearly_data:
            yearly_data[current_year] = [current_cane]
        else:
            yearly_data[current_year].append(current_cane)
    
    return yearly_data

yearly_impact = key_change(hurricanes, years)
#print(yearly_impact)


# COUNT FUNCTION OF HITS IN THE ATLANTIC
def location_impact(hurricanes):
    
    # defaultdict is a class of the collections module that creates a dict object with a default new key creation process. The default factory argument allows for new keys to be generated with default values in case a key is not found in the dictionary.
    from collections import defaultdict
    area_count = defaultdict(int)
    for impact in hurricanes:
        for area in hurricanes[impact]["Areas Affected"]:
            area_count[area] += 1 
    return dict(area_count)


area_affected = location_impact(hurricanes)
#print(area_affected)

def max_affected(areas_dict):
    area_max = ""
    area_count = 0
    for key, value in areas_dict.items():
        if value > area_count:
            area_max = key
            area_count = value
    
    return area_max, area_count

hurricane_impacted_area = max_affected(area_affected)
#print(hurricane_impacted_area)

# Step 6
def death_toll(hurricanes):
    death_toll = {}
    for hurricane in hurricanes:
        death_toll[hurricane] = hurricanes[hurricane]["Deaths"]
    
    # Using the max_affected function call here
    return max_affected(death_toll)

hurricane_hit, deaths = death_toll(hurricanes)
#print(hurricane_hit, deaths)

# MORTALITY SCALE
mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000,
}

# Mortality Rating Hurricane function
def mortality_rating(hurricanes):
    # Mortality rating dictionary as per rating level
    mortality_rating = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[]}
    # To review each hurricane and check what level it is
    for hurricane in hurricanes:
        # First conditional to check if it is at rating 0
        if hurricanes[hurricane]["Deaths"] <= mortality_scale[0]:
            mortality_rating[0].append(hurricanes[hurricane])
        
        # Second conditional to check rating 1
        elif hurricanes[hurricane]["Deaths"] > mortality_scale[0] and hurricanes[hurricane]["Deaths"] <= mortality_scale[1]:
            mortality_rating[1].append(hurricanes[hurricane])
        
         # Third conditional to check rating 2
        elif hurricanes[hurricane]["Deaths"] > mortality_scale[1] and hurricanes[hurricane]["Deaths"] <= mortality_scale[2]:
            mortality_rating[2].append(hurricanes[hurricane])
    
         # Third conditional to check rating 3
        elif hurricanes[hurricane]["Deaths"] > mortality_scale[2] and hurricanes[hurricane]["Deaths"] <= mortality_scale[3]:
            mortality_rating[3].append(hurricanes[hurricane])

         # Fourth conditional to check rating 4
        elif hurricanes[hurricane]["Deaths"] > mortality_scale[3] and hurricanes[hurricane]["Deaths"] <= mortality_scale[4]:
            mortality_rating[4].append(hurricanes[hurricane])

        else:
            mortality_rating[5].append(hurricanes[hurricane])

    return mortality_rating

test1 = mortality_rating(hurricanes)
#print(test1[5])


#STEP 8: Find the Hurricane that caused the greatest damage and how costly it was
def max_damage(hurricane_dict):
    max_damage_value = 0
    hurricane_damage_name = ""
    for hurricane in hurricane_dict:
        if hurricane_dict[hurricane]["Damage"] == "Damages not recorded":
            continue
        elif hurricane_dict[hurricane]["Damage"] > max_damage_value:
            max_damage_value = hurricane_dict[hurricane]["Damage"]
            hurricane_damage_name = hurricane

    return max_damage_value, hurricane_damage_name

damage_value, hurricane_name = max_damage(hurricanes)
# print(hurricane_name, damage_value)

#STEP 9: Function to rate the damage scale of hurricanes
damage_scale = {
    0: 0,
    1: 100000000,
    2: 1000000000,
    3: 10000000000,
    4: 50000000000
}

def damage_rating(hurricane_dictionary):
    damage_rating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for hurricane in hurricane_dictionary:

        # Text Based response
        if hurricane_dictionary[hurricane]["Damage"] == "Damages not recorded":
            damage_rating[0].append(hurricanes[hurricane])

        # First conditional to check if it is at rating 0
        elif hurricane_dictionary[hurricane]["Damage"] <= damage_scale[0]:
            damage_rating[0].append(hurricanes[hurricane])
        
        # Second conditional to check rating 1
        elif hurricane_dictionary[hurricane]["Damage"] > damage_scale[0] and hurricane_dictionary[hurricane]["Damage"] <= damage_scale[1]:
            damage_rating[1].append(hurricanes[hurricane])
        
         # Third conditional to check rating 2
        elif hurricane_dictionary[hurricane]["Damage"] > damage_scale[1] and hurricane_dictionary[hurricane]["Damage"] <= damage_scale[2]:
            damage_rating[2].append(hurricanes[hurricane])
    
         # Third conditional to check rating 3
        elif hurricane_dictionary[hurricane]["Damage"] > damage_scale[2] and hurricane_dictionary[hurricane]["Damage"] <= damage_scale[3]:
            damage_rating[3].append(hurricanes[hurricane])

         # Fourth conditional to check rating 4
        elif hurricane_dictionary[hurricane]["Damage"] > damage_scale[3] and hurricane_dictionary[hurricane]["Damage"] <= damage_scale[4]:
            damage_rating[4].append(hurricanes[hurricane])

        else:
            damage_rating[5].append(hurricanes[hurricane])

    return damage_rating

damages = damage_rating(hurricanes)
print(damages[5])

