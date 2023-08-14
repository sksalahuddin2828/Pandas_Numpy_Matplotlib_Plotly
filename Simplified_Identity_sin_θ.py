import sympy as sp

theta = sp.symbols('theta')
identity = sp.cos(theta)**2 - sp.cos(theta)**2 + sp.sin(theta)**2
simplified_identity = sp.simplify(identity)
print("Simplified Identity:", simplified_identity)

# Answer: Simplified Identity: sin(theta)**2
