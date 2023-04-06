import numpy as np
import pandas as pd

lst = ['Java', 'Python', 'C', 'C++',
       'JavaScript', 'Swift', 'Go']

dframe = pd.DataFrame(lst)

print(dframe.head(5))

print(np.eye(3))