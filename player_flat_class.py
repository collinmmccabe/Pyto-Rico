class Player(name):
    def __init__(self, name):
        self._name = name
        self._doubloons = 0
        self._vp = 0
        self._free_colonists = 0
        self._governor_flag = False

        self._plantation_list = []

        self._building_list = []
        self._city_occupied_squares = 0

        self._resources = {'corn': 0, 'indigo': 0, 'sugar': 0, 'tobacco': 0, 'coffee': 0}
    
    def pay_doubloons(self, number):
        if self._doubloons >= number:
            self._doubloons -= number
            return number  # for adding to Market doubloons
        return None
    def get_doubloons(self, number):
        self._doubloons += number
        return number
    def get_vp(self, number):
        self._vp += number
        return number
    def get_colonists(self, number):
        self._free_colonists += number
        return None
    def set_governor_flag(self, value):
        self._governor_flag = value
        return None
    
    def build_plantation(self, plantation_type):
        if len(self._plantation_list) < 12:
            self._plantation_list.append({'good_produced': plantation_type, 'occupied': False})
        return None
    def produce_plantation(self, market_supply_dict):  # send the market supply here to communicate with fn
        for good_type in ['corn', 'indigo', 'sugar', 'tobacco', 'coffee']:  # could replace list with keys of mkt spl d
            taken = min(min(sum([1 for i in self._plantation_list if (i.good_produced == good_type and i.occupied)]), 
                            sum([j.occupied_spaces for j in self._building_list if j.good_processed == good_type])), 
                        market_supply_dict[good_type])
            market_supply_dict[good_type] -= taken
            self._resources[good_type] += taken
        # Maybe use return value to communicate with Market class?
        return market_supply_dict
    def add_colonist_plantation(self, plantation_list_index):
        if (not self._plantation_list[plantation_list_index].occupied) and self._free_colonists > 0:
            self._plantation_list[plantation_list_index].occupied = True
            self._free_colonists -= 1
        return None
    def remove_colonist_plantation(self, plantation_list_index):
        if self._plantation_list[plantation_list_index].occupied:
            self._plantation_list[plantation_list_index].occupied = False
            self._free_colonists += 1
        return None
    
    def build_building(self, specific_building_lookup, cost):  # specific building lookup is BuildingLookup[building_name]
        endgame_trigger = False
        if ((specific_building_lookup.size + self._city_occupied_squares <= 12) and 
          (specific_building_lookup.name not in [i.name for i in self._building_list]) and
          (cost <= self._doubloons)):
            self._building_list.append({'name': specific_building_lookup.name, 
                                        'good_processed': specific_building_lookup.good_processed,
                                        'free_worker_spaces': specific_building_lookup.free_worker_spaces,
                                        'occupied_worker_spaces': 0})
            self._city_occupied_squares += specific_building_lookup.size
            if self._city_occupied_squares == 12:
                endgame_trigger = True
            return endgame_trigger, self.pay_doubloons(cost)  # Use return value to communicate with Market class
        return endgame_trigger, None
    def add_colonist_building(self, building_list_index):
        if self._building_list[building_list_index].free_worker_spaces > 0 and self._free_colonists > 0:
            self._building_list[building_list_index].occupied_worker_spaces += 1
            self._building_list[building_list_index].free_worker_spaces -= 1
            self._free_colonists -= 1
        return None
    def remove_colonist_building(self, building_list_index):
        if self._building_list[building_list_index].occupied_worker_spaces > 0:
            self._building_list[building_list_index].occupied_worker_spaces -= 1
            self._building_list[building_list_index].free_worker_spaces += 1
            self._free_colonists += 1
        return None

    def ship_resources(self, good, number):
        if self._resources[good] >= number:
            self._resources[good] -= number
            return number, self.get_vp(number)  # this will be used to update Market.Supply[good] and Market.vp
        return None, None
    def trade_resources(self, good):
        trade_value = {'corn': 0, 'indigo': 1, 'sugar': 2, 'tobacco': 3, 'coffee': 4}
        if self._resources[good] > 0:
            self._resources[good] -= 1
            return good, self.get_doubloons(trade_value[good])  # for TradingPost.trading_queue.append(good)
        return None, None
