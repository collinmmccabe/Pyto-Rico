import json

# From PEP 351 - Immutable Objects
# TODO: Have an if statement to convert numerical string keys to ints
class ImDict(dict):
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

class SetupDicts(ImDict):
    def __init__(self):
        self.building_lookup = ImDict(json.loads('config/building_lookup.json'))
        # First int key in player_setup is for number of players, second int key is for index of player in player list
        self.player_setup = ImDict(json.loads('config/player_setup.json'))
        # Plantation tile counts in market_setup assume that the starting tiles have already been taken out for players
        # and int keys are for the number of players
        self.market_setup = ImDict(json.loads('config/market_setup.json'))
