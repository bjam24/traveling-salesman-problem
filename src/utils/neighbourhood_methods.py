
def swap_method(route:list, idx1: int, idx2: int) -> list:
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route


def insertion_method(route: list, city1: int, idx2: int) -> list:
    route.remove(city1)
    route.insert(idx2, city1)
    return route

# Mapping neighbourhood method names to functions
neighbourhood_methods_dict = {
    'swap': swap_method,
    'insertion': insertion_method
}