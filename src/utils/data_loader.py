from pandas import read_excel
from numpy import delete, ndarray


def load_data(path_to_data: str) -> ndarray:
    try:
        data = read_excel(r'' + path_to_data, engine = 'openpyxl')
    except Exception as e:
        print(f'An error occurred while attempting to open the xlsx file from {path_to_data}: {e}')
        return None
    
    return delete(data.to_numpy(), 0, 1)