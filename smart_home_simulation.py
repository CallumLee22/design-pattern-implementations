"""
This smart home simulation implementation uses the command pattern
"""

from abc import ABC, abstractmethod


class Light:
    """Light receiver class"""

    def turn_on(self):
        """Method to turn on the light"""
        print("Light turned on")

    def turn_off(self):
        """Method to turn off the light"""
        print("Light turned off")


class Thermostat:
    """Thermostat receiver class"""

    def turn_up(self):
        """Method to turn up the temperature on the thermostat"""
        print("Thermostat temperature increased by 1 degree")

    def turn_down(self):
        """Method to turn down the temperature on the thermostat"""
        print("Thermostat temperature decreased by 1 degree")


class Door:
    """Door receiver class"""

    def lock(self):
        """Method to lock a door"""
        print("Door is locked")

    def unlock(self):
        """Method to unlock a door"""
        print("Door unlocked")


class CommandInterface(ABC):
    """Interface for command classes to implement"""

    @abstractmethod
    def execute(self):
        """
        Abstract method for commands to implement that executes the desired command
        """


class SwitchOnLightCommand(CommandInterface):
    """Command to turn on a light"""

    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.turn_on()


class SwitchOffLightCommand(CommandInterface):
    """Command to turn off a light"""

    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.turn_off()


class TurnUpThermostatCommand(CommandInterface):
    """Command to turn up the thermostat"""

    def __init__(self, thermostat: Thermostat):
        self._thermostat = thermostat

    def execute(self):
        self._thermostat.turn_up()


class TurnDownThermostatCommand(CommandInterface):
    """Command to turn down the thermostat"""

    def __init__(self, thermostat: Thermostat):
        self._thermostat = thermostat

    def execute(self):
        self._thermostat.turn_down()


class LockDoorCommand(CommandInterface):
    """Command to lock a door"""

    def __init__(self, door: Door):
        self._door = door

    def execute(self):
        self._door.lock()


class UnlockDoorCommand(CommandInterface):
    """Command to unlock a door"""

    def __init__(self, door: Door):
        self._door = door

    def execute(self):
        self._door.unlock()


class RemoteControl:
    """Invoker class"""

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        """Register a new command"""
        self._commands[command_name] = command

    def execute(self, command_name):
        """Execute the command"""
        if command_name in self._commands:
            self._commands[command_name].execute()


# Client
if __name__ == "__main__":
    # Receivers
    light = Light()
    thermostat = Thermostat()
    door = Door()

    # Commands
    switch_on_light = SwitchOnLightCommand(light)
    switch_off_light = SwitchOffLightCommand(light)
    turn_up_thermostat = TurnUpThermostatCommand(thermostat)
    turn_down_thermostat = TurnDownThermostatCommand(thermostat)
    lock_door = LockDoorCommand(door)
    unlock_door = UnlockDoorCommand(door)

    # Invoker
    remote_control = RemoteControl()

    # Register the commands in the invoker
    remote_control.register("LIGHT_ON", switch_on_light)
    remote_control.register("LIGHT_OFF", switch_off_light)
    remote_control.register("THERMOSTAT_UP", turn_up_thermostat)
    remote_control.register("THERMOSTAT_DOWN", turn_down_thermostat)
    remote_control.register("LOCK_DOOR", lock_door)
    remote_control.register("UNLOCK_DOOR", unlock_door)

    # Execute commands
    remote_control.execute("LIGHT_ON")
    remote_control.execute("LIGHT_OFF")
    remote_control.execute("THERMOSTAT_UP")
    remote_control.execute("THERMOSTAT_DOWN")
    remote_control.execute("LOCK_DOOR")
    remote_control.execute("LOCK_DOOR")
