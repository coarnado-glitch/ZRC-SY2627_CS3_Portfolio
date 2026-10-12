class PshsGalaxy:
    def __init__(self, universal_id, home_sector):
        self.universal_id = universal_id
        self.home_sector = home_sector

    def get_galactic_clearance(self):
        return (f"ID {self.universal_id} is cleared to travel across sector {self.home_sector}.")
    


class Nationality(PshsGalaxy):
    def __init__(self, universal_id, home_sector, country_of_origin, passport_number):
        super().__init__(universal_id, home_sector)
        self.country_of_origin = country_of_origin
        self.passport_number = passport_number

    def human_greeting(self):
        return f"Hello! I am from {self.country_of_origin}. My Earth passport is {self.passport_number}."

class Alien(PshsGalaxy):
    def __init__(self, universal_id, home_sector, species_name, homep_planet, special_ability):
        super().__init__(universal_id, home_sector)
        self.species_name = species_name
        self.homeplanet = homep_planet
        self.special_ability = special_ability

        def alien_greeting(self):
            return f"Greetings, Earthling. I am a {self.species_name} capable of {self.special_ability}."

class Filipinos(Nationality):
    def __init__(self, universal_id, home_sector, passport_number, native_dialect):
        super().__init__(universal_id, home_sector, "Philippines", passport_number)
        self.native_dialect = native_dialect

    def specific_greeting(self):
        return f"Kamusta! I speak {self.native_dialect}."

class Indonesians(Nationality):
    def __init__(self, universal_id, home_sector, passport_number, favorite_food):
        super().__init__(universal_id, home_sector, "Indonesia", passport_number)
        self.favorite_food = favorite_food

    def specific_greeting(self):
        return f"Halo! My favorite dish back home is {self.favorite_food}."

class Spaniards(Nationality):
    def __init__(self, universal_id, home_sector, passport_number, home_city):
        super().__init__(universal_id, home_sector, "Spain", passport_number)
        self.home_city = home_city

    def specific_greeting(self):
        return f"¡Hola! I am from the beautiful city of {self.home_city}."



class Marvelous(Alien):
    def __init__(self, universal_id, home_sector, species_name, home_planet, special_ability, favorite_color):
        super().__init__(universal_id, home_sector, species_name, home_planet, special_ability)
        self.favorite_color = favorite_color

        def specific_greeting(self):
            return f"Greetings, Earthling. I am a {self.species_name} from {self.homeplanet}, capable of {self.special_ability}. My favorite color is {self.favorite_color}."

class Avengers(Alien):
    def __init__(self, universal_id, home_sector, species_name, home_planet, special_ability, favorite_weapon):
        super().__init__(universal_id, home_sector, species_name, home_planet, special_ability)
        self.favorite_weapon = favorite_weapon

        def specific_greeting(self):
            return f"Greetings, Earthling. I am a {self.species_name} from {self.homeplanet}, capable of {self.special_ability}. My favorite weapon is {self.favorite_weapon}."