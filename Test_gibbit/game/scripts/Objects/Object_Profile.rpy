init python:
    class Profile:
        def __init__(self):
            self.skills = {"History": 0, "Occultism": 0, "Manipulation": 0, "Tact": 0, "Presence": 1}
            #Sort dictionary alphabetically
            self.skills = dict(sorted(self.skills.items()))

        def print_skills(self):
            # f-string allows us to easily include variables in string (e.g. {variable_name})
            [print(f"{key}: {value}") for key, value in self.skills.items()]

        def skillcheck(self, skill):
            for key, value in self.skills.items():
                # Return the key if the value matches
                if skill.lower() in key.lower():
                    return value

        def mod_skill(self, skill, mod):
            for key, value in self.skills.items():
                # Return the key if the value matches
                if skill.lower() in key.lower():
                    self.skills[key] += mod
                    return

        def set_skill(self, skill, new_val):
            for key, value in self.skills.items():
                # Return the key if the value matches
                if skill.lower() in key.lower():
                    self.skills[key] = new_val
                    return