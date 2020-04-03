%matplotlib inline
import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")
df.head()
previous_employers_hired = df[['Previous employers', 'Hired']][5:11]
previous_employers_hired
previous_employers_hired.plot(kind='bar')