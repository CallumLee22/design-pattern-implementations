"""
This smart home simulation implementation uses the proxy pattern.
"""

from abc import ABC, abstractmethod


class Switchable(ABC):
    """Interface for devices that can be switched on or off"""

    @abstractmethod
    def turn_on(self):
        """Turn on device"""

    @abstractmethod
    def turn_off(self):
        """Turn off device"""


class Adjustable(ABC):
    """Interface for devices that can adjust settings"""

    @abstractmethod
    def turn_up(self):
        """Turn up device"""

    @abstractmethod
    def turn_down(self):
        """Turn down device"""


class Lockable(ABC):
    """Interface for devices that can be locked or unlocked"""

    @abstractmethod
    def lock(self):
        """Lock device"""

    @abstractmethod
    def unlock(self):
        """Unlock device"""


class Light(Switchable):
    """Light receiver class."""

    def turn_on(self):
        print("Light turned on")

    def turn_off(self):
        print("Light turned off")


class Thermostat(Adjustable):
    """Thermostat receiver class."""

    def turn_up(self):
        print("Thermostat temperature increased by 1 degree")

    def turn_down(self):
        print("Thermostat temperature decreased by 1 degree")


class Door(Lockable):
    """Door receiver class"""

    def lock(self):
        print("Door is locked")

    def unlock(self):
        print("Door unlocked")


class ProxyBase:
    """Shared proxy behavior for access checking and logging"""

    def __init__(self, device, user_role="guest"):
        self._device = device
        self._user_role = user_role

    def _log_action(self, action_name: str):
        print(f"Proxy: {self._user_role} requested '{action_name}'")

    def _check_access(self, action_name: str, allowed_actions: set):
        self._log_action(action_name)
        if self._user_role == "admin":
            return True
        if action_name not in allowed_actions:
            raise PermissionError(
                f"Role '{self._user_role}' is not allowed to perform '{action_name}'"
            )
        return True


class LightProxy(ProxyBase, Switchable):
    """Proxy for Light object"""

    _allowed_actions = {"turn_on", "turn_off"}

    def turn_on(self):
        if self._check_access("turn_on", self._allowed_actions):
            self._device.turn_on()

    def turn_off(self):
        if self._check_access("turn_off", self._allowed_actions):
            self._device.turn_off()


class ThermostatProxy(ProxyBase, Adjustable):
    """Proxy for Thermostat object."""

    _allowed_actions = {"turn_up", "turn_down"}

    def turn_up(self):
        if self._check_access("turn_up", self._allowed_actions):
            self._device.turn_up()

    def turn_down(self):
        if self._check_access("turn_down", self._allowed_actions):
            self._device.turn_down()


class DoorProxy(ProxyBase, Lockable):
    """Proxy for Door object."""

    _allowed_actions = {"lock"}

    def lock(self):
        if self._check_access("lock", self._allowed_actions):
            self._device.lock()

    def unlock(self):
        if self._check_access("unlock", self._allowed_actions):
            self._device.unlock()


if __name__ == "__main__":
    light = Light()
    thermostat = Thermostat()
    door = Door()

    # Create proxies for different user roles
    light_proxy = LightProxy(light, user_role="user")
    thermostat_proxy = ThermostatProxy(thermostat, user_role="user")
    door_proxy = DoorProxy(door, user_role="guest")

    light_proxy.turn_on()
    light_proxy.turn_off()

    thermostat_proxy.turn_up()
    thermostat_proxy.turn_down()

    try:
        door_proxy.unlock()
    except PermissionError as exc:
        print(exc)

    # Admin can perform all actions
    admin_door_proxy = DoorProxy(door, user_role="admin")
    admin_door_proxy.unlock()
