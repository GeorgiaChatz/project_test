import streamlit as st

# Sidebar navigation
st.sidebar.title("Drug Screening Platform")
st.sidebar.markdown("### Navigation")
page = st.sidebar.radio("Select Page:", ["Workflow", "Plots Analysis"])

# Workflow Page
if page == "Workflow":
    st.title("Drug Screening Platform - Workflow")

    # Input fields matching the form in the image
    st.subheader("Experiment Details")
    experiment_name = st.text_input("Experiment name:")
    sample_id = st.text_input("SampleID:")
    label = st.text_input("Label:")

    # Checkbox for Attract Clinical report
    attract_clinical_report = st.checkbox("Add Attract Clinical report")

    # Readout day input
    readout_day = st.number_input("Readout day:", min_value=1, step=1)

    # Well columns input
    st.subheader("Plate Details")
    well_columns = st.text_input("Well columns of the plate0 (e.g., 2,3,4 or range 2-4):")

    # File uploader for readout files (assuming 5 files as in the image)
    st.subheader("Upload Readout Files")
    readout_files = [st.file_uploader(f"Upload readout file p{i}", type=["csv", "xls", "xlsx"]) for i in range(5)]

    # File uploader for layout template
    layout_template = st.file_uploader("Layout template upload", type=["csv", "xls", "xlsx"])

    # Button to submit form
    if st.button("Run"):
        st.write("Processing your request...")
        # Here you can add the code to handle the form submission and uploaded files

# Placeholder for Plots Analysis page
elif page == "Plots Analysis":
    st.title("Drug Screening Platform - Plots Analysis")
    st.write("This section will provide data visualization options and analysis plots.")
    # You can expand this section based on the information you provide later
