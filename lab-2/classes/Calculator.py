import math

from classes.ConsoleReader import ConsoleReader
from classes.ConsoleWriter import ConsoleWriter
from functions.calculate import calculate
from functions.perform_calculation import perform_calculation

class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []
        self.decimal_places = 2  # Default decimal places