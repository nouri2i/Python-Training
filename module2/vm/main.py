import random

class City:
    def __init__(self,name,country):
        self.name=name
        self.country=country
    def __str__(self):
        return f"{self.name}, {self.country}"
    
class WeatherRecord:
    def __init__(self,temperature,condition,humidity):
        self.temperature=temperature
        self.condition=condition
        self.humidity=humidity
   
    def __str__(self):
        return f"{self.temperature} degrees, {self.condition}, {self.humidity}% humidity"

class WeatherTracker:
    def __init__(self):
        self.weather_records ={}
    def __len__(self):
        return len(self.weather_records)     
    
    def add_cities(self,*cities):
        for city in cities:
            self.update_weather(city)
    
    # fake data
    def update_weather(self,city):
        fake_conditions=["clear","Cloudy","Snow","Thunderstorm"]
        self.weather_records[city]=WeatherRecord(temperature=random.randint(-5,35)
                                           ,condition=random.choice(fake_conditions),
                                           humidity=random.randint(30,90))
    # print cities weather record

    def list_cities(self):
        for city, weather in self.weather_records.items():
            print(f"{city}==> {weather}\n")

if __name__ == "__main__":
    london= City("London","UK")
    new_york=City("New York","USA")
    tokyo = City("Tokyo","Japan")

    tracker=WeatherTracker()
    tracker.add_cities(london,new_york,tokyo)

    print(f"Total cities tracked: {len(tracker)}\n")
    tracker.list_cities()