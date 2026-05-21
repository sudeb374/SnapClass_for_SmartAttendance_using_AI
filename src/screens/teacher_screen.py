import streamlit as st # type: ignore[import]
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from src.database.db import check_teacher_exits, create_teacher,teacher_login

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
        if st.button('Login',icon=':material/passkey:', shortcut='control+enter', width='stretch'):
            if teacher_login(teacher_username,teacher_password):
                st.toast("Welcome Back!", icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error('Invalid username or password. Please try again.')

    with btnc2:
        if st.button('Register Instead',type='primary',icon=':material/app_registration:', width='stretch'):
            st.session_state.teacher_login_type = 'register'

    footer_dashboard()

def register_teacher(teacher_username, teacher_password, teacher_confirm_pass, teacher_name):
    if not teacher_username or not teacher_password or not teacher_name:
        return False, 'All fields are required.'
    
    if teacher_password != teacher_confirm_pass:
        return False, 'Passwords do not match.'
    
    if check_teacher_exits(teacher_username):
        return False, 'Username already exists. Please choose a different one.'
    try:
      create_teacher(teacher_username, teacher_password, teacher_name)
      return True, 'Registration successful! You can now log in.'
    except Exception as e:
        return False, "Unexpected Error occured"
    
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
        if st.button('Register now',icon=':material/passkey:', shortcut='control+enter', width='stretch'):
            success, message = register_teacher(teacher_username, teacher_password, teacher_confirm_pass, teacher_name)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)
    with btnc2:
        if st.button('Login Instead',type='primary',icon=':material/app_registration:', width='stretch'):
            st.session_state.teacher_login_type = 'login'

    footer_dashboard()