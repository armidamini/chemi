import pytest
from chemeng_open_tools import (
    bar_to_pascal, celsius_to_kelvin, kelvin_to_celsius, pascal_to_bar,
)


def test_temperature_conversions():
    assert celsius_to_kelvin(0.0) == pytest.approx(273.15)
    assert kelvin_to_celsius(273.15) == pytest.approx(0.0)


def test_pressure_conversions():
    assert bar_to_pascal(1.0) == pytest.approx(100000.0)
    assert pascal_to_bar(250000.0) == pytest.approx(2.5)


def test_kelvin_below_absolute_zero_is_rejected():
    with pytest.raises(ValueError, match="absolute zero"):
        kelvin_to_celsius(-0.1)