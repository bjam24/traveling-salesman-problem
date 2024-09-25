from numpy import ndarray
from random import shuffle, random, sample 
from utils import neighbourhood_methods_dict, calculate_energy


class TabuSearch:
    def __init__(self, iterations: int, tabu_limit: int, neighbourhood_size: int, neighbourhood: str):
        self.iterations = iterations
        self.neighbourhood_size = neighbourhood_size
        self.neighbourhood_type = neighbourhood
        self.neighbourhood_method = neighbourhood_methods_dict[self.neighbourhood_type]
        self.tabu_limit = tabu_limit
        self.tabu = []
        self.route = []
        self.energy = 0


    def candidates_generator(self, distances: ndarray) -> list:
        candidates = []
        k = 0

        while k != self.neighbourhood_size:
            new_route = self.route.copy()
            city1, city2 = sample(new_route, 2)
            idx_city1, idx_city2 = new_route.index(city1), new_route.index(city2)

            if self.neighbourhood_type == 'swap':
                new_route = self.neighbourhood_method(new_route, idx_city1, idx_city2)
            elif self.neighbourhood_type == 'swap':
                new_route = self.neighbourhood_method(new_route, city1, idx_city2)

            new_energy = calculate_energy(new_route, distances)
            candidates.append((new_route, city1, city2, new_energy))
            k += 1

        return candidates


    def solve(self, distances: ndarray) -> tuple:
        self.route = list(range(distances.shape[0]))
        shuffle(self.route)  # Shuffle initial route
        self.energy = calculate_energy(self.route, distances)
        i = 0

        while i != self.iterations:
            candidates = self.candidates_generator(distances)
            min_route = self.route
            min_energy = self.energy
            tabu_pair = ()

            for new_route, city1, city2, new_energy in candidates:
                if (city1, city2) not in self.tabu and (city2, city1) not in self.tabu:

                    if new_energy < min_energy:
                        min_route = new_route
                        min_energy = new_energy
                        tabu_pair = (city1, city2)

            if min_energy < self.energy:
                self.route = min_route
                self.energy = min_energy
                self.tabu.append(tabu_pair)

            if len(self.tabu) > self.tabu_limit:
                self.tabu.pop(0)

            i += 1

        self.energy += distances[self.route[-1]][self.route[0]]
        self.route.append(self.route[0])

        return (self.route, self.energy)