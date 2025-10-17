import streamlit as st
import numpy as np
import pandas as pd
from helper import get_precautions
df=pd.read_csv('Aidoctor.csv')

st.markdown("""
    <style>
    .stApp {
        background-color: lightblue;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)


st.title('👨‍⚕️🩺AI-Smart-Doctor')
st.write('No wait, no worries. Just ask your AI doctor.')

prec_list = df['Disease'].unique()
selected_disease = st.selectbox("Select a disease", prec_list)

# Show precautions only when user selects something
if selected_disease:
    prec_recc = get_precautions(selected_disease, df)

    st.subheader("🛡️ Precautions you should take:")
    for i, p in enumerate(prec_recc, 1):
        st.write(f"{i}. {p}")
