
import matplotlib.pyplot as plt
from ...interfaces.VisualizationInterface import VisualizationInterface

class LineChartStrategy(VisualizationInterface):
    def visualize(self, data_x, data_y):
        if len(data_x) != len(data_y):
            raise ValueError("Дані для графіка некоректні.")
        plt.plot(data_x, data_y, label="Лінійний графік")
        plt.xlabel("X (вісь)")
        plt.ylabel("Y (вісь)")
        plt.title("Лінійний графік даних")
        plt.legend()
        plt.show()
