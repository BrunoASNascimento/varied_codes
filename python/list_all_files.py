import os
path = "//172.16.137.133/naskbots/API_OCR_TESTE/nas2/"

for root, d_names, f_names in os.walk(path):
    print(root, d_names, f_names)
