from pandas import read_excel
from numpy import delete, ndarray

def load_data(path_to_data: str) -> ndarray:
    data = read_excel(r'' + path_to_data, engine = 'openpyxl')
    return delete(data.to_numpy(), 0, 1)