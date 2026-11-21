"""Small, explicit unit conversions."""

import math


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def celsius_to_kelvin(celsius: float) -> float:
    """Convert degrees Celsius to kelvin."""
    return _finite("celsius", celsius) + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert kelvin to degrees Celsius; values below 0 K are invalid."""
    value = _finite("kelvin", kelvin)
    if value < 0.0:
        raise ValueError("kelvin cannot be below absolute zero")
    return value - 273.15


def bar_to_pascal(bar: float) -> float:
    """Convert bar to pascal."""
    return _finite("bar", bar) * 100_000.0


def pascal_to_bar(pascal: float) -> float:
    """Convert pascal to bar."""
    return _finite("pascal", pascal) / 100_000.0