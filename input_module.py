import streamlit as st

def render_input_section():
    st.header("📥 Input Module - Property & Document Upload")
    
    uploaded_file = st.file_uploader("Upload Property Document (PDF)", type=["pdf"])
    
    st.subheader("Property Information")
    col1, col2 = st.columns(2)
    with col1:
        property_id = st.text_input("Property ID", value="PROP-001")
        location = st.text_input("Property Location", value="Okara")
        property_type = st.selectbox("Property Type", ["House", "Plot", "Commercial"])
    with col2:
        area = st.text_input("Property Area", value="10 Marla")
        owner_name = st.text_input("Owner Name", value="Ali")
        asking_price = st.text_input("Asking Price", value="1.5 Crore")
        
    return uploaded_file, {
        "property_id": property_id,
        "location": location,
        "property_type": property_type,
        "area": area,
        "owner_name": owner_name,
        "asking_price": asking_price
    }
