import streamlit as st
import os
import platform

current_os = platform.system().lower()
print(current_os)
if current_os == "windows":
    parameter = "-n"
else:
    parameter = "-c"

ip = "127.0.0.1"
exit_code = os.system(f"ping {ip}")
print(exit_code)
if exit_code == 0:
    st.text(f'{ip} -> OK')
else:
    st.text(f'{ip} -> FAIL')
