# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def itemDropped(self, item):
        self.items.append(item)

    def itemTaken(self, item):
        self.items.remove(item)

    def __str__(self):
        if len(self.items) > 0:
            return (f"Look {self.items}!") 