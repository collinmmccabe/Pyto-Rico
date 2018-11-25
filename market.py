Class Market
    Class Buildings
        Attr available_buildings = {'small indigo plant’: 3, 'small sugar plant’: 3, …}
        Method building_bought(building)
            If available_buildings[building] > 0, available_buildings[building] -= 1
    Class Plantations
        Attr face_down_pool = [‘corn’, ‘corn’, ‘sugar’, ‘coffee’, ‘coffee’, …]
        Attr face_up_pool = [‘indigo’, ‘corn’, ‘coffee’, ‘coffee’] for 3 players
        Attr discard_pool = (list)
        Attr quarries (int)
        Method draw_new_tiles()
            Move all from face_up_pool to discard_pool, if length(face_down_pool) == 0, move all from discard_pool to face_down_pool (maybe deepcopy then wipe), while length of face_up_pool < (# players + 1): draw 1 random tile from face_down_pool, move that random tile to face)_up_pool, if length(face_down_pool) == 0, move all from discard_pool to face_down_pool
    Class RoleOptions
        Class Role(role_name)
            Attr role_name = role_name
            Attr stored_doubloons = (int)
            Attr taken_flag = (bool)
            Method choose_role(role)
                If not RoleOptions[role].taken_flag, add RoleOptions[role].stored_doubloons to Player.doubloons, set RoleOptions[role].stored_doubloons to 0, set RoleOptions[role].taken_flag to T, do Phase[role_name].full_phase())
    Class TradingPost
        Attr trading_queue (list)
        Method empty_queue()
            For each resource in trading_queue, pop from trading_queue and add 1 of that type back to Supply
    Class CaptainShips
        Class Ship
            Attr free_space = (int)
            Attr used_space = (int)
            Attr good_type = None (str or Enum)
            Method load_ship(good, number)
                If used_space == 0, or if good == Ship.good_type, then Ship.good_type = good, 
    Class ColonistShip
        Attr colonists_carried (int)
        Attr colonists_supply (int)
        Method new_voyage()
            Move colonists from colonists_supply to colonists_carried equal to x = min(total number of unoccupied_squares in all players’ cities, number of players); if colonists_supply <= x, move the total available in colonist supply to carried, endgame_trigger = T)
    Class Supply
        Class Barrels
            Attr corn (int)
            Attr indigo (int)
            Attr sugar (int)
            Attr tobacco (int)
            Attr coffee (int)
        Attr vp (int)
        Attr doubloons (int)
        Method check_vp_supply()
            If vp <= 0, endgame_trigger = T
    Attr endgame_trigger (bool)
