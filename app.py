import streamlit as st
from pypdf import PdfReader

# Page Configuration
st.set_page_config(page_title="PropertyGuardAI", page_icon="🏠")

st.title("🏠 PropertyGuardAI")
st.write("Automated Property Document Analysis & Verification System")

# File Uploader
uploaded_file = st.file_uploader("Upload Property Document (PDF)", type=["pdf"])

if uploaded_file is not None:
    # PDF Text Extraction
    pdf_reader = PdfReader(uploaded_file)
    extracted_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text + "\n"

    st.success("✅ PDF successfully uploaded and processed!")
    
    # Document Preview & Details
    st.subheader("📄 Extracted Document Data")
    st.text_area("Extracted Content", value=extracted_text, height=300)
    
    # Quick Statistics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Pages", len(pdf_reader.pages))
    with col2:
        st.metric("Total Character Count", len(extracted_text))