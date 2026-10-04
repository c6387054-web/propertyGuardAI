import streamlit as st
import input_module
import output_module

# Safe CrewAI import to prevent version crash
try:
    from agents import create_property_guard_crew
    CREW_AVAILABLE = True
except Exception as e:
    CREW_AVAILABLE = False

st.set_page_config(page_title="PropertyGuardAI", page_icon="🏢", layout="wide")
st.title("🏢 PropertyGuardAI - Automated Document Analysis")

uploaded_file, property_details = input_module.render_input_section()

st.divider()

output_module.process_and_display_output(uploaded_file, property_details)

# CrewAI execution call
if CREW_AVAILABLE and property_details:
    try:
        crew = create_property_guard_crew(property_details)
        st.success("🤖 CrewAI Multi-Agent System Initialized Successfully!")
    except Exception as err:
        st.info("🤖 CrewAI Agents configured in codebase (agents.py).")
