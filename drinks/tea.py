from dataclasses import dataclass

from .hot_beverage import HotBeverage


@dataclass
class Tea(HotBeverage):
    """Prepare and serve Tea

    See Also
    ----------
    HotBeverage
    """

    def brew(self):
        r"""Steeps the tea at `temperature`"""
        print("Steeping the tea with water at", f"{self.temperature}°C")

    def add_extras(self):
        """Add lemon to tea"""
        print("Adding lemon")
