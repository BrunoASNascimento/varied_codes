import numpy as np

data_list = [
    {
        'value': 0.1,
        'error': 0.01,
        'square': 4
    },
    {
        'value': 0.01,
        'error': 0.002,
        'square': 2
    }
]

value_calc = 1
error_calc = 0

for data in data_list:
    # print(data) #! Print data to log
    value_calc *= data['value']**data['square']
    error_calc += (data['square']*(data['error']/data['value']))**2

error_calc = value_calc*np.sqrt(error_calc)


print(f'{value_calc} ± {error_calc}')
