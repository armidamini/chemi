"""Worked idealized heat-exchanger calculation.

Run from the repository root with:
    python examples/heat_exchanger_example.py
"""

from chemeng_open_tools import (
    heat_exchanger_area,
    log_mean_temperature_difference,
    sensible_heat_duty,
)

mass_flow_kg_s = 2.0
heat_capacity_j_kg_k = 4180.0
inlet_temperature_k = 300.0
outlet_temperature_k = 350.0
overall_u_w_m2_k = 500.0

duty_w = sensible_heat_duty(
    mass_flow_kg_s,
    heat_capacity_j_kg_k,
    inlet_temperature_k,
    outlet_temperature_k,
)

# These are assumed terminal temperature differences for an
# idealized counterflow/parallel-flow LMTD calculation.
delta_t1_k = 40.0
delta_t2_k = 20.0
lmtd_k = log_mean_temperature_difference(delta_t1_k, delta_t2_k)

area_m2 = heat_exchanger_area(duty_w, overall_u_w_m2_k, lmtd_k)

print(f"Heat duty: {duty_w / 1000:.2f} kW")
print(f"LMTD: {lmtd_k:.2f} K")
print(f"Idealized heat-transfer area: {area_m2:.2f} m^2")
