import streamlit as st
import input_module
import output_module
from agents import create_property_guard_crew

st.set_page_config(page_title="PropertyGuardAI", page_icon="📑", layout="wide")
st.title("📑 PropertyGuardAI - Automated Document Analysis")

uploaded_file, property_details = input_module.render_input_section()

st.divider()

output_module.process_and_display_output(uploaded_file, property_details)
# CrewAI execution call
crew = create_property_guard_crew(property_details)
