class DictRef(dict):
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, value):
        self[key] = value

class Player(object):
    def __init__(self, name):
        self.name = name
        self.doubloons = 0
        self.vp = 0
        self.free_colonists = 0
        self.governor_flag = False
        self.island = self.Island()
        self.city = self.City()
        self.supply = self.Barrels()

    class Island(DictRef):
        def __init__(self):
            for n in range(1, 13):
                setattr(self, 'plot_' + str(n).zfill(2), None)  # i.e. self.plot_01 = Plantation()

        def swap_plots(self, from_plot, to_plot):
            self[from_plot], self[to_plot] = self[to_plot], self[from_plot]
            return None
        def plots_built(self):
            return sum(1 for i in self.values() if i is not None)
        def build(self, island_plot, good_produced):
            if ((self.plots_built() < 12) and (self[island_plot] is None)):
                self[island_plot] = self.Plantation(good_produced)
            return None

        class Plantation(DictRef):
            def __init__(self, good_produced):
                self.good_produced = good_produced
                self.occupied = False
    
    class City(DictRef):
        def __init__(self):
            for n in range(1, 13):
                setattr(self, 'plot_' + str(n).zfill(2), None)  # i.e. self.plot_01 = Building()

        def swap_plots(self, from_plot, to_plot):
            if ((self[from_plot] is not None) and (self[from_plot].size == 2)):
                from_plot_plus_one = 'plot_' + str(int(from_plot[-2:]) + 1).zfill(2)
                to_plot_plus_one = 'plot_' + str(int(to_plot[-2:]) + 1).zfill(2)
                self.move_building(from_plot_plus_one, to_plot_plus_one)
            self[from_plot], self[to_plot] = self[to_plot], self[from_plot]
            return None
        def plots_built(self):
            return sum(1 for i in self.values() if i is not None)
            
        class Building(DictRef):
            def __init__(self, building_lookup):
                self.building_name = building_lookup.name
                self.size = building_lookup.size
                self.good_processed = building_lookup.good_processed
                self.free_worker_spaces = building_lookup.free_worker_spaces
                self.occupied_worker_spaces = 0
    
    class Barrels(DictRef):
        def __init__(self):
            self.corn = 0
            self.indigo = 0
            self.sugar = 0
            self.tobacco = 0
            self.coffee = 0
    
    def lose_doubloons(self, number):
        if self.doubloons >= number:
            self.doubloons -= number
            return number
        return None
    def get_doubloons(self, number):
        self.doubloons += number
        return number
    def get_vp(self, number):
        self.vp += number
        return number
    def get_colonists(self, number):
        self.free_colonists += number
        return None
    def set_governor_flag(self, bool_value):
        self.governor_flag = bool_value
        return None
    
    def produce_plantation(self, market_supply_dict):  # send the market supply here to communicate with fn
        taken = min(sum(1 for i in self.island if (i.good_produced == 'corn' and i.occupied)), market_supply_dict.corn)
        market_supply_dict.corn -= taken
        self.supply.corn += taken
        for good_type in ['indigo', 'sugar', 'tobacco', 'coffee']:  # could replace list with keys of mkt spl d
            taken = min(min(sum(1 for i in self.island if (i.good_produced == good_type and i.occupied)), 
                            sum(j.occupied_worker_spaces for j in self.city if j.good_processed == good_type)), 
                        market_supply_dict[good_type])
            market_supply_dict[good_type] -= taken
            self.supply[good_type] += taken
        # Maybe use return value to communicate with Market class?
        return market_supply_dict
    def add_colonist_plantation(self, island_plot):
        if ((not self.island[island_plot].occupied) and (self.free_colonists > 0)):
            self.island[island_plot].occupied = True
            self.free_colonists -= 1
        return None
    def remove_colonist_plantation(self, island_plot):
        if self.island[island_plot].occupied:
            self.island[island_plot].occupied = False
            self.free_colonists += 1
        return None
    
    def build_building(self, city_plot, building_lookup, cost):  # specific building lookup is BuildingLookup[building_name]
        endgame_trigger = False
        if ((building_lookup.size + self.occupied_city_plots() <= 12) and (self.city[city_plot] is None) and
          (building_lookup.name not in [i.building_name for i in self.city]) and
          (cost <= self.doubloons)):
            if ((building_lookup.size == 2) and (self.city['plot_' + str(int(city_plot[-2:]) + 1).zfill(2)] is None)):
                self.city['plot_' + str(int(city_plot[-2:]) + 1).zfill(2)] = self.Building({
                                                                                'name': 'second plot for large building',
                                                                                'size': 0,
                                                                                'good_processed': None,
                                                                                'free_worker_spaces': 0 })
                self.city[city_plot] = self.Building(building_lookup)
            elif building_lookup.size == 1:
                self.city[city_plot] = self.Building(building_lookup)
            else:
                return endgame_trigger, None
            if self.occupied_city_plots() == 12:
                endgame_trigger = True
            return endgame_trigger, self.lose_doubloons(cost)  # Use return value to communicate with Market class
        return endgame_trigger, None
    def add_colonist_building(self, city_plot):
        if self.city[city_plot].free_worker_spaces > 0 and self.free_colonists > 0:
            self.city[city_plot].occupied_worker_spaces += 1
            self.city[city_plot].free_worker_spaces -= 1
            self.free_colonists -= 1
        return None
    def remove_colonist_building(self, city_plot):
        if self.city[city_plot].occupied_worker_spaces > 0:
            self.city[city_plot].occupied_worker_spaces -= 1
            self.city[city_plot].free_worker_spaces += 1
            self.free_colonists += 1
        return None

    def ship_resources(self, good, number):
        if self.supply[good] >= number:
            self.supply[good] -= number
            return number, self.get_vp(number)  # this will be used to update Market.Supply[good] and Market.vp
        return None, None
    def trade_resources(self, good):
        trade_value = {'corn': 0, 'indigo': 1, 'sugar': 2, 'tobacco': 3, 'coffee': 4}
        if self.supply[good] > 0:
            self.supply[good] -= 1
            self.get_doubloons(trade_value[good])
            return good  # for TradingPost.trading_queue.append(good)
        return None
