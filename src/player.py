# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return (f'Welcome {self.name}! You have taken the red pill and have woken up at {self.room}. Shall we see how far the rabbit hole goes?')