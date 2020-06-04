from room import Room
from player import Player

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
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
readyPlayerOne = input("Enter your name: ")

playerOne = Player(readyPlayerOne, room["outside"])
print(playerOne)

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


print("All you have to do to wake up again is press 'q'")


redPill = True

playerControls = ["n", "e", "s", "w", "q"]


while redPill == True:
    print(f"{readyPlayerOne}, you're currently standing in the {playerOne.current_room.name}. \n{playerOne.current_room.description}.")
    moves = input("Which way shall we go?")
    if moves == "q":
        exit()
    elif moves == "n":
        if playerOne.current_room == room["outside"]:
            playerOne.current_room = getattr(playerOne.current_room, 'n_to')
        elif playerOne.current_room == room["foyer"]:
            playerOne.current_room = getattr(playerOne.current_room, 'n_to')
        elif playerOne.current_room == room["narrow"]:
            playerOne.current_room = getattr(playerOne.current_room, 'n_to')
        else:
            print("Hmm, I don't think we should go that way. Enter one of the following commands to get going: \nn => Go North \ne => Go East \ns => Go South \nw => Go West")
    elif moves == "e":
        if playerOne.current_room == room["foyer"]:
            playerOne.current_room = getattr(playerOne.current_room, 'e_to')
        else:
            print("Hmm, I don't think we should go that way. Enter one of the following commands to get going: \nn => Go North \ne => Go East \ns => Go South \nw => Go West")
    elif moves == "s":
        if playerOne.current_room == room["foyer"]:
            playerOne.current_room = getattr(playerOne.current_room, 's_to')
        if playerOne.current_room == room["overlook"]:
            playerOne.current_room = getattr(playerOne.current_room, 's_to')
        if playerOne.current_room == room["treasure"]:
            playerOne.current_room = getattr(playerOne.current_room, 's_to')
        else:
            print("Hmm, I don't think we should go that way. Enter one of the following commands to get going: \nn => Go North \ne => Go East \ns => Go South \nw => Go West")
    elif moves == "w":
        if playerOne.current_room == room["narrow"]:
            playerOne.current_room = getattr(playerOne.current_room, 'w_to')
        else:
            print("Hmm, I don't think we should go that way. Enter one of the following commands to get going: \nn => Go North \ne => Go East \ns => Go South \nw => Go West")
if redPill == False:
    print(f"***{readyPlayerOne} wakes up*** What a weird dream!")