import math
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


def test_celsius_below_absolute_zero_is_rejected():
    with pytest.raises(ValueError, match="absolute zero"):
        celsius_to_kelvin(-273.16)


def test_absolute_zero_is_valid_in_both_temperature_scales():
    assert celsius_to_kelvin(-273.15) == pytest.approx(0.0)
    assert kelvin_to_celsius(0.0) == pytest.approx(-273.15)


@pytest.mark.parametrize("value", [math.inf, -math.inf, math.nan])
def test_temperature_conversions_reject_non_finite_values(value):
    with pytest.raises(ValueError, match="finite"):
        celsius_to_kelvin(value)
    with pytest.raises(ValueError, match="finite"):
        kelvin_to_celsius(value)
