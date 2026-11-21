"""Reproducible introductory pipe-flow example.

Run from the repository root with:
    python examples/pipe_flow_example.py
"""

import math

from chemeng_open_tools import (
    darcy_friction_factor,
    darcy_weisbach_pressure_drop,
    pump_power,
    reynolds_number,
)

# Illustrative water-like fluid and a straight circular pipe.
density = 998.2                 # kg/m^3
dynamic_viscosity = 1.002e-3    # Pa.s
velocity = 1.5                  # m/s
diameter = 0.05                 # m
length = 100.0                  # m
absolute_roughness = 1.0e-5     # m
flow_rate = math.pi * diameter**2 / 4.0 * velocity  # m^3/s

re = reynolds_number(density, velocity, diameter, dynamic_viscosity)
relative_roughness = absolute_roughness / diameter
friction_factor = darcy_friction_factor(re, relative_roughness)
pressure_loss = darcy_weisbach_pressure_drop(
    friction_factor, length, diameter, density, velocity
)
power = pump_power(pressure_loss, flow_rate, efficiency=0.75)

print(f"Reynolds number: {re:.1f}")
print(f"Darcy friction factor: {friction_factor:.5f}")
print(f"Straight-pipe pressure loss: {pressure_loss:.1f} Pa")
print(f"Hydraulic power: {power.hydraulic_power_w:.2f} W")
print(f"Pump shaft power: {power.shaft_power_w:.2f} W")
