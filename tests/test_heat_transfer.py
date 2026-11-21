import math
import pytest

from chemeng_open_tools import (
    heat_exchanger_area,
    log_mean_temperature_difference,
    sensible_heat_duty,
)


def test_sensible_heat_duty_heating():
    assert sensible_heat_duty(2.0, 4180.0, 300.0, 350.0) == pytest.approx(418000.0)


def test_sensible_heat_duty_cooling_is_negative():
    assert sensible_heat_duty(1.0, 2000.0, 350.0, 300.0) == pytest.approx(-100000.0)


def test_sensible_heat_duty_rejects_negative_mass_flow():
    with pytest.raises(ValueError, match="nonnegative"):
        sensible_heat_duty(-1.0, 2000.0, 300.0, 350.0)


def test_lmtd_equal_terminal_differences():
    assert log_mean_temperature_difference(20.0, 20.0) == pytest.approx(20.0)


def test_lmtd_known_case():
    result = log_mean_temperature_difference(40.0, 20.0)
    assert result == pytest.approx(28.8539008178)


def test_lmtd_rejects_nonpositive_terminal_difference():
    with pytest.raises(ValueError):
        log_mean_temperature_difference(20.0, 0.0)


def test_heat_exchanger_area():
    assert heat_exchanger_area(100000.0, 500.0, 20.0) == pytest.approx(10.0)


def test_heat_exchanger_area_rejects_nonpositive_u():
    with pytest.raises(ValueError):
        heat_exchanger_area(100000.0, 0.0, 20.0)
