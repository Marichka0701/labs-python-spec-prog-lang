from DAL.api_client import ApiClient

class DataService:
    def __init__(self):
        self.api_client = ApiClient()
    
    def get_posts(self):
        return self.api_client.get_posts()
    
    def get_users(self):
        return self.api_client.get_users()
    
    def save_data(self, data, file_format='json'):
        if file_format == 'json':
            self.save_json(data)
        elif file_format == 'csv':
            self.save_csv(data)
        elif file_format == 'txt':
            self.save_txt(data)
        else:
            print("Unsupported format")

    def save_json(self, data):
        import json
        with open("data.json", 'w') as f:
            json.dump(data, f)
    
    def save_csv(self, data):
        import csv
        with open("data.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            
    def save_txt(self, data):
        with open("data.txt", 'w') as f:
            if isinstance(data, list):
                for item in data:
                    f.write(str(item) + "\n")
            else:
                f.write(str(data))
