import sympy as sp

# Define symbols
alpha, beta = sp.symbols('alpha beta')

# Define the identity
lhs = sp.cos(alpha + beta)
rhs = sp.cos(alpha) * sp.cos(beta) - sp.sin(alpha) * sp.sin(beta)

# Check if the identity holds true
identity_holds = sp.simplify(lhs - rhs) == 0
print("Does the identity hold true?", identity_holds)


# Answer: Does the identity hold true? True
