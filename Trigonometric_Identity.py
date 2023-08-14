import sympy as sp

alpha, beta = sp.symbols('alpha beta')

# Trigonometric identity
left_side = sp.cos(alpha) + sp.cos(beta)
right_side = 2 * sp.cos(0.5 * (alpha + beta)) * sp.cos(0.5 * (alpha - beta))

simplified = sp.simplify(left_side - right_side)

if simplified == 0:
    print("The trigonometric identity is valid.")
else:
    print("The trigonometric identity is not valid.")


# Answer: The trigonometric identity is not valid.
