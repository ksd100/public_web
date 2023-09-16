# from calendar import c
# from turtle import clear
import streamlit as st
# from multiapp import MultiApp
from cgitb import enable

import time, datetime

import subprocess
import sys

import streamlit.components.v1 as stc
import os



# Change titles and icons for external and
filepath = os.path.abspath(__file__)

if "streamlit" in filepath:
    webTitle=":house: Trial Site"
    webTab="Trial Site"

    favicon = "./img/favicon/speed.png"

else:
    webTitle=":evergreen_tree: Trial Site -Local"
    webTab="Trial Site -L"

    favicon = "./img/favicon/python.ico"


def web_Home():
    st.set_page_config(page_title=webTab, page_icon=favicon)
    st.title(webTitle)
    st.write('')
    st.write('')
    st.write('**:blue[You do not have to enter the same information over and over again.]**')


    # st.write('')
    st.write('')

    st.write('Please navigate from the menu on the left.')




# 画面起動
if __name__ == "__main__":
    web_Home()






    


    



