from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons", ["Saber"]),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""", ["Spoon"]
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["Helmet"]
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["Map", "Shield"]
    ),
}

items = {
    "saber": Item("Saber", "A classy weapon to protect you from any foes"),
    "helmet": Item("Helmet", "Proects you from overhead damage"),
    "spoon": Item("Spoon", "This isn't worth very much"),
    "shield": Item("Shield", "Useful to defend against any foes"),
    "map": Item("Map", "A guide to your next adventure!")
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#Start Game
name = input("Enter your name: ")

player = Player(name, room["outside"])
print(player)
print("All you have to do to wake up again is press 'q'")

#Game Parameters
redPill = True
playerControls = ["n", "e", "s", "w", "q"]
checkItems = player.checkInventory()

#Game Mechanics

while redPill == True:
    print(f"{name}, you're currently standing in the {player.current_room.name}. \n{player.current_room.description}.")
    move = input("Which way shall we go?")
    if move == "q":
        exit()
    if move == "check items":
        if len(checkItems):
            print(f"These are the items you're carrying: {checkItems}")
        else:
            print(f"You're currently not holding any items. Anyway, back to where we were...")
    if move == "look around":
        if len(player.current_room.items) > 0:
            print(f"{player.current_room.items}")
            print(f"If you would like to pick up the item, type it's name.")
            continue
        else:
            print(f"Let's move on, there's nothing to gain here.")
    getItem = move.split(" ")[0]
    if getItem in (player.current_room.items):
            player.get(getItem)
            print(f"{getItem} added to your inventory.")       
    if "drop" in move:
        if len(player.inventory) > 0:
            dropItem = move.split(" ")[1]
            if dropItem in (player.inventory):
                player.drop(dropItem)
            print(f"You've dropped {dropItem}")
        else:
            print(f"You're not carrying anything at the moment.")
    elif move == "n":
        if player.current_room == room["outside"]:
            player.current_room = getattr(player.current_room, 'n_to')
        elif player.current_room == room["foyer"]:
            player.current_room = getattr(player.current_room, 'n_to')
        elif player.current_room == room["narrow"]:
            player.current_room = getattr(player.current_room, 'n_to')
        else:
            print("Hmm, I don't think we should go that way. Enter one of the following commands to get going: \nn => Go North \ne => Go East \ns => Go South \nw => Go West")
    elif move == "e":
        if player.current_room == room["foyer"]:
            player.current_room = getattr(player.current_room, 'e_to')
        else:
            print("Hmm, I don't think we should go that way. Enter one of the following commands to get going: \nn => Go North \ne => Go East \ns => Go South \nw => Go West")
    elif move == "s":
        if player.current_room == room["foyer"]:
            player.current_room = getattr(player.current_room, 's_to')
        if player.current_room == room["overlook"]:
            player.current_room = getattr(player.current_room, 's_to')
        if player.current_room == room["treasure"]:
            player.current_room = getattr(player.current_room, 's_to')
        else:
            print("Hmm, I don't think we should go that way. Enter one of the following commands to get going: \nn => Go North \ne => Go East \ns => Go South \nw => Go West")
    elif move == "w":
        if player.current_room == room["narrow"]:
            player.current_room = getattr(player.current_room, 'w_to')
        else:
            print("Hmm, I don't think we should go that way. Enter one of the following commands to get going: \nn => Go North \ne => Go East \ns => Go South \nw => Go West")
if redPill == False:
    print(f"***{name} wakes up*** What a weird dream!")