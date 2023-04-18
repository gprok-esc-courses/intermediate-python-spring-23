from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def get_route(self):
        pass


class ByCar(RouteStrategy):
    def get_route(self):
        return "Route by car ..."


class ByBus(RouteStrategy):
    def get_route(self):
        return "Route by bus ..."


class Walking(RouteStrategy):
    def get_route(self):
        return "Walking route"


class ByDrone(RouteStrategy):
    def get_route(self):
        return "Route by drone ..."


class Hyperloop(RouteStrategy):
    def get_route(self):
        return "Route by hyperloop ..."


class RouteFactory:
    options = {
        1: "By Car",
        2: "By Bus",
        3: "Walking",
        4: "By Drone",
        5: "Hyperloop"
    }
    @staticmethod
    def get_route_object(code):
        if code == 1:
            return ByCar()
        elif code == 2:
            return ByBus()
        elif code == 3:
            return Walking()
        elif code == 4:
            return ByDrone()
        elif code == 5:
            return Hyperloop()


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
        for index in RouteFactory.options:
            print(str(index) + ". " + RouteFactory.options[index])
        print("0. EXIT")

        selection = int(input("Select: "))

        if selection == 0:
            break
        else:
            map.set_route_strategy(RouteFactory.get_route_object(selection))

        map.print_route()
