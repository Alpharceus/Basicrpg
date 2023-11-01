import random
import tkinter as tk

# Here are our lists of creatures, items, and other things.
CREATURES = ['monster', 'rabbit', 'fox', 'rat']
ITEMS = ['helmet', 'shield', 'boots', 'chest plate', 'gauntlets']
OTHER_THINGS = ['bush', 'big tree', 'rock']
ALL_THINGS = CREATURES + ITEMS + OTHER_THINGS  # We're combining all the lists into one big list.

# We're setting our player's starting stats.
player_health = 20
player_items = []
player_coins = 0

# Setting up a small window to show our player's stats.
root = tk.Tk()
root.title("Player Stats")

health_label = tk.Label(root, text=f"Health: {player_health}")
health_label.pack()

items_label = tk.Label(root, text=f"Items: {', '.join(player_items)}")
items_label.pack()

coins_label = tk.Label(root, text=f"Coins: {player_coins}")
coins_label.pack()

def update_gui():
    """This function will update our player's stats in the window."""
    health_label.config(text=f"Health: {player_health}")
    items_label.config(text=f"Items: {', '.join(player_items)}")
    coins_label.config(text=f"Coins: {player_coins}")
    root.update()

root.after(1000, update_gui)  # We're telling our window to update the stats every second.
root.update()

# Now, let's start our game!
while True:
    encountered_thing = random.choice(ALL_THINGS)  # We're choosing a random thing from our big list.
    
    # Let's check if the thing we encountered is an item.
    if encountered_thing in ITEMS and encountered_thing not in player_items:
        response = input(f"Look, there's a {encountered_thing} over there! Do you want to pick it up? (Y/n) ")
        if response.lower() != 'n':
            player_items.append(encountered_thing)
            print(f"Great! You've picked up a {encountered_thing}.")
    
    # Now let's check if it's a creature.
    elif encountered_thing in CREATURES:
        if encountered_thing == 'monster':
            attack_amount = 7 - len([i for i in player_items if i in ['helmet', 'shield', 'chest plate', 'gauntlets']])
            player_health -= attack_amount
            print(f"Oh no! A wild {encountered_thing} has attacked you and you lost {attack_amount} health.")
            
            if player_health <= 0:
                print("Sorry, you've been defeated. Better luck next time!")
                break

            response = input(f"Do you want to fight back against the {encountered_thing}? (Y/n) ")
            if response.lower() != 'n':
                player_coins += 10
                print(f"Bravo! You've defeated the {encountered_thing} and earned 10 coins!")
        else:
            response = input(f"A wild {encountered_thing} appeared. Do you want to chase it away? (Y/n) ")
            if response.lower() != 'n':
                player_coins += 1
                print(f"You chased away the {encountered_thing} and found a coin!")

    # Checking if player has collected enough coins to win the game.
    if player_coins >= 100:
        print("Hooray! You've collected enough coins and you're the winner!")
        break

    update_gui()  # After each turn, we update the player's stats in the window.
    input("Take a deep breath and press ENTER to continue your journey.")

print("Thanks for playing our little game! Hope you had fun!")
root.destroy()  # We close the stats window.
