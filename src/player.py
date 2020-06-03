# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return (f'Welcome {self.name}! You have taken the red pill and have woken up {self.current_room.name}. Shall we see how far the rabbit hole goes?')