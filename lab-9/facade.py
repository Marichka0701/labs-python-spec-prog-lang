
from lab-1.main import main as lab1_main
from lab-2.main import main as lab2_main
from lab-3.main import main as lab3_main
from lab-4.main import main as lab4_main
from lab-5.main import main as lab5_main
from lab-7.main import main as lab7_main
from lab-8.main import main as lab8_main

class RunnerFacade:
    def __init__(self):
        self.labs = {
            1: self.run_lab1,
            2: self.run_lab2,
            3: self.run_lab3,
            4: self.run_lab4,
            5: self.run_lab5,
            7: self.run_lab7,
            8: self.run_lab8,
        }

    def show_menu(self, menu):
        print(menu)

    def run_lab(self, choice):
        if choice in self.labs:
            self.labs[choice]()
        elif choice == 0:
            print("Вихід із програми.")
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    def run_lab1(self):
        lab1_main()

    def run_lab2(self):
        lab2_main()

    def run_lab3(self):
        lab3_main()

    def run_lab4(self):
        lab4_main()

    def run_lab5(self):
        lab5_main()

    def run_lab7(self):
        lab7_main()

    def run_lab8(self):
        lab8_main()
