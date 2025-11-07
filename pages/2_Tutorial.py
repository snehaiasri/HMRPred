import streamlit as st
import base64

file_path = "static/HMRPred_Tutorial.pdf"
with open(file_path,"rb") as f:

    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'

st.markdown(pdf_display, unsafe_allow_html=True)
