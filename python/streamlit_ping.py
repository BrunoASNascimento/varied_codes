import streamlit as st
import os
import platform


def check_ping(hostname):

    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus


hostname = st.text_input('Input your hostname here:')
st.text(f'{hostname} -> {check_ping(hostname)}')
