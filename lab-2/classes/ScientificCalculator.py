class ScientificCalculator(Calculator):
    def sin(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        result = math.sin(angle_radians)
        self.add_to_history(f"sin({angle_degrees}) = {result}")
        return round(result, self.get_decimal_places())