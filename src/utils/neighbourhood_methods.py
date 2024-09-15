
def swap_method(route:list, idx1: int, idx2: int) -> list:
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

# Mapping neighbourhood method names to functions
neighbourhood_methods_dict = {
    'swap': swap_method
}