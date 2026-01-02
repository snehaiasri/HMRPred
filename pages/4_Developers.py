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

col1_1, col2_1 =st.columns([1, 1])

with col1_1:
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/Sneha_murmu.png")
        with colInCon_2:
            st.markdown('''**Dr. Sneha Murmu**  
                        Scientist  
                        Division of Agricultural Bioinformatics  
                        ICAR-Indian Agricultural Statistics Research Institute  
                        Pusa, New Delhi-110012, India.
                        Contact mail: sneha.murmu07@gmail.com''')
    
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            #st.image("")
            pass
        with colInCon_2:
            st.markdown("""**Jaya Krishna**  
                        Division of Agricultural Bioinformatics  
                        ICAR-Indian Agricultural Statistics Research Institute  
                        Pusa, New Delhi-110012, India.
                        Contact mail: jayakrishna338@gmail.com""")

with col2_1:
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/himanshu_pic.jpeg")
        with colInCon_2:
            st.markdown('''**Dr. Himanshushekhar Chaurasia**  
                        Scientist (Computer Application & IT)  
                        Mechanical Processing Division  
                        ICAR - Central Institute for Research on Cotton Technology,  
                        Mumbai, Maharashtra-400019, India.  
                        Contact mail: h.chaurasia@icar.org.in''')
            

            
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            pass
            #st.image("")
        with colInCon_2:
            st.markdown('''**Dr. Girish Kumar Jha**  
                        Principal Scientist  
                        Division of Agricultural Bioinformatics  
                        ICAR-Indian Agricultural Statistics Research Institute  
                        Pusa, New Delhi-110012, India.  
                        Contact mail: girish.stat@gmail.com''')


st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2025 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)