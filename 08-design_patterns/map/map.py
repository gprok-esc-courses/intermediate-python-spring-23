from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def get_route(self):
        pass


class ByCar(RouteStrategy):
    def get_route(self):
        return "Path by car"


class ByBus(RouteStrategy):
    def get_route(self):
        return "Path by bus"


class Walking(RouteStrategy):
    def get_route(self):
        return "Path walking"


class Map:
    def __init__(self):
        self.route_strategy = None

    def set_route_strategy(self, route_strategy):
        self.route_strategy = route_strategy

    def print_route(self):
        if self.route_strategy is not None:
            print(self.route_strategy.get_route())


if __name__ == '__main__':
    map = Map()
    while True:
        print("1. By Car")
        print("2. By Bus")
        print("3. Walking")
        print("0. EXIT")
        selection = int(input("Select: "))
        if selection == 1:
            map.set_route_strategy(ByCar())
        elif selection == 2:
            map.set_route_strategy(ByBus())
        elif selection == 3:
            map.set_route_strategy(Walking())
        elif selection == 0:
            break
        map.print_route()





