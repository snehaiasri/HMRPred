import streamlit as st

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

st.header("Welcome to HMRPred")
st.markdown("""
**HMRPred** is a machine learning-based predictive framework for the identification of heavy metal resistance (HMR) proteins across ten critical metals:
cadmium, arsenic, chromium, copper, iron, lead, mercury, nickel, silver, and zinc.

Heavy metal contamination is a serious environmental and agricultural concern. HMRPred helps in genome-wide mining and annotation of metal resistance proteins using optimized ensemble learning classifiers.

- Covers bacteria, archaea, and selected eukaryotes.
- Utilizes amino acid composition, physicochemical features, and evolutionary profiles.
- Provides high prediction accuracy (90–96%).
- Useful in bioremediation, biosensor design, phytoremediation, and synthetic biology.

""")

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2025 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)
