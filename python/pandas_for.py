import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randint(0, 100, size=(100, 4)),
    columns=list('ABCD')
)

for row in df.itertuples(index=False):
    print(row)
