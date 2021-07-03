import pandas as pd
import tabula

PATH = 'data/ufabc_ajuste_2021.2_turmas_ofertadas.pdf'

df = tabula.read_pdf(PATH, pages='all')

df = df.loc[df['CURSO'] != 'CURSO']
df.columns = [column_name.replace('\r', ' ') for column_name in df.columns]
df = df.replace(
    to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"],
    value=[" ", " "],
    regex=True
)
df.loc[df['SALDO DE VAGAS PARA O AJUSTE'] ==
       '#N/D', 'SALDO DE VAGAS PARA O AJUSTE'] = 0
df['SALDO DE VAGAS PARA O AJUSTE'] = df['SALDO DE VAGAS PARA O AJUSTE'].astype(
    int)

df['DOCENTE TEORIA'] = df['DOCENTE TEORIA'].str.title()
df['DOCENTE PRÁTICA'] = df['DOCENTE PRÁTICA'].str.title()

df.sort_values(by=['CURSO', 'TURMA'], inplace=True)
df = (df.loc[df['SALDO DE VAGAS PARA O AJUSTE'] > 0])

print(df)

df.to_csv(f'{PATH}.csv', index=False, sep=';', encoding='utf-8-sig')
