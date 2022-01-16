import pygame
from Main.classes.planets.Planet import Planet


class PlanetsConfigurationResolver:
    def __init__(self, center):
        self.center = center
        self.planets = []
        with open("classes/planets/planets_configuration", "r") as file:
            for i in file:
                planet_string = i.strip(" \n,.")
                if planet_string != "" and not planet_string.startswith("#"):
                    self.planets.append(PlanetsConfigurationResolver.planet_resolver(planet_string))
        self.planet_center_resolver()

    @staticmethod
    def planet_resolver(planet_string):
        planet_list = planet_string.split()
        return Planet(planet_list[0],
                      int(planet_list[1]),
                      int(planet_list[2]),
                      float(planet_list[3]),
                      float(planet_list[4]),
                      pygame.color.THECOLORS[planet_list[5]],
                      planet_list[6]
                      )

    def planet_center_resolver(self):
        for planet in self.planets:
            for other_planet in self.planets:
                if planet.center == other_planet.name:
                    planet.center = other_planet
            if isinstance(planet.center, str):
                planet.center = self.center


if __name__ == "__main__":
    x = PlanetsConfigurationResolver((12, 12))
    print(x.planets[0].center)
    print(x.planets[1].center)
