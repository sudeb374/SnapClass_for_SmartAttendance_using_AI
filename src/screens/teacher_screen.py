import streamlit as st # type: ignore[import]
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard


def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    teacher_screen_login()


def teacher_screen_login():
    c1,c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.button('Go back to Home', type='secondary',key='loginbackbtn',shortcut='control+backspace')

    st.header('Login using password', text_alignment='center')
    st.space()
    st.space()

    teacher_username = st.text_input('Enter your Name:',placeholder='full name',)

    teacher_password = st.text_input('Enter Password:',placeholder='Enter correct password',type='password')
    
    st.divider()

    footer_dashboard()

def teacher_screen_register():
    c1,c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.button('Go back to Home', type='secondary',key='loginbackbtn',shortcut='control+backspace')

    st.header('Register your Teacher Profile')
