#Shows info about passed item
screen item_display(item):
    frame:
        xysize (400, 650)
        align (1.0, 0.13)
        vbox:
            image item.pic
            text "{b}{i}[item.name]{/i}{/b}":
                size 30
            text "[item.bio]":
                size 20

screen inventory_display():
    frame:
        xysize (1200, 650)
        align (0, 0.13)
        hbox:
            align (0.015, 0.015)
            spacing 15
            for item in player_inventory.held_items:
                imagebutton:
                    idle item.pic
                    hover item.pic
                    action NullAction()
                    hovered Show("item_display", item = item)
                    unhovered Hide("item_display")
    
    # imagebutton:
    #     xysize (10, 10)
    #     align (0.1, 0.16)
    #     idle player_inventory.held_items[0].pic
    #     hover player_inventory.held_items[0].pic