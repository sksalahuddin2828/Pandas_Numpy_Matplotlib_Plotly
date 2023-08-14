

import numpy as np
import pandas as pd

theta_vals = np.linspace(0, 2 * np.pi, 100)
cos_squared_vals = np.cos(theta_vals)**2
sin_squared_vals = np.sin(theta_vals)**2
two_cos_squared_minus_one_vals = 2 * cos_squared_vals - 1

data = {'Theta': theta_vals,
        'cos^2(θ)': cos_squared_vals,
        'sin^2(θ)': sin_squared_vals,
        '2cos^2(θ) - 1': two_cos_squared_minus_one_vals}

df = pd.DataFrame(data)
print(df.head())


# Answer:       Theta  cos^2(θ)  sin^2(θ)  2cos^2(θ) - 1
#         0  0.000000  1.000000  0.000000       1.000000
#         1  0.063467  0.995977  0.004023       0.991955
#         2  0.126933  0.983974  0.016026       0.967949
#         3  0.190400  0.964184  0.035816       0.928368
#         4  0.253866  0.936925  0.063075       0.873849
