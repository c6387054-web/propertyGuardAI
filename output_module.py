import streamlit as st
import pypdf

def process_and_display_output(uploaded_file, property_data):
    st.header("📊 Output Module - Analysis & Risk Assessment")
    
    if uploaded_file is not None:
        try:
            pdf_reader = pypdf.PdfReader(uploaded_file)
            num_pages = len(pdf_reader.pages)
            
            extracted_text = ""
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
            
            st.success("✅ File successfully analyzed!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Total Pages", value=num_pages)
            with col2:
                st.metric(label="Extracted Characters", value=len(extracted_text))
                
            st.subheader("Document Content Preview")
            st.text_area("Extracted Text", value=extracted_text[:2000], height=200)
            
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
    else:
        st.info("Please upload a PDF document in the Input section above.")
