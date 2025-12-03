import streamlit as st
from pages.login import login_page
from search_page import search_page

st.set_page_config(page_title="Job Search App", layout="centered")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login_page()
else:
    search_page()
