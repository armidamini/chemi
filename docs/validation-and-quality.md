# Validation and software quality

## Automated tests

The project uses pytest and GitHub Actions. The workflow tests Python 3.10, 3.11, 3.12, and 3.13 on pushes and pull requests, and builds both a source distribution and a wheel.

Run locally:

    python -m pip install -e ".[dev]"
    pytest

## What the current tests cover

- Reynolds-number calculation, zero velocity, and invalid physical inputs.
- Laminar friction factor and the explicitly rejected transitional range.
- Colebrook–White and Swamee–Jain turbulent friction-factor calculations.
- Darcy–Weisbach pressure loss.
- Hydraulic and shaft pump power, including zero flow and invalid efficiency.
- Celsius/kelvin and bar/pascal conversion behavior.
- Sensible heat duty for heating and cooling, and rejection of negative mass flow.
- LMTD for equal and unequal terminal temperature differences, including invalid terminal differences.
- Idealized heat-exchanger area and invalid heat-transfer coefficient.

## Validation philosophy

A passing software test establishes that the implementation behaves as asserted for the tested cases. It does not prove that the equations apply to every physical system or that the software is suitable for a particular plant or design.

The test suite checks mathematical behavior, selected reference cases, boundary behavior, and input validation. Engineering applicability still depends on the assumptions documented in [equations-and-methods.md](equations-and-methods.md). Results should be independently checked against a recognized engineering reference and the relevant design standard before practical use.

## Reproducible build

The GitHub Actions workflow builds a source distribution and a wheel before running the test suite. This checks that the package can be built in CI; it does not by itself constitute a published or independently certified release.

## Reporting a problem

Use the repository's [bug report form](https://github.com/armidamini/chemi/issues/new?template=bug_report.yml). Include units, a minimal reproducible example, and the Python version. Never submit confidential process or customer information.
