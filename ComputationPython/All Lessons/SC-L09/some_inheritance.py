# 4.
class Engine:
    def start(self):
        return

    def stop(self):
        pass


# Is-A Engine
class ElectricEngine(Engine):
    pass


# Is-A Engine
class V8Engine(Engine):
    pass


class Headlights:
    def lights_on(self):
        print('Lights are on')

    def lights_off(self):
        print('Lights are off')


class Car:
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls()  # Has-A Engine
        self.headlights = Headlights()  # Has-A Headlights

    def start(self):
        print(
            'Starting engine {0} for car {1}... Wroom, wroom!'
            .format(self.engine.__class__.__name__, self.__class__.__name__)
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def turn_on_lights(self):
        self.headlights.lights_on()

    def turn_off_lights(self):
        self.headlights.lights_off()


# Is-A Car
class RaceCar(Car):
    engine_cls = V8Engine


class CityCar(Car):
    engine_cls = ElectricEngine


class F1Car(RaceCar):
    pass  # engine_cls same as parent


car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()
    car.turn_on_lights()
    car.turn_off_lights()
