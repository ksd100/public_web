from docx import Document
from datetime import datetime
import streamlit as st
import shutil
from pathlib import Path
import os
from PIL import Image
import pandas as pd

from streamlit_extras.colored_header import colored_header

# ---------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------


# String definition from here. Change it for local and external.
filepath = os.path.abspath(__file__)

# Strings on external public sites
if "Local" not in filepath:
    inputFolder = fr"..\input\boot_bat"
    inputFile = fr"{inputFolder}\master_boot.bat"
    outputFolder =  fr"..\output\boot_bat"
    webTitle = ":rocket: Delayed app launch batch creation"
    webTab = "Create batch"

    iconPath = "./img/favicon/cloud.ico"

# String in local environment
else:
    inputFolder =fr"C:\Users\j111718\AppData\Local\Programs\Python\workspace\homePC_code\input\boot_bat"
    inputFile = fr"{inputFolder}\master_boot.bat"
    outputFolder =  fr"C:\Users\j111718\AppData\Local\Programs\Python\workspace\homePC_code\output\boot_bat"
    webTitle = ":hotdog: Delayed app launch batch creation -L"
    webTab = "Create batch -L"

    iconPath = "./img/favicon/python.ico"


# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


# ---------------------------------------------------------------------------------------


# character string definition
dataDict = {
    "creating": [False, False, False,  False, False, False, False, False, False, False, False, False, False, False, False, False],
    "Device (not editable)": ["Database device", "Calculating device1", "Calculating device2",  "External communicating device",  "Display device1", "Display device2", "Training devices",   "Other device", "Other device", "Other device" , "Remote calculating device1", "Remote display device1", "Remote display device2",  "Remote other device", "Remote other device" , "Remote other device" ], 
    "file-name": ["db-pc", "calc-pc1", "calc-pc2", "comm-pc", "disp-pc1", "disp-pc2", "train-pc",  "aXXX-pc", "bXXX-pc", "cXXX-pc", "R-calc-pc", "R-disp-pc1", "R-disp-pc2",  "R-dXXX-pc", "R-eXXX-pc", "R-fXXX-pc"], 
    "Node No.": ["130", "100", "101",  "170", "150", "151", "190",  "X", "X", "X", "130", "150", "151",  "X", "X", "X"], 
    "Launch delay (sec)": ["30", "90", "120", "150", "180", "190", "200",  "X", "X", "X", "30", "90", "120",  "X", "X", "X"]
    }

machineList = dataDict['Device (not editable)']



# initialization
checkNG = 1


# message definition
waitMsg = ""
compMsg = f"Created in the above folder. **Check the contents of the batch file.**"


# ---------------------------------------------------------------------------------------
# Function from here

# Replace in text file
def rep_TextFile(file_path, old_text, new_text):

    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace(old_text, new_text)

    with open(file_path, 'w') as file:
        file.write(content)


# error check
def error_check(outputOfficeFolder, folderPath, office, checkNG):

    # Folder existence check
    file_path = Path(outputOfficeFolder)

    # Item Incomplete Check
    if office == "":      
        st.warning('Please enter the name of office.')
    
        return 0

    elif folderPath == "":      
        st.warning('Enter the folder path for Exe.')
    
        return 0
    
    
    elif checkNG:
        st.warning('No device is selected.')

    
    elif file_path.exists():
        st.error(fr"{outputOfficeFolder} folder already exists. **:red[Please change the office name or delete (boot_bat_{office} )folder.]**")

        return 0
    
    else:
        return 1

# ---------------------------------------------------------------------------------------

# WEB from here
def web_Home(webTitle, webTab):
    st.set_page_config(page_title=webTab, page_icon=iconPath)
    
    st.title(webTitle)
    st.write("")

    st.write("**Set according to your system.**")
    st.write("")

    st.write("")
    # st.write("")

    st.write(':large_blue_diamond:**:blue[1. first, set the following]**')
 
    folderPath = st.text_input(fr"Folder with Exe (e.g. C:\Users\2023-02-02-XXXX\Develop\Exe)")
    exeName = st.text_input(fr"Name of the exe", placeholder="exe filename (excluding file extensions)")

    col11, col12 = st.columns(2)
    office = col11.text_input(fr'Abbreviation for  Office',  placeholder=fr"slc, etc. (for Salt Lake City)")
    office2 = col12.text_input(fr'Abbreviation for Remote Office (May be omitted)')

    # Last Blank Field Deletion Process
    folderPath = folderPath.rstrip()
    office = office.rstrip()
    office2 = office2.rstrip()
    exeName = exeName.rstrip()

    st.write("---")

    st.write(f':large_blue_diamond:**:blue[2. Next, check the target device.]**  (Others are changed as needed)')



    # Put e front of the line. the office at the front of the line.
    for i, str in enumerate(dataDict['file-name']):
        if "R-" in str:
            dataDict['file-name'][i] = f"{office2}-{str[2:]}" 
        else:
            dataDict['file-name'][i] = f"{office}-{str}"




    df = pd.DataFrame(dataDict)

    iElm = len(dataDict["creating"])

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
        height=iElm*38,
        disabled=["Device (not editable)"]
    )

    # Variable initialization
    updated_data = {
        'creating':[],
        'Device (not editable)': [],
        'file-name': [],
        'Node No.': [],
        'Launch delay (sec)': []
    }

    # Convert edited DF to dictionary type
    updated_data = edited_df.to_dict(orient='list')

    # st.write("---")

    colored_header(
        label="",
        description=" ",
        color_name="blue-70",
        )
    col1, col2 = st.columns(2)
    event_ok = col1.button("Create Batch", key='btn_ok')
    guide_text = col2.write('(To clear the entry, press the F5 key.)')

    st.write("")


    # ---------------------------------------------------------------------------
    # Execute button process from here

    if event_ok:

        outputOfficeFolder = fr"{outputFolder}\Boot_bat_{office}"

        # Unchecked decision
        if any(updated_data['creating']):
            checkNG = 0
        else:
            checkNG = 1

        # Checks for input errors and starts if there are no errors
        if error_check(outputOfficeFolder, folderPath, office, checkNG):

            # Office Folder Creation
            os.mkdir(outputOfficeFolder)


            # Checked device file creation
            for i, value in enumerate(updated_data['creating']):
                if value : 

                    # file saving
                    outputDamFile = fr"{outputOfficeFolder}\app_start_{updated_data['file-name'][i]}.bat"
                    shutil.copy2(inputFile, outputDamFile)

                    rep_TextFile(outputDamFile, "val_Time", updated_data['Launch delay (sec)'][i])
                    rep_TextFile(outputDamFile, "val_ExePath", folderPath)
                    rep_TextFile(outputDamFile, "val_App", exeName)

                    rep_TextFile(outputDamFile, "val_Node", updated_data['Node No.'][i])


                else:
                    pass

            st.code(outputOfficeFolder, language="html")
            st.success(compMsg)
    
            st.error(f"If you wish to recreate it, delete the **(boot_bat_{office})**  folder.")

        pass











# ---------------------------------------------------------------------------------------


# main program
if __name__ == "__main__":
    web_Home(webTitle, webTab)


            
