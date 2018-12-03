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
