new_colonists = min(sum([j.free_worker_spaces for j in i._building_list for i in player_list]), len(player_list))
