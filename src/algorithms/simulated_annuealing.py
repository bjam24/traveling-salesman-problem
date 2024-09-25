from numpy import ndarray
from random import shuffle, random, sample 
from utils import cooling_methods_dict, neighbourhood_methods_dict, calculate_energy
from math import exp


class SimulatedAnnealing:
    def __init__(self, start_temperature: int, min_temperature: int, iterations: int, neighbourhood: str, cooling: str):
        self.temperature = start_temperature
        self.min_temperature = min_temperature
        self.iterations = iterations
        self.neighbourhood_type = neighbourhood
        self.neighbourhood_method = neighbourhood_methods_dict[self.neighbourhood_type]
        self.cooling_type = cooling
        self.cooling_method = cooling_methods_dict[self.cooling_type]
        self.route = []
        self.energy = 0
    

    def solve(self, distances: ndarray) -> tuple:
        self.route = list(range(distances.shape[0]))
        shuffle(self.route)
        self.energy = calculate_energy(self.route, distances)

        while self.temperature > self.min_temperature:
            i = 0

            while i != self.iterations:
                city1, city2 = sample(self.route, 2)
                idx_city1, idx_city2 = self.route.index(city1), self.route.index(city2)

                if self.neighbourhood_type == 'swap':
                    self.route = self.neighbourhood_method(self.route, idx_city1, idx_city2)
                if self.neighbourhood_type == 'insertion':
                    self.route = self.neighbourhood_method(self.route, city1, idx_city2)

                new_energy = calculate_energy(self.route, distances)
                change_cost = new_energy - self.energy

                if change_cost < 0:
                    self.energy = new_energy
                elif random() < exp(-change_cost / self.temperature):
                    self.energy = new_energy
                elif self.neighbourhood_type == 'swap':
                    self.route = self.neighbourhood_method(self.route, idx_city1, idx_city2)

                i += 1

            if self.cooling_type in ['quadratic_multiplicative', 'linear_multiplicative']:
                self.temperature = self.cooling_method(self.temperature, self.iterations)
            else:
                self.temperature = self.cooling_method(self.temperature)

        self.energy += distances[self.route[-1]][self.route[0]]
        self.route.append(self.route[0])
        return (self.route, self.energy)