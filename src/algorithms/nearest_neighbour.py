from numpy import ndarray


class NearestNeighbour:
    def __init__(self):
        self.route = []
        self.visited_cities = set()
        self.score = 0

    def solve(self, distances: ndarray, start_city: int) -> tuple:
        n = distances.shape[0]
        self.route = [start_city]
        self.visited_cities = set([start_city])

        while len(self.visited_cities) < n:
            current_city = self.route[-1]
            
            nearest_city, nearest_dist = min(
                [(i, distances[current_city][i]) for i in range(n) if i not in self.visited_cities], 
                key=lambda x: x[1]
            )

            self.route.append(nearest_city)
            self.visited_cities.add(nearest_city)
            self.score += nearest_dist
        
        self.score += distances[self.route[-1]][start_city]
        self.route.append(start_city)
        return (self.route, self.score)