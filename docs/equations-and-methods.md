# Equations, methods, and references

This document records the equations implemented by ChemEng Open Tools and the assumptions that limit their use. All quantities are expressed in SI units unless explicitly stated otherwise.

## Reynolds number

For a Newtonian fluid in a circular pipe:

\[
\mathrm{Re}=\frac{\rho |v|D}{\mu}
\]

where \(\rho\) is density (kg/m³), \(v\) is average velocity (m/s), \(D\) is internal diameter (m), and \(\mu\) is dynamic viscosity (Pa·s). Reynolds number is dimensionless.

## Darcy friction factor

The package returns the Darcy friction factor. It is four times the Fanning friction factor; the two conventions must not be interchanged.

### Laminar regime

For fully developed laminar flow in a circular pipe:

\[
f_D=\frac{64}{\mathrm{Re}}
\]

### Turbulent regime: Colebrook–White

For turbulent flow, the implicit Colebrook–White relation is solved numerically:

\[
\frac{1}{\sqrt{f_D}}=-2\log_{10}\left(\frac{\varepsilon/D}{3.7}+\frac{2.51}{\mathrm{Re}\sqrt{f_D}}\right)
\]

where \(\varepsilon/D\) is relative roughness. The implementation uses a bracketed bisection solver and raises an error if it cannot establish a bracket or converge.

### Turbulent regime: Swamee–Jain

The explicit approximation implemented for comparison is:

\[
f_D=\frac{0.25}{\left[\log_{10}\left(\frac{\varepsilon/D}{3.7}+\frac{5.74}{\mathrm{Re}^{0.9}}\right)\right]^2}
\]

### Regime handling

The automatic method uses the laminar expression for Re ≤ 2300, rejects 2300 < Re < 4000 rather than silently selecting a correlation in the transitional region, and uses Colebrook–White for Re ≥ 4000. Explicit turbulent methods also require Re ≥ 4000. These cutoffs are conservative software behavior, not a claim that the physical transition occurs at one universal Reynolds number.

## Darcy–Weisbach pressure loss

For a straight, constant-diameter pipe:

\[
\Delta P=f_D\frac{L}{D}\frac{\rho v^2}{2}
\]

The result is pressure loss in pascals. The current function does not add minor losses, static elevation changes, acceleration terms, or compressibility effects.

## Pump power

For a specified pressure rise/loss and volumetric flow:

\[
P_{hyd}=\Delta P\,Q,\qquad P_{shaft}=\frac{P_{hyd}}{\eta}
\]

where \(Q\) is volumetric flow (m³/s) and \(\eta\) is the supplied overall pump efficiency as a fraction between zero and one. Motor and drive efficiencies are not modeled separately.

## References

1. USDA Natural Resources Conservation Service, *National Engineering Handbook, Part 636, Chapter 4: Pipe Flow*. Includes Darcy–Weisbach and Swamee–Jain treatment: https://directives.nrcs.usda.gov/sites/default/files2/1720463089/Chapter%204%20-%20Pipe%20Flow.pdf
2. USDA Natural Resources Conservation Service, *Engineering Field Handbook, Part 650, Chapter 3: Hydraulics*. Presents laminar Darcy friction factor, Colebrook–White, Swamee–Jain, and pipe-flow equations: https://irrigationtoolbox.com/NEH/Part650EngineeringFieldHandbook/Part650Ch03-DRAFT.pdf
3. Colebrook, C. F. (1939), “Turbulent Flow in Pipes, with Particular Reference to the Transition Region Between the Smooth and Rough Pipe Laws,” *Journal of the Institution of Civil Engineers*.
4. Swamee, P. K. and Jain, A. K. (1976), “Explicit Equations for Pipe-Flow Problems,” *Journal of the Hydraulics Division, ASCE*, 102(5), 657–664.

## Scope and safety

These are introductory calculations for idealized pipe flow. Real systems may require property models, elevation and fitting losses, network interactions, transient analysis, multiphase or compressible-flow treatment, uncertainty analysis, and applicable engineering codes. Validate inputs and independently review any result before using it in design, operation, or safety-critical work.


## Sensible heat duty

For a stream with constant specific heat capacity over the temperature interval:

\\[
Q=\\dot m C_p(T_{out}-T_{in})
\\]

The function returns watts. Positive duty indicates heat added to the stream; negative duty indicates cooling. The model assumes constant heat capacity and does not account for phase change, reaction heat, or heat loss to the surroundings.

## Log-mean temperature difference

For two positive terminal temperature differences:

\\[
\\Delta T_{lm}=\\frac{\\Delta T_1-\\Delta T_2}{\\ln(\\Delta T_1/\\Delta T_2)}
\\]

When the two differences are equal, the limiting value is that common difference. The function rejects zero or negative terminal differences; it does not apply shell-and-tube correction factors.

## Idealized heat-exchanger area

For a specified duty, overall heat-transfer coefficient, and LMTD:

\\[
A=\\frac{|Q|}{U\\Delta T_{lm}}
\\]

The current area function accepts a nonnegative duty and returns square metres. It does not include fouling, correction factors, design margins, mechanical constraints, or detailed exchanger rating.
