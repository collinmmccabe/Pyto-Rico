# From PEP 351
class imdict(dict):
    def __hash__(self):
        return id(self)

    def _immutable(self, *args, **kws):
        raise TypeError('object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear       = _immutable
    update      = _immutable
    setdefault  = _immutable
    pop         = _immutable
    popitem     = _immutable

d = {'small_indigo_plant': {
        'name': 'Small Indigo Plant', 
        'good_processed': 'indigo',
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Production',
        'perk_description': 'A production building that processes a maximum of 1 indigo',
        'base_cost': 1,
        'quarries_allowed': 1,
        'vp_value': 1
        },
    'small_sugar_mill': {
        'name': 'Small Sugar Mill', 
        'good_processed': 'sugar',
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Production',
        'perk_description': 'A production building that processes a maximum of 1 sugar',
        'base_cost': 2,
        'quarries_allowed': 1,
        'vp_value': 1
        },
    'indigo_plant': {
        'name': 'Indigo Plant', 
        'good_processed': 'indigo',
        'free_worker_spaces': 3,
        'size': 1,
        'building_type': 'Large Production',
        'perk_description': 'A production building that processes a maximum of 3 indigo',
        'base_cost': 3,
        'quarries_allowed': 2,
        'vp_value': 2
        },
    'sugar_mill': {
        'name': 'Sugar Mill', 
        'good_processed': 'sugar',
        'free_worker_spaces': 3,
        'size': 1,
        'building_type': 'Large Production',
        'perk_description': 'A production building that processes a maximum of 3 sugar',
        'base_cost': 4,
        'quarries_allowed': 2,
        'vp_value': 2
        },
    'tobacco_storage': {
        'name': 'Tobacco Storage', 
        'good_processed': 'tobacco',
        'free_worker_spaces': 3,
        'size': 1,
        'building_type': 'Large Production',
        'perk_description': 'A production building that processes a maximum of 3 tobacco',
        'base_cost': 5,
        'quarries_allowed': 3,
        'vp_value': 3
        },
    'coffee_roaster': {
        'name': 'Coffee Roaster', 
        'good_processed': 'coffee',
        'free_worker_spaces': 2,
        'size': 1,
        'building_type': 'Large Production',
        'perk_description': 'A production building that processes a maximum of 2 coffee',
        'base_cost': 6,
        'quarries_allowed': 3,
        'vp_value': 3
        },
    'small_market': {
        'name': 'Small Market', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that gives +1 doubloons for sales in the trader phase',
        'base_cost': 1,
        'quarries_allowed': 1,
        'vp_value': 1
        },
    'hacienda': {
        'name': 'Hacienda', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that gives +1 random plantation in the settler phase',
        'base_cost': 2,
        'quarries_allowed': 1,
        'vp_value': 1
        },
    'construction_hut': {
        'name': 'Construction Hut', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that allows selection of a quarry in the settler phase',
        'base_cost': 2,
        'quarries_allowed': 1,
        'vp_value': 1
        },
    'small_warehouse': {
        'name': 'Small Warehouse', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that allows player to store all of 1 type of goods (in addition to the one already kept) at the end of the captain phase',
        'base_cost': 3,
        'quarries_allowed': 1,
        'vp_value': 1
        },
    'hospice': {
        'name': 'Hospice', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that gives +1 colonist to place on new plantation in the settler phase',
        'base_cost': 4,
        'quarries_allowed': 2,
        'vp_value': 2
        },
    'office': {
        'name': 'Office', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that allows sale of the same good in the trader phase',
        'base_cost': 5,
        'quarries_allowed': 2,
        'vp_value': 2
        },
    'large_market': {
        'name': 'Large Market', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that gives +2 doubloons for sales in the trader phase',
        'base_cost': 5,
        'quarries_allowed': 2,
        'vp_value': 2
        },
    'large_warehouse': {
        'name': 'Large Warehouse', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that allows player to store all of 2 types of goods (in addition to the one already kept) at the end of the captain phase',
        'base_cost': 6,
        'quarries_allowed': 2,
        'vp_value': 2
        },
    'factory': {
        'name': 'Factory', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that gives player 0, 1, 2, 3, or 5 doubloons for producing 1, 2, 3, 4, or 5 different kinds of goods, respectively, in the craftsman phase',
        'base_cost': 7,
        'quarries_allowed': 3,
        'vp_value': 3
        },
    'university': {
        'name': 'University', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that gives +1 colonist to place on new building in the builder phase',
        'base_cost': 8,
        'quarries_allowed': 3,
        'vp_value': 3
        },
    'harbour': {
        'name': 'Harbour', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that gives +1 VP per delivery of a type of good in the captain phase',
        'base_cost': 8,
        'quarries_allowed': 3,
        'vp_value': 3
        },
    'wharf': {
        'name': 'Wharf', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 1,
        'building_type': 'Small Violet',
        'perk_description': 'A violet building that gives player a private ship in the captain phase',
        'base_cost': 9,
        'quarries_allowed': 3,
        'vp_value': 3
        },
    'guild_hall': {
        'name': 'Guild Hall', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 2,
        'building_type': 'Large Violet',
        'perk_description': 'A large violet building that gives +1 VP per small production building and +2 VP per large production building at the end of the game',
        'base_cost': 10,
        'quarries_allowed': 4,
        'vp_value': 4
        },
    'residence': {
        'name': 'Residence', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 2,
        'building_type': 'Large Violet',
        'perk_description': 'A large violet building that gives VP for the number of island spaces filled: 4 VP for 9 or fewer spaces filled, 5 for 10, 6 for 11, or 7 for 12 at the end of the game',
        'base_cost': 10,
        'quarries_allowed': 4,
        'vp_value': 4
        },
    'fortress': {
        'name': 'Fortress', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 2,
        'building_type': 'Large Violet',
        'perk_description': 'A large violet building that gives +1 VP per 3 colonists (rounded down) at the end of the game',
        'base_cost': 10,
        'quarries_allowed': 4,
        'vp_value': 4
        },
    'customs_house': {
        'name': 'Customs House', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 2,
        'building_type': 'Large Violet',
        'perk_description': 'A large violet building that gives +1 VP per 4 VP earned before the end of the game (rounded down) at the end of the game',
        'base_cost': 10,
        'quarries_allowed': 4,
        'vp_value': 4
        },
    'city_hall': {
        'name': 'City Hall', 
        'good_processed': None,
        'free_worker_spaces': 1,
        'size': 2,
        'building_type': 'Large Violet',
        'perk_description': 'A large violet building that gives +1 VP per violet building at the end of the game',
        'base_cost': 10,
        'quarries_allowed': 2,
        'vp_value': 2
        }
    }

building_lookup = imdict(d)
