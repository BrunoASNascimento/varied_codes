# import cx_Oracle

# # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
# dsn_tns = cx_Oracle.makedsn(
#     'BASN-NITRO5',
#     '1521',
#     service_name='XE')
# # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
# conn = cx_Oracle.connect(
#     user=r'system',
#     password='Basn51828896',
#     dsn=dsn_tns
# )

# c = conn.cursor()
# # use triple quotes if you want to spread your query across multiple lines
# c.execute('select * from TB_CLIENTES3')
# print(c)
# # for row in c:
# # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
# # print(row[0], '-', row[1])
# conn.close()

import cx_Oracle
import os
import platform

# LOCATION = r"C:\Users\bruno\Downloads\instantclient-basic-windows.x64-19.8.0.0.0dbru\instantclient_19_8"
# print("ARCH:", platform.architecture())
# print("FILES AT LOCATION:")
# os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

# if needed, place an 'r' before any parameter in order to address special characters such as '\'.
dsn_tns = cx_Oracle.makedsn(
    'BASN-NITRO5',
    '1521',
    service_name='orcl')
# if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
conn = cx_Oracle.connect(
    user=r'system',
    password='Basn1234',
    dsn=dsn_tns
)
c = conn.cursor()
c.execute('SELECT * FROM TEST')

print(c)
for row in c:
    # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
    print(row)
conn.close()
