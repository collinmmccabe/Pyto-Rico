import random

class Market(object):
    def __init__(self, colonists, vp, barrel_dict, plantation_list, quarries, building_dict, prospectors, ship_size_list):
        self._endgame_trigger = False
        self.building_supply = Buildings()
        self._buildings = Buildings(building_dict)
        self._plantations = Plantations(plantation_list, quarries)
        self._role_options = RoleOptions(prospectors)
        self._trading_post = TradingPost()
        self._captain_ships = CaptainShips(ship_size_list)
        self._colonist_ship = ColonistShip(colonists)
        self._supply = Supply(barrel_dict, vp)
