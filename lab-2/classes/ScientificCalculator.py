import math
from classes.Calculator import Calculator

class ScientificCalculator(Calculator):
    def sin(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        result = math.sin(angle_radians)
        self.add_to_history(f"sin({angle_degrees}) = {round(result, self.get_decimal_places())}")
        return round(result, self.get_decimal_places())

    def cos(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        result = math.cos(angle_radians)
        self.add_to_history(f"cos({angle_degrees}) = {round(result, self.get_decimal_places())}")
        return round(result, self.get_decimal_places())
