import os
import pandas as pd
from .factories.VisualizationFactory import VisualizationFactory

file_path = "/Users/marichka/labs-python/lab_8/data/people.csv"

print(f"Trying to load file from: {file_path}")

import os
import pandas as pd
from .factories.VisualizationFactory import VisualizationFactory

class CSVVisualization:
    def __init__(self):
        self.visualization_factory = VisualizationFactory()

    def load_data(self, file_path: str) -> pd.DataFrame:
        if not os.path.isfile(file_path):
            print(f"Файл {file_path} не знайдено.")
            return None
        try:
            data = pd.read_csv(file_path)
            print("Дані успішно завантажено.")
            return data
        except Exception as e:
            print(f"Помилка при завантаженні CSV: {e}")
            return None

    def visualize_data(self, data: pd.DataFrame, visualization_type: str, x: str, y: str):
        try:
            strategy = self.visualization_factory.create_strategy(visualization_type)
            if x not in data.columns or y not in data.columns:
                print(f"Одна з колонок ({x}, {y}) не знайдена в даних.")
                return
            data_x = pd.to_numeric(data[x], errors="coerce")
            data_y = pd.to_numeric(data[y], errors="coerce")
            if data_x.isnull().any() or data_y.isnull().any():
                print("У даних є некоректні значення.")
                return
            strategy.visualize(data_x, data_y)
        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Помилка: {e}")
