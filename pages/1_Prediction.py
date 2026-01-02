import streamlit as st
import pandas as pd
from Bio import SeqIO
import joblib
from io import StringIO
from static.code import *
import re

if "fasta_data" not in st.session_state:
    st.session_state.fasta_data = ""

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

file_path = 'static/example.fasta' 

btn_col1, btn_col2, _ = st.columns([4, 4, 16])

with open(file_path, "rb") as file:
    file_content = file.read()

with btn_col1:
    st.download_button(
        label="📥 Download Sample File",
        data=file_content,
        file_name="example.fasta",
        mime="text/plain"
    )

with btn_col2:
    run_example = st.button("▶ Run Example Sequence")

metal = st.selectbox("Select Heavy Metal", ["Arsenic", "Cadmium", "Chromium", "Copper", "Iron", "Lead", "Mercury", "Nickle", "Silver", "Zinc"])

tab1, tab2 = st.tabs(["Paste FASTA Sequence", "Upload FASTA File"])

with tab1:
    st.markdown("**Paste FASTA Sequences:**")
    text_input = st.text_area("Enter sequence in FASTA format")
with tab2:
    st.markdown("**Upload FASTA File:**")
    fasta_file = st.file_uploader("Upload a .fasta file", type=["fasta", "fa"])
    st.markdown(":orange-badge[⚠️ Please remove any file uploaded here before running Single Sequence in the 'Paste FASTA Sequence' tab]")

def error_msg(e):
    st.error(e, icon="🚨")
    st.stop()

def read_excelConfig(METAL_NAME):
    cfg = pd.read_csv(f"static/features_file.csv")

    row = cfg[cfg["Metal"] == METAL_NAME]
    
    descriptor_types = [d.strip() for d in row.iloc[0]["Descriptor_Types"].split(",")]
    selected_features = [
        f.strip() for f in row.iloc[0]["Selected_Features"].split(";") if f.strip()
    ]

    return descriptor_types, selected_features


CTDT_GROUPS = {
    "A": 1, "G": 1, "V": 1,
    "I": 2, "L": 2, "F": 2, "P": 2,
    "Y": 3, "M": 3, "T": 3, "S": 3,
    "H": 4, "N": 4, "Q": 4, "W": 4,
    "R": 5, "K": 5,
    "D": 6, "E": 6,
    "C": 7
}

def is_valid_sequence(seq, descriptor_types):
    seq = str(seq)

    if any(d in descriptor_types for d in ["CKSAAP", "CKSAAGP"]) and len(seq) < 7:
        return False

    if "CTriad" in descriptor_types and len(seq) < 3:
        return False

    if "CTDT" in descriptor_types:
        groups = {CTDT_GROUPS[a] for a in seq if a in CTDT_GROUPS}
        if len(groups) < 2:
            return False

    return True


def validate_fasta(FASTA, descriptor_types):
    records = []
    sequences = []
    current_seq = ""

    for line in FASTA.strip().splitlines():
            if line.startswith(">"):
                if current_seq:
                    sequences.append(current_seq)
                    current_seq = ""
            else:
                current_seq += line.strip()
                
    if current_seq:
        sequences.append(current_seq)

    for rec in SeqIO.parse(StringIO(FASTA), "fasta"):
        if is_valid_sequence(rec.seq, descriptor_types):
            records.append(rec)

    try:
        if not records:
            raise RuntimeError("No valid sequences found after validation")
    except RuntimeError as e:
        #print("validate_fasta function")
        error_msg(e)

    fasta_handle = StringIO()
    SeqIO.write(records, fasta_handle, "fasta")
    fasta_handle.seek(0)
    fasta_string = fasta_handle.read()
    return fasta_string, sequences


def ifeature(validated_fasta, descriptor_types):
    fastas = []
    
    try:
        if re.search('>', validated_fasta) == None:
            raise ValueError("The input file seems not in FASTA format.")
        
        validated_fasta = validated_fasta.split('>')[1:]
        
        for fasta in validated_fasta:
            array = fasta.split('\n')
            name, sequence = array[0].split()[0], re.sub('[^ARNDCQEGHILKMFPSTWYV-]', '-', ''.join(array[1:]).upper())
            fastas.append([name, sequence])
    
    except ValueError as e:
        #print("ifeature value error")
        error_msg(e)
    except Exception as e:
        #print("ifeature exception")
        error_msg(e)

    myFun = descriptor_types + '.' + descriptor_types + '(fastas)'
    encodings = eval(myFun)

    return encodings

def feature_extraction(validated_fasta, descriptor_types):
    feature_dfs = []

    for desc in descriptor_types:
        encodings = ifeature(validated_fasta, desc)
        df = pd.DataFrame(encodings[1:], columns=encodings[0])

        feature_cols = [
            c for c in df.columns
            if c.lower() not in ["#", "name", "label", "sequence"]
        ]

        df.rename(columns={c: f"{desc}_{c}" for c in feature_cols}, inplace=True)
        df = df[[f"{desc}_{c}" for c in feature_cols]]

        feature_dfs.append(df)

    return feature_dfs

def feature_assembly(feature_dfs, selected_features):
    full_df = pd.concat(feature_dfs, axis=1)

    for feat in selected_features:
        if feat not in full_df.columns:
            full_df[feat] = 0.0

    X = full_df[selected_features]

    return X

predict = st.button("Predict")

if predict or run_example:
    st.session_state.fasta_data = None
    if fasta_file is not None:
        st.session_state.fasta_data = fasta_file.read().decode("utf-8")

    elif text_input.strip() != "":
        st.session_state.fasta_data = text_input

    if run_example:
        st.session_state.fasta_data = file_content.decode("utf-8")
    
    run_example = False

    if st.session_state.fasta_data:
        fasta_data = st.session_state.fasta_data
        descriptor_types, selected_features = read_excelConfig(metal)
        validated_fasta, sequences = validate_fasta(fasta_data, descriptor_types)
        feature_dfs = feature_extraction(validated_fasta, descriptor_types)
        X = feature_assembly(feature_dfs, selected_features)
        model = joblib.load(f"static/models/{metal}.pkl")
        proba = model.predict_proba(X)
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
        st.dataframe(results_df.style.format({
            "Probability (No Heavy Metal Resistance)": "{:.2f}",
            "Probability (Heavy Metal Resistance)": "{:.2f}"
        }).set_properties(subset=['FASTA Sequence'], **{
                        "white-space": "nowrap",
                        "overflow": "auto",
                        "display": "block",
                        "font-family": "monospace",
                        "max-width": "400px"
                    }), width='stretch', hide_index=True)
    else:
        st.warning("Please provide input through text area or upload a FASTA file.")

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2025 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)
