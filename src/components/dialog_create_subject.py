import streamlit as st #type: ignore[import]
from src.database.db import create_subject


@st.dialog("create New subject")
def create_subject_dialog(teacher_id):
    st.write("ENTER THE DETAILS OF NEW SUBJECT")
    sub_id = st.text_input("Subject ID", placeholder = "BTA02106")
    sub_name = st.text_input("Subject Name", placeholder = "Data Structures and Algorithms")
    sub_section = st.text_input("Section", placeholder = "A")

    if st.button("Create subject Now", type = "primary", width ='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject add successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all fields to create new subject") 

