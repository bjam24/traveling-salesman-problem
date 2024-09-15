from numpy import ndarray


def calculate_energy(route: list, distances: ndarray) -> int:
        new_energy = 0

        for i in range(len(route) - 1):
            first_city, second_city = route[i], route[i + 1]
            new_energy += distances[first_city, second_city]
        
        new_energy += distances[route[-1], route[0]]

        return new_energy