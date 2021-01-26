import streamlit as st

def render_page(menupage):
    menupage.write()


def title_awesome(body: str):
    st.title(
        f"{body} "
        # "[![Quantum](https://cdn.rawgit.com/sindresorhus/awesome/"
        # "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]"
        # "(https://github.com/Avkash/mldl)"
    )
