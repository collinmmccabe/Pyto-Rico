import random
from building_lookup import building_lookup

class DictRef(dict):
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, value):
        self[key] = value

class Market(object):
    def __init__(self, setup_subdict, num_players):
        self.endgame_trigger = False
        self.buildings = self.Buildings(setup_subdict['building_dict'])
        self.plantations = self.Plantations(setup_subdict['plantation_dict'], 
                                            setup_subdict['quarries'],
                                            num_players)
        #self.role_options = self.RoleOptions(setup_subdict.prospectors)
        self.trading_post = self.TradingPost()
        #self.captain_ships = self.CaptainShips(setup_subdict.ship_size_list)
        self.colonist_ship = self.ColonistShip(setup_subdict['colonists'], num_players)
        self.supply = self.Supply(setup_subdict['barrel_dict'], setup_subdict['vp'])

    class Buildings(DictRef):
        def __init__(self, building_dict):
            for building, count in building_dict.items():
                setattr(self, building, { 'available': count, 'info': self.Building(building) })

        def building_taken(self, building):
            if self[building].available > 0:
                self[building].available -= 1

        class Building(DictRef):
            def __init__(self, building_name):
                for key, value in building_lookup[building_name].items():
                    setattr(self, key, value)
            
            def __repr__(self):
                return ("Name: {}\nDescription: {}\nBuilding Type: {}\nGood Processed: {}\nWorker Spaces: {}\nSize: {}"
                        "\nCost: {}\nQuarries Allowed: {}\nVP: {}".format(self.name,
                                                                          self.perk_description,
                                                                          self.building_type,
                                                                          self.good_processed,
                                                                          self.free_worker_spaces,
                                                                          self.size,
                                                                          self.base_cost,
                                                                          self.quarries_allowed,
                                                                          self.vp_value))

    class Plantations(object):
        def __init__(self, plantation_dict, quarries, number_of_players):
            self.number_of_players = number_of_players
            self.face_down_pool = []
            for plantation, number in plantation_dict.items():
                self.face_down_pool += [plantation] * number
            self.face_up_pool = []
            self.discard_pool = []
            self.quarries = quarries
            self.draw_new_tiles()
        def plantation_taken(self, plantation):
            if plantation in self.face_up_pool:
                self.face_up_pool.remove(plantation)
                return plantation
            return None
        def quarry_taken(self):
            if self.quarries > 0:
                self.quarries -= 1
                return 'quarry'
            return None
        def draw_new_tiles(self):
            self.discard_pool += self.face_up_pool
            self.face_up_pool.clear()
            if len(self.face_down_pool) == 0:
                self.face_down_pool += self.discard_pool
                self.discard_pool.clear()
            while len(self.face_up_pool) < (self.number_of_players + 1):
                self.face_up_pool += [self.face_down_pool.pop(random.randrange(len(self.face_down_pool)))]
                if len(self.face_down_pool) == 0:
                    self.face_down_pool += self.discard_pool
                    self.discard_pool.clear()
            return None

    class TradingPost():
        def __init__(self):
            self.trading_queue = []
        def add_barrel(self, good_type):
            if len(self.trading_queue) < 4:
                self.trading_queue.append(good_type)
                return good_type

    class ColonistShip(object):
        def __init__(self, colonists, number_of_players):
            self.colonists_carried = number_of_players
            self.colonists_supply = colonists - number_of_players
    
    class Supply(object):
        def __init__(self, barrel_dict, vp):
            self.barrels = barrel_dict
            self.vp = vp
    
    def check_vp_supply(self):
        if self.supply.vp <= 0:
            self.endgame_trigger = True

    def empty_trading_queue(self):
        while self.trading_post.trading_queue:
            self.supply.barrels[self.trading_post.trading_queue.pop()] += 1
        return None
    
    def new_colonist_voyage(self, new_colonists):
        if self.colonist_ship.colonists_supply > new_colonists:
            self.colonist_ship.colonists_supply -= new_colonists
            self.colonist_ship.colonists_carried += new_colonists
        else:
            self.colonist_ship.colonists_carried += self.colonist_ship.colonists_supply
            self.colonist_ship.colonists_supply = 0
            self.endgame_trigger = True
