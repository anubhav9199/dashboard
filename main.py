import streamlit as st

import src.page.upload
import src.page.plot

from Lib.utils import render_page

MENU = {
    "Plots & Graphs" : src.page.plot,
    "Data Upload" : src.page.upload
}


def _main():

    st.sidebar.title("My Dashboard")
    st.sidebar.title("\n")
    st.sidebar.title("\n")
    st.sidebar.title("\n")

    add_selector = st.sidebar.selectbox(
        'Dashboard Menu',
        ("Plots & Graphs", "Data Upload",)
    )

    menu = MENU[add_selector]

    with st.spinner(f"Loading {add_selector} ....."):
        render_page(menu)


if __name__ == '__main__' :
    
    _main()
