# Subject (Observable)
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

# Observer (Subscriber)
class Observer:
    def update(self, message):
        pass

# Concrete Subject
class WeatherStation(Subject):
    def set_weather(self, weather):
        self.notify_observers(f"Weather is now {weather}")

# Concrete Observer
class WeatherObserver(Observer):
    def update(self, message):
        print(f"WeatherObserver received message: {message}")

# Another Concrete Observer
class TrafficObserver(Observer):
    def update(self, message):
        print(f"TrafficObserver received message: {message}")

# Usage
weather_station = WeatherStation()
weather_observer = WeatherObserver()
traffic_observer = TrafficObserver()

weather_station.add_observer(weather_observer)
weather_station.add_observer(traffic_observer)

weather_station.set_weather("Sunny")