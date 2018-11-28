import random
from setup_dict import setup_dict
from building_lookup import building_lookup

class DictRef(dict):
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, value):
        self[key] = value

class Market(object):
    def __init__(self, setup_subdict):
        self.endgame_trigger = False
        self.buildings = self.Buildings(setup_subdict.building_dict)
        self.plantations = self.Plantations(setup_subdict.plantation_dict, setup_subdict.quarries)
        self.role_options = self.RoleOptions(setup_subdict.prospectors)
        self.trading_post = self.TradingPost()
        self.captain_ships = self.CaptainShips(setup_subdict.ship_size_list)
        self.colonist_ship = self.ColonistShip(setup_subdict.colonists)
        self.supply = self.Supply(setup_subdict.barrel_dict, setup_subdict.vp)

    class Buildings(DictRef):
        def __init__(self, building_dict):
            for building in building_dict.key():
                setattr(self, building, { 'available': building_dict[building], 'info': self.Building(building) })

        def building_taken(self, building):
            if self._available_buildings[building] > 0:
                self._available_buildings[building] -= 1

        class Building(DictRef):
            def __init__(self, building_name):
                setattr(self, 'properties', building_lookup[building_name])

class Plantations(object):
    def __init__(self, plantation_dict, quarries):
        self._face_down_pool = plantation_dict
        self._face_up_pool = []
        self._discard_pool = []
        self._quarries = quarries
    def plantation_taken(self, plantation):
        if plantation in self._face_up_pool:
            self._face_up_pool.remove(plantation)
            return plantation
        return None
    def quarry_taken(self):
        if self._quarries > 0:
            self._quarries -= 1
            return 'quarry'
        return None
    def draw_new_tiles(self, num_players):
        self._discard_pool += self._face_up_pool
        self._face_up_pool.clear()
        if len(self._face_down_pool) == 0:
            self._face_down_pool += self._discard_pool
            self._discard_pool.clear()
        while len(self._face_up_pool) < (num_players + 1):
            self._face_up_pool += self._face_down_pool.pop(random.randrange(len(self._face_down_pool)))
            if len(self._face_down_pool) == 0:
                self._face_down_pool += self._discard_pool
                self._discard_pool.clear()
        return None

class RoleOptions(object):
    def __init__(self, prospectors):
        self._role_list = [Role('mayor'), Role('captain'), Role('etc')]
        self._role_list += (Role('prospector') * prospectors)
        class Role(object):
            def __init__(self, role_name):
                self._role_name = role_name
                self._stored_doubloons = 0
                self._taken_flag = False
    def choose_role(self, role):
        if not self._role_list[role]._taken_flag:
            Player.doubloons += self._role_list[role]._stored_doubloons
            self._role_list[role]._stored_doubloons = 0
            self._role_list[role]._.taken_flag = True
            return Phase[role_name].full_phase()
        return None

class TradingPost():
    def __init__(self):
        self._trading_queue = []
    def add_barrel(self, good_type):
        if len(self._trading_queue) < 4:
            self._trading_queue.append(good_type)
            return good_type
    def empty_queue(self):
        while self._trading_queue:
            Supply.Barrels[self._trading_queue.pop()] += 1
        return None

class CaptainShips(object):
    def __init__(self, ship_size_list):
        self._ship_list = []
        for ship_size in ship_size_list:
            self._ship_list.append(Ship(ship_size))
        class Ship(object):
            def __init__(self, size):
                self._free_space = size
                self._used_space = 0
                self._good_type = None
            def load_ship(self, good, number):
                if (used_space == 0 or good == self._good_type) and number <= self._free_space:
                    self._good_type = good
                    self._free_space -= number
                    self._used_space += number
                    return number
                return None
            def unload_ship(self):
                if self._free_space == 0:
                    Supply.Barrels[self._good_type] += self._used_space
                    self._free_space += self._used_space
                    self._used_space = 0
                return None

class ColonistShip(object):
    def __init__(self, colonists):
        self._colonists_carried = 0
        self._colonists_supply = colonists
    def new_voyage(self, new_colonists):
        if self._colonists_supply > new_colonists:
            self._colonists_supply -= new_colonists
            self._colonists_carried += new_colonists
        else:
            self._colonists_carried += self._colonists_supply
            self._colonists_supply = 0
            Market.endgame_trigger = True

class Supply(object):
    def __init__(self, barrel_dict, vp):
        self._barrels = barrel_dict
        self._vp = vp
    def check_vp_supply(self):
        if self._vp <= 0:
            Market.endgame_trigger = True
