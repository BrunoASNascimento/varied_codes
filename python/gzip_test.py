import gzip
import shutil
import os

path_input = 'D:/developer/bitbucket/sulamerica/sas-governanca-analysis-datastream/cloud-function/test_datastream_to_bq/data/json'
path_output = 'D:/developer/bitbucket/sulamerica/sas-governanca-analysis-datastream/cloud-function/test_datastream_to_bq/data/gzip'
files = os.listdir(path_input)
for file in files:
    print(file)
    name_input = f'{path_input}/{file}'
    name_output = f'{path_output}/{file}.gz'
    with open(name_input, 'rb') as f_in:
        with gzip.open(name_output, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
