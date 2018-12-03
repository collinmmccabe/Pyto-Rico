from market import Market
from player_flat_class import Player
from starting_setup import player_init, setup_dict

#new_colonists = min(sum([j.free_worker_spaces for j in i._building_list for i in player_list]), len(player_list))

def main():
    print("Welcome to Pyto Rico! Pyto Rico is played with 2 to 6 players. "
          "Let's start by getting all the players' names.")
    player_names = []; another = True
    while another:
        print("Name:", end = " ")
        player_names.append(input())
        print("Would you like to add another player? [y/n]:", end = " ")
        response = input()
        if response in ["y", "Y", "yes", "Yes", "YES", "yeah", "Yeah", "YEAH"]:
            another = True
        elif response in ["n", "N", "no", "No", "NO", "nope", "Nope", "NOPE"]:
            another = False
        if len(player_names) == 1 and not another:
            print("You need more than 1 player for Pyto Rico...")
            another = True
        if len(player_names) == 6 and another:
            print("You can't play Pyto Rico with more than 6 players...")
            another = False

    print("Alright! It looks like we are playing with {} players.".format(len(player_names)))
    print("Since {} is the first player, they'll start as the governor.".format(player_names[0]))
    print("Everyone will start with {} doubloons, and the starting plantations "
          "are as follows:".format(player_init[len(player_names)][0]["doubloons"]))
    player_dict = {}
    for index, name in enumerate(player_names):
        print("{}: {}".format(name, player_init[len(player_names)][index]["first_plantation"]))
        player_dict[name] = Player(name, player_init[len(player_names)][index])
    
    print(player_dict)

    print("And here's the starting marketplace:")
    market = Market(setup_dict[len(player_dict)], len(player_dict))
    print(market.plantations.face_up_pool)
    market.trading_post.add_barrel('corn')
    market.empty_trading_queue()

if __name__ == '__main__':
   main()