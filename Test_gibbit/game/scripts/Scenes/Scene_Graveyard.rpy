label graveyard_intro():
    #Clears scene of images
    scene
    #Clears screen and adds new background
    scene bg graveyard at background_trans:
        zoom 2.5

    if not graveyard_visited:
        "intro text"

    $ graveyard_visited = True
    
    call screen graveyard_screen

    return

label graveyard_pd():

    #show fx transmission
    #'show' replaces any image with the same tag (e.g. pd love will auto-replace pd normal)
    show pd normal at character_trans behind fx

    amaris "Hey girlybestie."
    amaris "Will you take this rose?"
    
    menu:
        "Despite the whole vibe of this fella, you are tempted to accept..."

        "Sure, they're kinda cute tbh.":
            show fx transmission:
                alpha 0.5
            call graveyard_pd_accept
        "What, no! What the hell, they're terrifying, why the hell would we accept that??? What the fuck???":
            call graveyard_pd_reject
        # "Secret Third Option" if secret_found == TRUE:
        #     call secret

    jump graveyard_intro

    return

label graveyard_pd_accept():
    show pd love at character_trans:
        zoom 0.8

    amaris "hell yeah"
    "{b}cool ending{/b}"

    return

label graveyard_pd_reject():
    amaris "bitch"
    "{b}Bad Ending{/b}."

    return

label test:
    show pd love at character_trans:
        zoom 1.0
    amaris "YOU DID IT, YOU WON! EVERYONE LOVES YOU!"

    return


