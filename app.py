# import streamlit as st
# from sqlalchemy import create_engine
#
# # Sidebar navigation
# st.sidebar.title("Drug Screening Platform")
# st.sidebar.markdown("### Navigation")
# page = st.sidebar.radio("Select Page:", ["Workflow", "Plots Analysis"])
#
#
# # Load the PostgreSQL URL from Streamlit secrets
# database_url = st.secrets["postgresql"]["url"]
#
# # Create an SQLAlchemy engine
# engine = create_engine(database_url)
#
# # Workflow Page
# if page == "Workflow":
#     st.title("Drug Screening Platform - Workflow")
#
#     # Input fields matching the form in the image
#     st.subheader("Experiment Details")
#     experiment_name = st.text_input("Project name:")
#     sample_id = st.text_input("SampleID:")
#     label = st.text_input("Label:")
#
#     # Checkbox for Attract Clinical report
#     attract_clinical_report = st.checkbox("Add Attract Clinical report")
#
#     # Readout day input
#     readout_day = st.number_input("Readout day:", min_value=1, step=1)
#
#     # Well columns input
#     st.subheader("Plate Details")
#     well_columns = st.text_input("Well columns of the plate0 (e.g., 2,3,4 or range 2-4):")
#
#     # File uploader for readout files (assuming 5 files as in the image)
#     st.subheader("Upload Readout Files")
#     readout_files = [st.file_uploader(f"Upload readout file p{i}", type=["csv", "xls", "xlsx"]) for i in range(5)]
#
#     # File uploader for layout template
#     layout_template = st.file_uploader("Layout template upload", type=["csv", "xls", "xlsx"])
#
#     # Button to submit form
#     if st.button("Run"):
#         st.write("Processing your request...")
#         # Here you can add the code to handle the form submission and uploaded files
#
# # Placeholder for Plots Analysis page
# elif page == "Plots Analysis":
#     st.title("Drug Screening Platform - Plots Analysis")
#     st.write("This section will provide data visualization options and analysis plots.")
#     # You can expand this section based on the information you provide later
import streamlit as st
from sqlalchemy import create_engine, text
from datetime import datetime
import re

# Load the PostgreSQL URL from Streamlit secrets
database_url = st.secrets["postgresql"]["url"]

# Create an SQLAlchemy engine
engine = create_engine(database_url)

# Sidebar navigation
st.sidebar.title("Drug Screening Platform")
st.sidebar.markdown("### Navigation")
page = st.sidebar.radio("Select Page:", ["Workflow", "Plots Analysis"])


# Function to generate the next version based on project and sample_id
def get_next_version(project, sample_id):
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT version FROM Experiment
                WHERE project = :project AND sample_id = :sample_id
                ORDER BY experiment_id DESC LIMIT 1
            """),
            {"project": project, "sample_id": sample_id}
        ).fetchone()

    if result:
        latest_version = result[0]
        major, minor = map(int, re.findall(r'\d+', latest_version))
        new_version = f"v{major}.{minor + 1}"
    else:
        new_version = "v1.0"

    return new_version


# Function to insert experiment data and retrieve experiment_id
def insert_experiment(project, sample_id, version, experiment_name):
    with engine.connect() as connection:
        query = text("""
            INSERT INTO Experiment (
                project, sample_id, version, experiment_name, timestamp
            ) VALUES (
                :project, :sample_id, :version, :experiment_name, :timestamp
            ) RETURNING experiment_id
        """)
        result = connection.execute(query, {
            "project": project,
            "sample_id": sample_id,
            "version": version,
            "experiment_name": experiment_name,
            "timestamp": datetime.now()
        })
        experiment_id = result.fetchone()[0]
        return experiment_id


# Function to insert plate and file data into plates_info table
def insert_plate_info(experiment_id, plate_number, file_name, file_data):
    with engine.connect() as connection:
        query = text("""
            INSERT INTO plates_info (experiment_id, plate_number, file_name, file_data)
            VALUES (:experiment_id, :plate_number, :file_name, :file_data)
        """)
        connection.execute(query, {
            "experiment_id": experiment_id,
            "plate_number": plate_number,
            "file_name": file_name,
            "file_data": file_data
        })


# Workflow Page
if page == "Workflow":
    st.title("Drug Screening Platform - Workflow")

    # Input fields for experiment details
    st.subheader("Experiment Details")
    project = st.text_input("Project name:")
    sample_id = st.text_input("SampleID:")
    label = st.text_input("Label:")

    # Checkbox for Attract Clinical report
    attract_clinical_report = st.checkbox("Add Attract Clinical report")

    # Readout day input
    readout_day = st.number_input("Readout day:", min_value=1, step=1)

    # Plate details
    st.subheader("Plate Details")
    well_columns = st.text_input("Well columns of the plate0 (e.g., 2,3,4 or range 2-4):")
    #plate_number = st.number_input("Plate Number", min_value=1, step=1)

    # File uploader for readout files
    st.subheader("Upload Readout Files")
    readout_files = [st.file_uploader(f"Upload readout file p{i}", type=["csv", "xls", "xlsx"]) for i in range(5)]

    # File uploader for layout template
    layout_template = st.file_uploader("Layout template upload", type=["csv", "xls", "xlsx"])

    # Button to submit form
    if st.button("Run"):
        if project and sample_id:
            st.write("Processing your request...")

            # Step 1: Generate version and experiment name
            version = get_next_version(project, sample_id)
            experiment_name = f"{project}_{sample_id}_{version}"

            # Step 2: Insert into Experiment table and get the generated experiment_id
            experiment_id = insert_experiment(project, sample_id, version, experiment_name)

            # Step 3: Insert each uploaded file into plates_info table
            for i, uploaded_file in enumerate(readout_files):
                if uploaded_file:
                    file_name = uploaded_file.name
                    file_data = uploaded_file.read()
                    insert_plate_info(experiment_id, i, file_name, file_data)

            # Step 4: Insert layout template if uploaded
            if layout_template:
                layout_file_name = layout_template.name
                layout_file_data = layout_template.read()
                insert_plate_info(experiment_id, "layout", layout_file_name, layout_file_data)

            st.success("Experiment and associated files inserted successfully!")
        else:
            st.warning("Please fill in all required fields: Project Name and Sample ID.")

# Placeholder for Plots Analysis page
elif page == "Plots Analysis":
    st.title("Drug Screening Platform - Plots Analysis")
    st.write("This section will provide data visualization options and analysis plots.")
