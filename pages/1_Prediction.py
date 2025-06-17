import streamlit as st
import itertools
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from Bio.SeqIO import parse
import io
import pickle as pkl
import joblib
import base64

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


st.header("Predict Heavy Metal Resistance Proteins")
metal = st.selectbox("Select Heavy Metal", ["Zinc", "Silver", "Mercury", "Nickle", "Cadmium", "Chromium", "Copper", "Iron", "Lead"])

tab1, tab2 = st.tabs(["Paste FASTA Sequence", "Upload FASTA File"])

with tab1:
    st.markdown("**Paste FASTA Sequences:**")
    text_input = st.text_area("Enter sequence in FASTA format")
with tab2:
    st.markdown("**Upload FASTA File:**")
    fasta_file = st.file_uploader("Upload a .fasta file", type=["fasta", "fa"])

def parse_fasta(fasta_text):
    sequences = []
    current_seq = ""
    for line in fasta_text.strip().splitlines():
        if line.startswith(">"):
            if current_seq:
                sequences.append(current_seq)
                current_seq = ""
        else:
            current_seq += line.strip()
    if current_seq:
        sequences.append(current_seq)
    return sequences

def compute_features(sequences):
    from collections import Counter
    AMINO_ACIDS = list("ACDEFGHIKLMNPQRSTVWYU")
    features = []
    for seq in sequences:
        seq = ''.join([aa for aa in seq.upper() if aa in AMINO_ACIDS])
        if not seq:
            continue
        length = len(seq)
        counts = Counter(seq)
        vec = [counts.get(aa, 0)/length for aa in AMINO_ACIDS]
        features.append(vec)
    return pd.DataFrame(features, columns=[f"AA_{aa}" for aa in AMINO_ACIDS])

if st.button("Predict"):
    fasta_data = ""
    if fasta_file:
        fasta_data = fasta_file.read().decode("utf-8")
    elif text_input:
        fasta_data = text_input

    if fasta_data:
        sequences = parse_fasta(fasta_data)
        features_df = compute_features(sequences)
        model = joblib.load(f"static/models/{metal}_RF_model.joblib")
        proba = model.predict_proba(features_df)
        preds = (proba[:, 1] >= 0.5).astype(int)
        pred_labels = ["Yes" if p == 1 else "No" for p in preds]

        results_df = pd.DataFrame({
                "Sr. No.": list(range(1, len(sequences)+1)),
                "FASTA Sequence": sequences,
                "Probability (No Heavy Metal Resistance)": proba[:, 0],
                "Probability (Heavy Metal Resistance)": proba[:, 1],
                "Prediction (Heavy Metal Resistance)": pred_labels
            })

        #csv = results_df.to_csv(index=False)
        #b64 = base64.b64encode(csv.encode()).decode()
        #href = f'<a href="data:file/csv;base64,{b64}" download="prediction_output.csv">Download Output</a>'
        #st.markdown(href, unsafe_allow_html=True)

        st.markdown("### Prediction Results")
        st.dataframe(results_df.style.set_properties(subset=['FASTA Sequence'], **{'overflow-x': 'auto'}), use_container_width=True)
    else:
        st.warning("Please provide input through text area or upload a FASTA file.")



# print(result_df)

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2025 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)
