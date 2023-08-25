import sympy as sp

# Define symbols
I0, V0 = sp.symbols('I0 V0')

# Define equations
Pave_eq = (1/2) * I0 * V0
Irms_eq = I0 * sp.sqrt(2)
Vrms_eq = V0 * sp.sqrt(2)

# Substitute values and solve
Pave = Pave_eq.subs({I0: 2.5, V0: 120})
Irms = Irms_eq.subs({I0: 2.5})
Vrms = Vrms_eq.subs({V0: 120})

print("Average Power:", Pave)
print("RMS Current:", Irms)
print("RMS Voltage:", Vrms)


# Answer: Average Power: 150.000000000000
#         RMS Current: 2.5*sqrt(2)
#         RMS Voltage: 120*sqrt(2)
