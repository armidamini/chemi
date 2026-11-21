# Contributing

Contributions are welcome, especially improvements to calculation transparency, documentation, validation, and test coverage.

Before opening a pull request:

1. Explain the engineering equation or authoritative reference behind a change.
2. State the expected units for every input and output.
3. Add tests for normal, boundary, and invalid inputs.
4. Run the test suite with: python -m pip install -e ".[dev]" and pytest.
5. Update the README when public behavior changes.

Keep the project focused on small, auditable engineering calculations. Avoid opaque black-box calculations or claims of design-code compliance without a documented, tested basis.

When reporting an issue, include a minimal reproducible example, Python version, input values with units, observed result, and expected result. Do not include confidential plant or customer data.