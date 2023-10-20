
from abc import ABC, abstractmethod

from battery.battery import Battery
from battery.nubbin_battery import NubinBattery
from battery.spindler_battery import SpindlerBattery
from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class Serviceable(ABC):
    @abstractmethod
    def needs_service() -> bool:
        raise NotImplementedError

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery)

    def create_palindrome(current_date, last_service_date, warning_light_on) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubinBattery(current_date, last_service_date)

        return Car(engine, battery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubinBattery(current_date, last_service_date)

        return Car(engine, battery)
