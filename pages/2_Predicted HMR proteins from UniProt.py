import streamlit as st
import pandas as pd
import glob
import os
import re

def extract_index(filename):
    return int(re.search(r"_(\d+)\.csv$", filename).group(1))

st.set_page_config( page_title="HMRPred", initial_sidebar_state="expanded", layout="wide")
col1, col2, col3 = st.columns([1.5, 20, 2])

with col1:
    st.image("static/images/icarlogo.png", width=150)

with col2:
    st.markdown("<h1 style='text-align:center;'> HMRPred: A Machine Learning-Based Web Resource for Identification of Heavy Metal Resistance Proteins</h1>", unsafe_allow_html=True)

with col3:
    st.image("static/images/iasri-logo.png", width=150)

st.markdown("---")
st.text("")

st.header("Predicted HMR proteins from UniProt")
st.markdown("""
**HMRPred** was used to screen 343,595 unreviewed protein-level UniProt sequences to identify putative heavy metal resistance (HMR) proteins across ten metals. Predictions include metal-specific probability scores and represent computational candidates requiring experimental validation.
Select a metal from the dropdown menu to view the corresponding predicted HMR proteins.
""")

metal = st.selectbox("Select Heavy Metal", ["Arsenic", "Cadmium", "Chromium", "Copper", "Iron", "Lead", "Mercury", "Nickle", "Silver", "Zinc"])

if st.button("Submit"):
    try:
        files = glob.glob(os.path.join(f"static/uniprot/{metal}", f"{metal}_*.csv"))
    
        files = sorted(files, key=extract_index)
    
        dfs = [pd.read_csv(f) for f in files]
        combined_df = pd.concat(dfs, ignore_index=True)
    except Exception as e:
        st.error(e, icon="🚨")
        st.stop()
    
    st.dataframe(data=combined_df, column_config={"Probability":"Probability of HMR Prediction"}, width='stretch')

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2025 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)
