import numpy as np

# Given data
resistance_per_insulator = 1.00e9  # Ohms
number_of_insulators = 100

# Total resistance in parallel is given by the reciprocal of the sum of reciprocals
total_resistance = 1 / np.sum(1 / resistance_per_insulator)

print("Total resistance to ground:", total_resistance, "Ohms")
