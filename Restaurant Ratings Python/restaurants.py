"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurants.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)
    
    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result


def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

    r = []

    for i in names_final:
        r.append([name_to_rating[i], i])
    r.sort(reverse = True)

    return r


def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """

    names_cuisine = []

    for cuisine in cuisines_list:
        for name in cuisine_to_names[cuisine]:
            names_cuisine.append(name)

    names_price = []

    for name in names_matching_price:
        if name in names_cuisine:
            names_price.append(name)

    return names_price


def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    >>> read_restaurants('/Users/kristine/Documents/Restaurant Ratings Python/restaurants_small.txt')
    {'Georgie Porgie': '87%', 'Queen St. Cafe': '82%', 'Dumplings R Us': '71%', 'Mexican Grill': '85%', 'Deep Fried Everything': '52%'}{'Georgie Porgie': '87%', 'Queen St. Cafe': '82%', 'Dumplings R Us': '71%', 'Mexican Grill': '85%', 'Deep Fried Everything': '52%'}
    
    file location: '/Users/kristine/Documents/Restaurant Ratings Python/restaurants_small.txt'
    
    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """
    
    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}
    
    fh = open(file, 'r')
    lines = fh.readlines()

    for i in range(0, len(lines), 5):

        # a dict of {restaurant name: rating%}
        name_to_rating[lines[i].strip()] = lines[i + 1].strip()

        # a dict of {price: list of restaurant names}
        if lines[i + 2].strip() == '$':
            price_to_names['$'].append(lines[i].strip())
        elif lines[i + 2].strip() == '$$':
            price_to_names['$$'].append(lines[i].strip())
        elif lines[i + 2].strip() == '$$$':
            price_to_names['$$$'].append(lines[i].strip())
        else:
            price_to_names['$$$$'].append(lines[i].strip())

        # a dict of {cuisine: list of restaurant names}
        cuisines = lines[i + 3].strip().split(',')
        for cuisine in cuisines:
            if cuisine not in cuisine_to_names:                # if we haven't encountered this cuisine yet
                cuisine_to_names[cuisine] = []                 # initialize a list inside the dictionary
            cuisine_to_names[cuisine].append(lines[i].strip()) # before we append the restaurant

    return (name_to_rating, price_to_names, cuisine_to_names)        
