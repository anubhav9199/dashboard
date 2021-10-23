import streamlit as st
import pandas as pd

def _dataframe_extractor(data_file):
    _type = data_file.type

    if _type == "text/csv":
        dataframe = pd.read_csv(data_file)
    elif _type == "text/xlsx" or _type == "text/xls":
        dataframe = pd.read_excel(data_file)

    return dataframe

def file_upload_main(title, subtitle):

    st.sidebar.title(title)
    st.sidebar.info(subtitle)

    _data_file = st.file_uploader("Upload Data", type=["csv", "xlsx", 'xls'])

    if _data_file is not None:
        dataframe = _dataframe_extractor(_data_file)
        data_col = [r for r in dataframe.columns]
        