import pandas as pd
import random

size_data = 10

data = {
    'A': [i for i in range(size_data)],
    'B': [random.randint(1, 20) for _ in range(size_data)],
    'C': [random.randint(1, 20) for _ in range(size_data)]
}
print(data)

df = pd.DataFrame(data)


def check_number(a, b, c):
    test = f'{a}*{b}*{c} = {a * b * c}'
    return test


df['TEST_VALUE'] = df.apply(
    lambda x: check_number(x['A'], x['B'], x['C']),
    axis=1
)

print(df)
