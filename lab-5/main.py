from shared.logger import Logger
from .UI.user_interface import UserInterface

def main():
    Logger.log("Лабораторна 5 запущена")
    
    ui = UserInterface()
    ui.start()