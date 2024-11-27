import GlobalVariables as Global
from DAL.functions.artFunctions import draw_char, changeSymbol
from DAL.functions.upload_to_file import file_upload

class Console:
    @staticmethod
    def prompt():
        draw_char("ASCIIFY")
        while True:
            prompt = input("1 - enter text\n"
                           "2 - random font\n"
                           "3 - change symbol\n"
                           "4 - change width and height\n"
                           "5 - change color\n"
                           "Your choice: ")
            match prompt:
                case "1":
                    Console.enter_text()
                case "2":
                    Console.auto_font()
                case "3":
                    Console.change_symbol()
                case "4":
                    Console.change_width_and_height()
                case "5":
                    Console.change_color()
                case _:
                    return

    @staticmethod
    def enter_text():
        text = input("Enter text: ")
        ftext = draw_char(text)
        
        ftext = changeSymbol(ftext, Global.symbol)
        
        print(Global.color + ftext + Global.color_reset)
        
        save_prompt = input("Do you want to save the text? (y/n): ").lower()
        if save_prompt == "y":
            try:
                file_upload(ftext)
            except IOError:
                print("An error occurred during file upload")
                
    @staticmethod
    def change_width_and_height():
        while True:
            width_prompt = input("Enter the width of ASCII art (non-positive to reset): ")
            try:
                width = int(width_prompt)
                if width > 0:
                    Global.width = width
                    print(f"Width changed to {Global.width}")
                else:
                    Global.width = 80  
                    print("Width reset to default")
            except ValueError:
                print("Please enter an integer")
                continue
            
            height_prompt = input("Enter the height of ASCII art (non-positive to reset): ")
            try:
                height = int(height_prompt)
                if height > 0:
                    Global.height = height
                    print(f"Height changed to {Global.height}")
                else:
                    Global.height = 20 
                    print("Height reset to default")
                break
            except ValueError:
                print("Please enter an integer")
                continue

    @staticmethod
    def change_color():
        color_prompt = input("Enter the color of your ASCII art:\n"
                             "1 - Red\n"
                             "2 - Green\n"
                             "3 - Yellow\n"
                             "4 - Blue\n"
                             "5 - Magenta\n"
                             "6 - Cyan\n"
                             "7 - Light gray\n"
                             "0 - Default\n"
                             "Your choice: ")
        match color_prompt:
            case "1":
                Global.color = "\033[31m"
            case "2":
                Global.color = "\033[32m"
            case "3":
                Global.color = "\033[33m"
            case "4":
                Global.color = "\033[34m"
            case "5":
                Global.color = "\033[35m"
            case "6":
                Global.color = "\033[36m"
            case "7":
                Global.color = "\033[37m"
            case "0":
                Global.color = "\033[39m"
            case _:
                print("Invalid color choice, please try again.")
                return
        print("Color changed successfully.")
