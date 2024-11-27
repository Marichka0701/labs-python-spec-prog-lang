import os
import math
import random
import GlobalVariables as Global
from pyfiglet import figlet_format, FigletFont


class Ascii:
    @staticmethod
    def verify_width(width):
        if width <= 0:
            try:
                return os.get_terminal_size().columns
            except OSError:
                return 220
        elif width > 0:
            return width
        else:
            return 220

    @staticmethod
    def print(text, is_random=False):
        if is_random:
            font = random.choice(FigletFont.getFonts())
            color = "\033[" + str(random.randint(31, 39)) + "m"
        else:
            font = Global.font
            color = Global.color
        
        art = figlet_format(text, font=font, width=Global.width)
        
        print(color + art + Global.color_reset)