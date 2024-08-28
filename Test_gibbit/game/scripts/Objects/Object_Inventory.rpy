init python:
    class Item:
        def __init__(self, name, pic, bio):
            self.name = name
            self.pic = im.Scale(pic, 100, 100) #Enforce standard item image size
            self.bio = bio

        def hi(self):
            return "Heya, my name is " + self.name + "!"

    class Inventory:
        def __init__(self):
            self.held_items = []
            self.size = 0

        def add_item(self, item: Item):
            self.held_items.append(item)
            self.size += 1

        def remove_item(self, item: Item):
            self.held_items.remove(item)
            self.size -= 1

        def item_list(self):
            names = ""
            if len(self.held_items) <= 0:
                names += "ack"
            for item in self.held_items:
                names += item.name
            return names

        #def contains(self, item):
            

        
