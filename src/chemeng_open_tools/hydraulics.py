"""Pipe-flow and pump calculations using SI units."""

from dataclasses import dataclass
import math


def _positive_finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be a finite number greater than zero")
    return value


def _nonnegative_finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return value


def reynolds_number(density_kg_m3: float, velocity_m_s: float, diameter_m: float,
                    dynamic_viscosity_pa_s: float) -> float:
    """Return Re = rho * |v| * D / mu (dimensionless)."""
    rho = _positive_finite("density_kg_m3", density_kg_m3)
    velocity = _nonnegative_finite("velocity_m_s", abs(float(velocity_m_s)))
    diameter = _positive_finite("diameter_m", diameter_m)
    viscosity = _positive_finite("dynamic_viscosity_pa_s", dynamic_viscosity_pa_s)
    return rho * velocity * diameter / viscosity


def darcy_friction_factor(reynolds: float, relative_roughness: float = 0.0,
                          method: str = "auto", tolerance: float = 1e-12,
                          max_iterations: int = 200) -> float:
    """Return Darcy friction factor; transitional flow is rejected in auto mode."""
    re = _positive_finite("reynolds", reynolds)
    rr = _nonnegative_finite("relative_roughness", relative_roughness)
    tol = _positive_finite("tolerance", tolerance)
    if not isinstance(max_iterations, int) or isinstance(max_iterations, bool) or max_iterations < 1:
        raise ValueError("max_iterations must be a positive integer")
    selected = method.strip().lower()
    if selected not in {"auto", "colebrook", "swamee-jain"}:
        raise ValueError("method must be 'auto', 'colebrook', or 'swamee-jain'")
    if selected == "auto":
        if re <= 2300.0:
            return 64.0 / re
        if re < 4000.0:
            raise ValueError("Transitional flow (2300 < Re < 4000): no correlation selected")
        selected = "colebrook"
    if re < 4000.0:
        raise ValueError("Colebrook and Swamee-Jain methods require Re >= 4000")
    if selected == "swamee-jain":
        term = rr / 3.7 + 5.74 / (re ** 0.9)
        return 0.25 / (math.log10(term) ** 2)

    def residual(factor: float) -> float:
        return 1.0 / math.sqrt(factor) + 2.0 * math.log10(
            rr / 3.7 + 2.51 / (re * math.sqrt(factor))
        )

    low, high = 0.005, 0.2
    f_low, f_high = residual(low), residual(high)
    if f_low * f_high > 0.0:
        raise ArithmeticError("Could not bracket the Colebrook-White solution")
    for _ in range(max_iterations):
        mid = 0.5 * (low + high)
        f_mid = residual(mid)
        if abs(f_mid) <= tol or (high - low) <= tol:
            return mid
        if f_low * f_mid > 0.0:
            low, f_low = mid, f_mid
        else:
            high, f_high = mid, f_mid
    raise ArithmeticError("Colebrook-White solver did not converge")


def darcy_weisbach_pressure_drop(friction_factor: float, length_m: float,
                                 diameter_m: float, density_kg_m3: float,
                                 velocity_m_s: float) -> float:
    """Return pressure loss in Pa using the Darcy-Weisbach equation."""
    f = _positive_finite("friction_factor", friction_factor)
    length = _positive_finite("length_m", length_m)
    diameter = _positive_finite("diameter_m", diameter_m)
    rho = _positive_finite("density_kg_m3", density_kg_m3)
    velocity = _nonnegative_finite("velocity_m_s", abs(float(velocity_m_s)))
    return f * (length / diameter) * (rho * velocity**2 / 2.0)


@dataclass(frozen=True)
class PumpPower:
    """Pump power results in watts."""
    hydraulic_power_w: float
    shaft_power_w: float


def pump_power(pressure_drop_pa: float, flow_rate_m3_s: float,
               efficiency: float) -> PumpPower:
    """Return hydraulic and shaft power for a supplied pump efficiency."""
    pressure = _nonnegative_finite("pressure_drop_pa", pressure_drop_pa)
    flow = _nonnegative_finite("flow_rate_m3_s", flow_rate_m3_s)
    eta = float(efficiency)
    if not math.isfinite(eta) or not 0.0 < eta <= 1.0:
        raise ValueError("efficiency must be greater than zero and at most one")
    hydraulic = pressure * flow
    return PumpPower(hydraulic_power_w=hydraulic, shaft_power_w=hydraulic / eta)