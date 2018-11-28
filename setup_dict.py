# First int key is for number of players, second int key is for index of player in player list
player_init = {
    2: {
        0: {
            'doubloons': 3,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 3,
            'first_plantation': 'corn',
            'governor': False
        }
    },
    3: {
        0: {
            'doubloons': 2,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 2,
            'first_plantation': 'indigo',
            'governor': False
        },
        2: {
            'doubloons': 2,
            'first_plantation': 'corn',
            'governor': False
        }
    },
    4: {
        0: {
            'doubloons': 3,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 3,
            'first_plantation': 'indigo',
            'governor': False
        },
        2: {
            'doubloons': 3,
            'first_plantation': 'corn',
            'governor': False
        },
        3: {
            'doubloons': 3,
            'first_plantation': 'corn',
            'governor': False
        }
    },
    5: {
        0: {
            'doubloons': 4,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 4,
            'first_plantation': 'indigo',
            'governor': False
        },
        2: {
            'doubloons': 4,
            'first_plantation': 'indigo',
            'governor': False
        },
        3: {
            'doubloons': 4,
            'first_plantation': 'corn',
            'governor': False
        },
        4: {
            'doubloons': 4,
            'first_plantation': 'corn',
            'governor': False
        }
    },
    6: {
        0: {
            'doubloons': 5,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 5,
            'first_plantation': 'indigo',
            'governor': False
        },
        2: {
            'doubloons': 5,
            'first_plantation': 'indigo',
            'governor': False
        },
        3: {
            'doubloons': 5,
            'first_plantation': 'corn',
            'governor': False
        },
        4: {
            'doubloons': 5,
            'first_plantation': 'corn',
            'governor': False
        },
        5: {
            'doubloons': 5,
            'first_plantation': 'corn',
            'governor': False
        }
    },
}

# Plantation tile counts assume that the starting tiles have already been taken out for players
# int keys are for the number of players
setup_dict = {
    2: {
        'colonists': 42, 
        'vp': 65, 
        'barrel_dict': {
            'corn': 8,
            'indigo': 9,
            'sugar': 9,
            'tobacco': 7,
            'coffee': 7 }, 
        'plantation_dict': {
            'corn': 6,
            'indigo': 8,
            'sugar': 8,
            'tobacco': 6,
            'coffee': 5 },
        'quarries': 5,
        'building_dict': {
            'small indigo plant': 2,
            'small sugar mill': 2,
            'indigo plant': 2,
            'sugar mill': 2,
            'tobacco storage': 2,
            'coffee roaster': 2,
            'small market': 1,
            'hacienda': 1,
            'construction hut': 1,
            'small warehouse': 1,
            'hospice': 1,
            'office': 1,
            'large market': 1,
            'large warehouse': 1,
            'factory': 1,
            'university': 1,
            'harbour': 1,
            'wharf': 1,
            'guild hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs house': 1,
            'city hall': 1
             }, 
        'prospectors': 1,
        'ship_size_list': [4, 6]
    },
    3: {
        'colonists': 58, 
        'vp': 75, 
        'barrel_dict': {
            'corn': 10,
            'indigo': 11,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 9 }, 
        'plantation_dict': {
            'corn': 9,
            'indigo': 10,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 8 },
        'quarries': 8,
        'building_dict': {
            'small indigo plant': 3,
            'small sugar mill': 3,
            'indigo plant': 3,
            'sugar mill': 3,
            'tobacco storage': 3,
            'coffee roaster': 3,
            'small market': 2,
            'hacienda': 2,
            'construction hut': 2,
            'small warehouse': 2,
            'hospice': 2,
            'office': 2,
            'large market': 2,
            'large warehouse': 2,
            'factory': 2,
            'university': 2,
            'harbour': 2,
            'wharf': 2,
            'guild hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs house': 1,
            'city hall': 1 },  
        'prospectors': 0,
        'ship_size_list': [4, 5, 6]
    },
    4: {
        'colonists': 79, 
        'vp': 100, 
        'barrel_dict': {
            'corn': 10,
            'indigo': 11,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 9 }, 
        'plantation_dict': {
            'corn': 8,
            'indigo': 10,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 8 },
        'quarries': 8,
        'building_dict': {
            'small indigo plant': 4,
            'small sugar mill': 4,
            'indigo plant': 3,
            'sugar mill': 3,
            'tobacco storage': 3,
            'coffee roaster': 3,
            'small market': 2,
            'hacienda': 2,
            'construction hut': 2,
            'small warehouse': 2,
            'hospice': 2,
            'office': 2,
            'large market': 2,
            'large warehouse': 2,
            'factory': 2,
            'university': 2,
            'harbour': 2,
            'wharf': 2,
            'guild hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs house': 1,
            'city hall': 1 }, 
        'prospectors': 1,
        'ship_size_list': [5, 6, 7] 
    },
    5: {
        'colonists': 100, 
        'vp': 122, 
        'barrel_dict': {
            'corn': 10,
            'indigo': 11,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 9 }, 
        'plantation_dict': {
            'corn': 8,
            'indigo': 9,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 8 },
        'quarries': 8,
        'building_dict': {
            'small indigo plant': 4,
            'small sugar mill': 4,
            'indigo plant': 3,
            'sugar mill': 3,
            'tobacco storage': 3,
            'coffee roaster': 3,
            'small market': 2,
            'hacienda': 2,
            'construction hut': 2,
            'small warehouse': 2,
            'hospice': 2,
            'office': 2,
            'large market': 2,
            'large warehouse': 2,
            'factory': 2,
            'university': 2,
            'harbour': 2,
            'wharf': 2,
            'guild hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs house': 1,
            'city hall': 1 },
        'prospectors': 2,
        'ship_size_list': [6, 7, 8] 
    },
    6: {
        'colonists': 121, 
        'vp': 150, 
        'barrel_dict': {
            'corn': 12,
            'indigo': 14,
            'sugar': 14,
            'tobacco': 11,
            'coffee': 11 }, 
        'plantation_dict': {
            'corn': 9,
            'indigo': 12,
            'sugar': 14,
            'tobacco': 11,
            'coffee': 10 },
        'quarries': 10,
        'building_dict': {
            'small indigo plant': 5,
            'small sugar mill': 5,
            'indigo plant': 4,
            'sugar mill': 4,
            'tobacco storage': 4,
            'coffee roaster': 4,
            'small market': 3,
            'hacienda': 3,
            'construction hut': 3,
            'small warehouse': 3,
            'hospice': 3,
            'office': 3,
            'large market': 3,
            'large warehouse': 3,
            'factory': 3,
            'university': 3,
            'harbour': 3,
            'wharf': 3,
            'guild hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs house': 1,
            'city hall': 1 },
        'prospectors': 3,
        'ship_size_list': [7, 8, 9]
    }
}
