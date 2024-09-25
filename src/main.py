from algorithms import NearestNeighbour, SimulatedAnnealing, HillClimbing, TabuSearch, Genetic
from utils import load_data, draw_path


def main():
    distances = load_data('src/data/TSP2.xlsx')

    nn = NearestNeighbour()
    results = nn.solve(distances, start_city=19)
    draw_path(distances, results, 'Nearest Neighbour')

    # sa = SimulatedAnnealing(7000, 0, 1000, neighbourhood='swap', cooling='arithmetic')
    # results = sa.solve(distances)
    # draw_path(distances, results, 'Simulated Annealing')

    # hc = HillClimbing(100, 1000, 1000, neighbourhood='swap')
    # results = hc.solve(distances)
    # draw_path(distances, results, 'Hill Climbing')

    # ts = TabuSearch(100, 10, 16, neighbourhood='swap')
    # results = ts.solve(distances)
    # draw_path(distances, results, 'Tabu Search')


if __name__ == "__main__":
    main()