import random

# Here are our lists of creatures, items, and other things.
CREATURES = ['monster', 'rabbit', 'fox', 'rat']
ITEMS = ['helmet', 'shield', 'boots', 'chest plate', 'gauntlets']
OTHER_THINGS = ['bush', 'big tree', 'rock']
ALL_THINGS = CREATURES + ITEMS + OTHER_THINGS  # We're combining all the lists into one big list.

def play_game():
    # We're setting our player's starting stats.
    player_health = 20
    player_items = []
    player_coins = 0

    # Now, let's start our game!
    while True:
        encountered_thing = random.choice(ALL_THINGS)  # We're choosing a random thing from our big list.
        
        # Let's check if the thing we encountered is an item.
        if encountered_thing in ITEMS and encountered_thing not in player_items:
            player_items.append(encountered_thing)
    
        # Now let's check if it's a creature.
        elif encountered_thing in CREATURES:
            if encountered_thing == 'monster':
                attack_amount = 7 - len([i for i in player_items if i in ['helmet', 'shield', 'chest plate', 'gauntlets']])
                player_health -= attack_amount
                
                if player_health <= 0:
                    return player_coins, False  # Returns coins earned and a loss status
                
                player_coins += 10
            else:
                player_coins += 1

        # Checking if player has collected enough coins to win the game.
        if player_coins >= 100:
            return player_coins, True  # Returns coins earned and a win status

    return player_coins, False  # Default return (unlikely to be hit)

def main():
    wins = 0
    total_coins = 0

    for _ in range(1000):
        coins, win = play_game()
        total_coins += coins
        wins += win

    win_rate = wins / 10  # Percentage
    avg_coins = total_coins / 1000

    print(f"Win Rate: {win_rate}%")
    print(f"Average Score: {avg_coins}")
    

if __name__ == "__main__":
    main()
    input("Press Enter to close the window...")
