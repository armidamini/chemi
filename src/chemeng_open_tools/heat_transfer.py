"""Introductory thermal calculations using SI units."""

import math


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def _positive(name: str, value: float) -> float:
    value = _finite(name, value)
    if value <= 0.0:
        raise ValueError(f"{name} must be greater than zero")
    return value


def sensible_heat_duty(
    mass_flow_kg_s: float,
    heat_capacity_j_kg_k: float,
    inlet_temperature_k: float,
    outlet_temperature_k: float,
) -> float:
    """Return signed sensible heat duty in watts: m_dot * Cp * (Tout - Tin).

    Positive values represent heat added to the stream; negative values
    represent cooling. Constant heat capacity is assumed over the interval.
    """
    flow = _finite("mass_flow_kg_s", mass_flow_kg_s)
    cp = _positive("heat_capacity_j_kg_k", heat_capacity_j_kg_k)
    tin = _positive("inlet_temperature_k", inlet_temperature_k)
    tout = _positive("outlet_temperature_k", outlet_temperature_k)
    if flow < 0.0:
        raise ValueError("mass_flow_kg_s must be nonnegative")
    return flow * cp * (tout - tin)


def log_mean_temperature_difference(delta_t1_k: float, delta_t2_k: float) -> float:
    """Return LMTD for two positive terminal temperature differences in K."""
    dt1 = _positive("delta_t1_k", delta_t1_k)
    dt2 = _positive("delta_t2_k", delta_t2_k)
    if math.isclose(dt1, dt2, rel_tol=1e-12, abs_tol=0.0):
        return 0.5 * (dt1 + dt2)
    return (dt1 - dt2) / math.log(dt1 / dt2)


def heat_exchanger_area(
    heat_duty_w: float,
    overall_heat_transfer_coefficient_w_m2_k: float,
    lmtd_k: float,
) -> float:
    """Return required idealized area in m² from Q = U * A * LMTD.

    Heat duty must be nonnegative. Fouling, correction factors, and
    mechanical/design margins are not included.
    """
    duty = _finite("heat_duty_w", heat_duty_w)
    if duty < 0.0:
        raise ValueError("heat_duty_w must be nonnegative")
    coefficient = _positive(
        "overall_heat_transfer_coefficient_w_m2_k",
        overall_heat_transfer_coefficient_w_m2_k,
    )
    lmtd = _positive("lmtd_k", lmtd_k)
    return duty / (coefficient * lmtd)
