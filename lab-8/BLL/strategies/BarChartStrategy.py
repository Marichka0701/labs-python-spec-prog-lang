
from ...interfaces.VisualizationInterface import VisualizationInterface
import matplotlib.pyplot as plt

class BarChartStrategy(VisualizationInterface):
    def visualize(self, data_x, data_y):
        if len(data_x) != len(data_y):
            raise ValueError("Дані для графіка некоректні.")
        plt.bar(data_x, data_y)
        plt.xlabel("Категорії")
        plt.ylabel("Значення")
        plt.title("Стовпчастий графік")
        plt.show()
