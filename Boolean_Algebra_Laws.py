from sympy import symbols, Not, Or, And, simplify_logic

# Boolean Algebra Laws
def prove_boolean_algebra_laws():
    A, B = symbols('A B')

    commutative_law = And(A, B).equals(And(B, A))
    associative_law = And(And(A, B), B).equals(And(A, And(B, B)))
    distributive_law = And(A, Or(B, B)).equals(Or(And(A, B), And(A, B)))
    demorgans_law_1 = Not(And(A, B)).equals(Or(Not(A), Not(B)))
    demorgans_law_2 = Not(Or(A, B)).equals(And(Not(A), Not(B)))

    laws = [commutative_law, associative_law, distributive_law, demorgans_law_1, demorgans_law_2]

    for law in laws:
        print(f"Proving: {law}")
        proof = simplify_logic(law)
        print("Proof:", proof)
        print("\n")

# Run examples
prove_boolean_algebra_laws()
