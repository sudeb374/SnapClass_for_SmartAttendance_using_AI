import streamlit as st  # type: ignore[import]

def footer_home():

    st.markdown(f"""
        <div style='margin-top: 10px; display:flex; gap:6px; justify-content: center; item-align: center;'>
            <p style='font-weight: bold; font-size: 20px; color:white;'>Developed by Sudeb 🇮🇳</p>
        </div>
        """, unsafe_allow_html=True
    )

def footer_dashboard():

    st.markdown(f"""
        <div style='margin-top: 10px; display:flex; gap:6px; justify-content: center; item-align: center;'>
            <p style='font-weight: bold; font-size: 20px; color:black;'>Developed by Sudeb 🇮🇳</p>
        </div>
        """, unsafe_allow_html=True
    )