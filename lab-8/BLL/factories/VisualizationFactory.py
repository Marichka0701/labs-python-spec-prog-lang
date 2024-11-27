from ...BLL.strategies.LineChartStrategy import LineChartStrategy
from ...BLL.strategies.BarChartStrategy import BarChartStrategy
from ...interfaces.VisualizationInterface import VisualizationInterface

class VisualizationFactory:
    def create_strategy(self, choice: str) -> VisualizationInterface:
        match choice.lower():
            case "line":
                return LineChartStrategy()
            case "bar":
                return BarChartStrategy()
            case _:
                raise ValueError("Невідомий вибір стратегії візуалізації")
