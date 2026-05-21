import streamlit as st # type: ignore[import]
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard


def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == 'login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()

def teacher_screen_login():
    c1,c2 = st.columns(2, vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button('Go back home', type='secondary',key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()
   
    st.header('Log in using password',text_alignment='center')
    st.space()
    st.space()
    teacher_username = st.text_input('Enter username', placeholder='Enter username')
    teacher_password = st.text_input('Password', placeholder='Enter password', type='password')

    st.divider()
    btnc1,btnc2 = st.columns(2)

    with btnc1:
        st.button('Login',icon=':material/passkey:', shortcut='control+enter', width='stretch')
    with btnc2:
        if st.button('Register Instead',type='primary',icon=':material/app_registration:', width='stretch'):
            st.session_state.teacher_login_type = 'register'
            

    footer_dashboard()


def teacher_screen_register():
    c1,c2 = st.columns(2, vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
       if st.button('Go back home', type='secondary',key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()
   
    st.header('Register your teacher profile')

    st.space()
    st.space()
    teacher_username = st.text_input('Enter username', placeholder='Enter username')
    teacher_name = st.text_input('Enter name', placeholder='Enter name')
    teacher_password = st.text_input('Password', placeholder='Enter password', type='password')
    teacher_confirm_pass = st.text_input('Confirm Password', placeholder='Confirm password', type='password')


    st.divider()
    btnc1,btnc2 = st.columns(2)

    with btnc1:
        st.button('Register now',icon=':material/passkey:', shortcut='control+enter', width='stretch')
    with btnc2:
        if st.button('Login Instead',type='primary',icon=':material/app_registration:', width='stretch'):
            st.session_state.teacher_login_type = 'login'

    footer_dashboard()