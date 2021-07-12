import pandas as pd

PATH = '//172.16.137.133/naskbots/DGA-XXX - SisFies/Arquivos/DGA-355/backup/pesquisa-aditamentos.xls'

df = pd.read_excel(PATH, sheet_name=0, skiprows=12)
print(df)
