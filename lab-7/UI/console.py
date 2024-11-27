from BLL.DataService import DataService

class ConsoleUI:
    def __init__(self):
        self.bll = DataService()
    
    def prompt(self):
        while True:
            user_input = input("Choose an option: \n1. Get posts\n2. Get users\n3. Save data\n4. Exit\n")
            if user_input == "1":
                posts = self.bll.get_posts()
                self.display_data(posts)
            elif user_input == "2":
                users = self.bll.get_users()
                self.display_data(users)
            elif user_input == "3":
                file_format = input("Enter file format (json/csv/txt): ")
                self.bll.save_data(posts, file_format)
            elif user_input == "4":
                break
            else:
                print("Invalid option")
    
    def display_data(self, data):
        print("ID | Title/Name")
        print("-" * 50)
        for item in data:
            print(f"{item['id']} | {item.get('title', item.get('name'))}")
