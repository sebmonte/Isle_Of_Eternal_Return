init python:
    import random

    class Player:
        def __init__(self, virtue, vice):
            self.skills = {"History": 0, "Occultism": 0, "Manipulation": 0, "Tact": 0, "Presence": 1, "Investigation": 1}
            self.skills = dict(sorted(self.skills.items())) #Sorts dictionary alphabetically
            self.virtue = virtue
            self.vice = vice
            #self.test = [("Okay", 1), ("nokay", 2)] #Another way to do paired lists

            self.effects = {} #Tracks player's current status effects. Treated as a stack (last-in, first-out)

            self.money = 0

            self.location = None #Tracks current player location

        def print_skills(self):
            # f-string allows us to easily include variables in string (e.g. {variable_name})
            [print(f"{key}: {value}") for key, value in self.skills.items()]

        #Checks and returns a skill's level
        def skill_check(self, skill):
            for key, value in self.skills.items():
                # Return the value if the key skill string starts with the given skill 
                if key.lower().startswith(skill.lower()):
                    return value

        #Checks if player has given virtue or vice, returns boolean
        def check_virtueVice(self, name):
            True if name == self.virtue or name == self.vice else False

        #Rolls a skill check, adding the given skill's level and any additional modifiers.
        def skill_roll(self, skill, modifiers):
            print(f"skill: {skill}")
            #Roll 2d6
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)
            print(f"Rolls: {roll1}, {roll2}")
            if roll1 == 6 and roll2 == 6:
                return 999 #Auto-success
            else if roll1 == 1 and roll2 == 1:
                return 0 #Auto-fail
            result = roll1 + roll2
            print(f"before skill mod: {result}")
            #Add skill's level to roll result
            print(self.skill_check(skill))
            result += self.skill_check(skill)
            print(f"after skill mod: {result}")
            #Add modifiers to roll result
            for mod in modifiers:
                result += mod
            print(f"after other mods: {result}")
            return result

        #Temp test function--shouldn't need this in actual game
        def notify_skill_roll(self, skill, modifiers):
            renpy.notify(self.skill_roll(skill, modifiers))

        #Change skill level by given modifier
        def mod_skill(self, skill, mod):
            for key, value in self.skills.items():
                # Return the key if the value matches
                if skill.lower() in key.lower():
                    self.skills[key] += mod
                    return

        #Set skill level to given val
        def set_skill(self, skill, new_val):
            for key, value in self.skills.items():
                # Return the key if the value matches
                if skill.lower() in key.lower():
                    self.skills[key] = new_val
                    return

        #Checks for given virtue/vice and returns given modifier if found.
        # If no bonus is given, gives the default bonus of +2 or -2
        def get_virtueVice_mod(self, virtue_vice, mod = None):
            if virtue_vice.lower() == self.virtue.lower():
                if mod == None:
                    return 2
                else:
                    return mod
            elif virtue_vice.lower() == self.vice.lower():
                if mod == None:
                    return -2
                else:
                    return mod