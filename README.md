# ChemEng Open Tools

A small open-source Python toolkit for transparent introductory chemical-engineering calculations. The package emphasizes explicit SI units, documented equations, input validation, and reproducible tests.

## Current capabilities

### Fluid mechanics and hydraulics
- Reynolds number for circular-pipe flow
- Darcy friction factor: laminar, Colebrook–White, and Swamee–Jain
- Darcy–Weisbach pressure drop
- Hydraulic and pump shaft power

### Heat transfer
- Sensible heat duty for a stream with constant specific heat capacity
- Log-mean temperature difference (LMTD)
- Idealized heat-exchanger area from the LMTD method

### Unit conversions
- Celsius and kelvin
- Bar and pascal

## Installation

Requires Python 3.10 or newer. Clone the repository, enter its directory, and install from source:

    git clone https://github.com/armidamini/chemi.git
    cd chemi
    python -m pip install .

For development and tests:

    python -m pip install -e ".[dev]"
    pytest

The project is currently distributed as source on GitHub; a PyPI package release has not been published.

## Quick example

After installing the package from a local checkout, the following calculates Reynolds number:

    from chemeng_open_tools import reynolds_number
    re = reynolds_number(
        density_kg_m3=998.2,
        velocity_m_s=1.5,
        diameter_m=0.05,
        dynamic_viscosity_pa_s=0.001,
    )
    print(re)

A complete heat-exchanger example is available in [examples/heat_exchanger_example.py](examples/heat_exchanger_example.py).

## Engineering assumptions and limitations

All calculation inputs and outputs use SI units. Friction factors are Darcy factors, not Fanning factors. Pipe correlations assume steady, fully developed, single-phase flow in a circular conduit. The automatic friction-factor method uses 64/Re for Re <= 2300, rejects the transitional range 2300 < Re < 4000, and uses Colebrook–White for Re >= 4000. Relative roughness is absolute roughness divided by internal diameter.

Pump calculations use the efficiency supplied by the caller and do not model motor or drive losses. Sensible-heat calculations assume constant heat capacity and no phase change. The LMTD and area functions are idealized: the LMTD method is intended for parallel- or counterflow arrangements with appropriate positive terminal temperature differences; multipass and other configurations may require a correction factor. Fouling, heat loss, mechanical constraints, and design margins are not included.

This educational software is not a substitute for engineering review, validated process data, applicable design codes, or a detailed equipment rating.

## Documentation and contribution

- [Equations, methods, references, and limitations](docs/equations-and-methods.md)
- [Testing and validation approach](docs/validation-and-quality.md)
- [Reproducible pipe-flow example](examples/pipe_flow_example.py)
- [Worked heat-exchanger example](examples/heat_exchanger_example.py)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Support and reporting](SUPPORT.md)
- [Pull request checklist](.github/pull_request_template.md)
- [Changelog](CHANGELOG.md)
- [Contribution guidelines](CONTRIBUTING.md)
- [Issue templates](https://github.com/armidamini/chemi/issues/new/choose)

Please report reproducible issues with units and non-confidential example data. All engineering calculations should be independently reviewed before practical use.

## License and citation

Released under the MIT License; see [LICENSE](LICENSE). Citation metadata is provided in [CITATION.cff](CITATION.cff).
