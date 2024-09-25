from numpy import ndarray
from random import shuffle, sample
from utils import calculate_energy, neighbourhood_methods_dict


class HillClimbing:
    def __init__(self, multistarts: int, iterations1: int, iterations2: int, neighbourhood: str):
        self.multistarts = multistarts
        self.iterations1 = iterations1
        self.iterations2 = iterations2
        self.neighbourhood_type = neighbourhood
        self.neighbourhood_method = neighbourhood_methods_dict[self.neighbourhood_type]
        self.route = []
        self.energy = 0


    def solve(self, distances: ndarray) -> tuple:
        self.route = list(range(distances.shape[0]))
        i = 0

        while i < self.multistarts:
            shuffle(self.route)
            current_energy = calculate_energy(self.route, distances)
            j = 0

            while j < self.iterations1:
                min_route = self.route.copy()
                min_energy = current_energy
                k = 0

                while k < self.iterations2:
                    new_route = self.route.copy()
                    city1, city2 = sample(new_route, 2)
                    idx_city1, idx_city2 = new_route.index(city1), new_route.index(city2)

                    if self.neighbourhood_type == 'swap':
                        new_route = self.neighbourhood_method(new_route, idx_city1, idx_city2)
                    elif self.neighbourhood_type == 'insertion':
                        new_route = self.neighbourhood_method(new_route, city1, idx_city2)

                    new_energy = calculate_energy(new_route, distances)

                    if new_energy < min_energy:
                        min_route, min_energy = new_route.copy(), new_energy
                    
                    k += 1
                
                if min_route == self.route is True:
                    break

                self.route = min_route
                current_energy = min_energy
                j += 1

            i += 1
        
        self.energy = current_energy + distances[self.route[-1]][self.route[0]]
        self.route.append(self.route[0])

        return (self.route, self.energy)