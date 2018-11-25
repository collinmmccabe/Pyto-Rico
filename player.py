# Need to figure out how to access/change parent class attributes...

class Player(name):
    def __init__(self, name):
        self._name = name
        self._doubloons = 0
        self._vp = 0
        self._free_colonists = 0
        self._governor_flag = False
        self._island = Island()
        self._city = City()
        self._resources = Resources()

class Island():
    def __init__(self):
        self._plantation_list = []
        # this is just here to remind me to remove it in other parts of the code
        self._occupied_squares = len(self._plantation_list)
    def build(self, plantation_type):
        if len(self._plantation_list) < 12:
            self._plantation_list.append(Plantation(plantation_type))
        return None
    def produce(self):
        for good_type in ['corn', 'indigo', 'sugar', 'tobacco', 'coffee']:
            taken = min(min(sum([1 for i in self._plantation_list if (i.good_produced == good_type and i.occupied_worker)]), 
                            sum([j.occupied_workers for j in Player.City.building_list if j.good_processed == good_type])), 
                        Market.Supply[good_type])
            Market.Supply[good_type] -= taken
            Player.Resources[good_type] += taken
        return None

class Plantation(good_type):
    def __init__(self, good_type):
        self._good_produced = good_type
        self._occupied_worker = False
    def add_colonist(self):
        if (not self._occupied_worker) and Player.free_colonists > 0:
            self._occupied_worker = True
            Player.free_colonists -= 1
        return None
    def remove_colonist(self):
        if self._occupied_worker:
            self._occupied_worker = False
            Player.free_colonists += 1
        return None

class City():
    def __init__(self):
        self._building_list = []
        self._occupied_squares = 0
    def build(self, building_name):
        if BuildingLookup[building_name].size + self._occupied_squares <= 12 and \
          building_name not in self._building_list.building_name:  # self.building_list.building_name probably not right...
            self._building_list.append(Building(building_name))
            self._occupied_squares += BuildingLookup[building_name].size
            if self._occupied_squares == 12:
                Market.endgame_trigger = True

class Building(building_name):
    def __init__(self, building_name):
        self._building_name = building_name
        self._good_processed = BuildingLookup[building_name].worker_spaces
        self._free_workers = BuildingLookup[building_name].worker_spaces
        self._occupied_workers = 0
    def add_colonist(self):
        if self._free_workers > 0 and Player.free_colonists > 0:
            self._occupied_workers += 1
            self._free_workers -= 1
            Player.free_colonists -= 1
    def remove_colonist(self):
        if self._occupied_workers > 0:
            self._occupied_workers -= 1
            self._free_workers += 1
            Player.free_colonists += 1

class Resources():
    def __init__(self):
        self._corn = 0
        self._indigo = 0
        self._sugar = 0
        self._tobacco = 0
        self._coffee = 0
    def shipping(self, good, number):
        if self[good] >= number:
            self[good] -= number
            Market.Supply[good] += number
    def trading(self, good):
        if self[good] > 0:
            self[good] -= 1
            TradingPost.trading_queue.append(good)
