"""
Smart home simulation using the Singleton pattern
"""


class SingletonMeta(type):
    """Metaclass that creates only one instance of the singleton"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Light:
    """Light receiver class"""

    def turn_on(self):
        """Turn light on"""
        print("Light turned on")

    def turn_off(self):
        """Turn light off"""
        print("Light turned off")


class Thermostat:
    """Thermostat receiver class."""

    def turn_up(self):
        """Turn up thermostat"""
        print("Thermostat temperature increased by 1 degree")

    def turn_down(self):
        """Turn down thermostat"""
        print("Thermostat temperature decreased by 1 degree")


class Door:
    """Door receiver class"""

    def lock(self):
        """Lock door"""
        print("Door is locked")

    def unlock(self):
        """Unlock door"""
        print("Door unlocked")


class SmartHomeController(metaclass=SingletonMeta):
    """Singleton controller for the smart home"""

    def __init__(self):
        self._light = Light()
        self._thermostat = Thermostat()
        self._door = Door()

    def switch_on_light(self):
        """Calls turn on method for light class"""
        self._light.turn_on()

    def switch_off_light(self):
        """Calls turn off method for light class"""

        self._light.turn_off()

    def turn_up_thermostat(self):
        """Calls turn up method for thermostat class"""

        self._thermostat.turn_up()

    def turn_down_thermostat(self):
        """Calls turn down method for thermostat class"""

        self._thermostat.turn_down()

    def lock_door(self):
        """Calls lock method for door class"""

        self._door.lock()

    def unlock_door(self):
        """Calls unlock method for door class"""

        self._door.unlock()


home_a = SmartHomeController()
home_b = SmartHomeController()

print("Using singleton SmartHomeController")
print(f"Same instance: {home_a is home_b}")

home_a.switch_on_light()
home_a.turn_up_thermostat()
home_a.lock_door()
home_b.switch_off_light()
home_b.turn_down_thermostat()
home_b.unlock_door()
