# ChemEng Open Tools

A small open-source Python toolkit for transparent introductory chemical-engineering calculations.

## Initial scope

- Reynolds number for circular-pipe flow
- Darcy friction factor: laminar, Colebrook-White, and Swamee-Jain
- Darcy-Weisbach pressure drop
- Hydraulic and pump shaft power
- Celsius/Kelvin and bar/pascal conversions

## Installation

Requires Python 3.10 or newer.

    python -m pip install .

For development and tests:

    python -m pip install -e ".[dev]"
    pytest

## Engineering assumptions and limitations

All calculation inputs and outputs use SI units. Friction factors are Darcy factors, not Fanning factors. Pipe correlations assume steady, fully developed, single-phase flow in a circular conduit. The automatic friction-factor method uses 64/Re for Re <= 2300, rejects the transitional range 2300 < Re < 4000, and uses Colebrook-White for Re >= 4000. Relative roughness is absolute roughness divided by internal diameter.

Pump calculations use the efficiency supplied by the caller and do not model motor or drive losses. This educational software is not a substitute for engineering review, validated process data, or applicable design-code checks.

## License

MIT. See LICENSE.

## Documentation and contribution

- [Equations, methods, references, and limitations](docs/equations-and-methods.md)
- [Changelog](CHANGELOG.md)
- [Contribution guidelines](CONTRIBUTING.md)
- [Issue templates](https://github.com/armidamini/chemi/issues/new/choose)

Please report reproducible issues with units and non-confidential example data. All engineering calculations should be independently reviewed before practical use.

- [Reproducible pipe-flow example](examples/pipe_flow_example.py)
- [Testing and validation approach](docs/validation-and-quality.md)
