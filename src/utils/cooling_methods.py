from math import sqrt


def arithmetic_cooling(temperature: float) -> float:
    return temperature - 1


def geometric_cooling(temperature: float) -> float:
    return temperature * 0.999


def quadratic_multiplicative_cooling(temperature: float, iterations: int) -> float:
    return temperature / (1 + 0.0001 * sqrt(iterations))


def linear_multiplicative_cooling(temperature: float, iterations: int) -> float:
    return temperature / (1 + 0.0001 * iterations)


# Mapping cooling method names to functions
cooling_methods_dict = {
    'arithmetic': arithmetic_cooling,
    'geometric': geometric_cooling,
    'quadratic_multiplicative': quadratic_multiplicative_cooling,
    'linear_multiplicative': linear_multiplicative_cooling
}