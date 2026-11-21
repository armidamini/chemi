import math
import pytest
from chemeng_open_tools import (
    darcy_friction_factor, darcy_weisbach_pressure_drop, pump_power, reynolds_number,
)


def test_reynolds_number():
    assert reynolds_number(998.2, 1.5, 0.05, 0.001) == pytest.approx(74865.0)


def test_laminar_darcy_friction_factor():
    assert darcy_friction_factor(1000.0) == pytest.approx(0.064)


def test_auto_method_rejects_transition_range():
    with pytest.raises(ValueError, match="Transitional"):
        darcy_friction_factor(3000.0)


def test_colebrook_white_reference_case():
    assert darcy_friction_factor(100000.0, 0.0002, method="colebrook") == pytest.approx(0.0190, rel=0.005)


def test_swamee_jain_is_close_to_colebrook():
    f1 = darcy_friction_factor(100000.0, 0.0002, method="colebrook")
    f2 = darcy_friction_factor(100000.0, 0.0002, method="swamee-jain")
    assert f2 == pytest.approx(f1, rel=0.02)


def test_darcy_weisbach_pressure_drop():
    assert darcy_weisbach_pressure_drop(0.02, 10.0, 0.05, 1000.0, 2.0) == pytest.approx(8000.0)


def test_pump_power():
    result = pump_power(100000.0, 0.01, 0.8)
    assert result.hydraulic_power_w == pytest.approx(1000.0)
    assert result.shaft_power_w == pytest.approx(1250.0)


@pytest.mark.parametrize("args", [
    (0.0, 1.0, 0.1, 0.001),
    (1000.0, 1.0, 0.0, 0.001),
    (1000.0, 1.0, 0.1, 0.0),
    (math.inf, 1.0, 0.1, 0.001),
])
def test_reynolds_rejects_invalid_inputs(args):
    with pytest.raises(ValueError):
        reynolds_number(*args)


def test_friction_factor_rejects_invalid_method():
    with pytest.raises(ValueError, match="method"):
        darcy_friction_factor(10000.0, method="unknown")


def test_pump_efficiency_must_be_between_zero_and_one():
    with pytest.raises(ValueError, match="efficiency"):
        pump_power(1000.0, 0.1, 1.2)
