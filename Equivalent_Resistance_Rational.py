import sympy as sp

R1 = sp.Rational(2750, 1000)  # 2.75 kΩ
R2 = 27.5  # 27.5 Ω

equivalent_resistance = sp.simplify(1 / (1/R1 + 1/R2))
print("Equivalent Resistance:", equivalent_resistance)

# Answer: Equivalent Resistance: 2.50000000000000
