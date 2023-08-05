import numpy as np
import pandas as pd

# Function to generate truth table for n variables
def generate_truth_table(n):
    return np.array(np.meshgrid(*[[True, False]] * n)).T.reshape(-1, n)

# Function to evaluate a logical expression using the truth table
def evaluate_expression(expression, variables, truth_table):
    for i, var in enumerate(variables):
        expression = expression.replace(var, f'truth_table[:, {i}]')
    return eval(expression)

# Example 1: Show that p → q and its contrapositive ~q → ~p are logically equivalent.
p = 'p'
q = 'q'
implication_expression = '(p & ~q) | (~p & q)'

# Generate truth table for p and q
variables = ['p', 'q']
truth_table = generate_truth_table(2)

# Evaluate the expressions
p_implies_q = evaluate_expression(implication_expression, variables, truth_table)
contrapositive = evaluate_expression('(~q & p) | (q & ~p)', variables, truth_table)

# Create DataFrame for the truth table and results
df = pd.DataFrame(truth_table, columns=variables)
df['p → q'] = p_implies_q
df['~q → ~p'] = contrapositive

print(df)


# Answer:         p      q  p → q  ~q → ~p
#          0   True   True  False    False
#          1   True  False   True     True
#          2  False   True   True     True
#          3  False  False  False    False
