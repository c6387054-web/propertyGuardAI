import streamlit as st

st.set_page_config(page_title="PropGuard AI", page_icon="🏠", layout="wide")

st.title("🏠 PropGuard AI")
st.subheader("AI-Powered Property Verification & Risk Detection")
st.write("Verify property information and documents to identify possible inconsistencies and risks.")

st.divider()

st.header("📋 Property Information")

col1, col2 = st.columns(2)

with col1:
    property_id = st.text_input("Property ID", value="PROP-001")
    location = st.text_input("Property Location", value="Okara")
    property_type = st.selectbox("Property Type", ["House", "Plot", "Apartment", "Commercial"])

with col2:
    area = st.text_input("Property Area", value="10 Marla")
    owner_name = st.text_input("Owner Name", value="Ali")
    asking_price = st.text_input("Asking Price", value="1.5 Crore")

st.divider()

st.header("📑 Upload Property Documents")
uploaded_file = st.file_uploader("Upload Property Document", type=["pdf", "png", "jpg"])

verify_button = st.button("🔍 Verify Property", type="primary")

if verify_button:
    st.divider()
    st.header("📊 Verification Result")
    
    if uploaded_file is not None:
        st.success("✅ Verification Process Completed Successfully!")
        
        # Display Mock Risk Analysis Results
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.metric(label="Overall Risk Status", value="LOW RISK", delta="Passed")
            st.write("*Area Match:* ✅ Matched (10 Marla)")
            st.write("*Owner Information:* ✅ Matched (Ali)")
            
        with col_res2:
            st.write("*Location Match:* ✅ Matched (Okara)")
            st.write("*Duplicate Property Check:* ✅ No Duplicate Found")
            st.write("*Manual Verification Required:* ❌ No")

        st.info("💡 *AI Summary:* Document text and user inputs match perfectly. No fraud or discrepancy detected.")
        
        st.divider()
        st.subheader("📄 Final Report")
        st.download_button(
            label="📥 Download Risk Assessment Report (PDF)",
            data=f"PropGuard AI Verification Report\nProperty ID: {property_id}\nOwner: {owner_name}\nStatus: Passed (Low Risk)",
            file_name=f"{property_id}_Verification_Report.txt",
            mime="text/plain"
        )
    else:
        st.error("⚠️ Please upload a property document before running the verification.")