# from calendar import c
# from turtle import clear
import streamlit as st
# from multiapp import MultiApp
from cgitb import enable

import time, datetime

import subprocess
import sys
# import pyautogui as pa

import streamlit.components.v1 as stc
import os



# 外部とでタイトルとアイコン変える
filepath = os.path.abspath(__file__)

if "homepc" in filepath:
    webTitle="ST-CLOUD　家PC"
    favicon = "./img/icon/cloud.ico"

else:
    webTitle=":house: Trial Site"
    favicon = "./img/icon/speed.png"


def web_Home():
    st.set_page_config(page_title=webTitle, page_icon=favicon)
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






    


    



