import streamlit as st
from backend import *


st.title("AI-Powered Job Description Generator")

# Input Fields
job_title = st.text_input("Job Title", placeholder="e.g., Machine Learning Intern")
company_name = st.text_input("Company Name", placeholder="e.g., TezHire AI")
brief_desc = st.text_area("Brief Job Description",
                          placeholder="e.g., Assist in developing machine learning models, performing data "
                                      "preprocessing, and helping with model evaluation.")
skills = st.text_input("Desired Skills",
                       placeholder="e.g., Python, TensorFlow, Data Analysis, Machine Learning Algorithms")
experience_level = st.selectbox("Experience Level", options=["Entry-Level", "Mid-Level", "Senior"])

# Additional style feature
style = st.selectbox("Choose Writing Style", options=["Formal", "Informal", "Creative", "Professional"], index=0)

# Optional Features Checkboxes
generate_keywords_checkbox = st.checkbox("Generate Keywords")

# Generate Button
if st.button("Generate Job Description"):
    job_description = generate_job_description(job_title, company_name, brief_desc, skills, experience_level,
                                               style=style)

    if job_description:
        st.subheader("Generated Job Description:")
        st.write(job_description)

        if generate_keywords_checkbox:
            keywords = generate_keywords(job_description)
            st.subheader("Keywords:")
            st.write(", ".join(keywords))
    else:
        st.error("Could not generate job description. Please check your inputs and try again.")
