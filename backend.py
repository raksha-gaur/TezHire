import google.generativeai as gemini
from llm_application_config import GOOGLE_API_KEY, SAFETY_SETTINGS

GEMINI_MODEL = "models/gemini-1.5-flash-latest"


def generate_job_description(job_title, company_name, brief_desc, skills, experience_level, style):
    """
    Function to generate a job description using the Gemini API.
    """
    prompt = f"""
        Generate a detailed job description for a position with the following information:

        Job Title: {job_title}
        Company Name: {company_name}
        Brief Job Description: {brief_desc}
        Desired Skills: {skills}
        Experience Level: {experience_level}
        writing_style: {style}

        Please provide a professional and detailed job description suitable for a job listing.
        """

    gemini.configure(api_key=GOOGLE_API_KEY)

    try:
        model = gemini.GenerativeModel(model_name=GEMINI_MODEL, safety_settings=SAFETY_SETTINGS)
        response = model.generate_content([prompt])
        generated_text = response.text

        return generated_text

    except Exception as e:
        print(f"Error in generating job description using model - {GEMINI_MODEL}: {e}")
        return ""


def generate_keywords(job_description):
    """
    Function to generate keywords based on the job description.
    """
    try:
        prompt = f"Extract relevant 10 keywords from the following job description:\n\n{job_description}"
        model = gemini.GenerativeModel(model_name=GEMINI_MODEL, safety_settings=SAFETY_SETTINGS)
        response = model.generate_content([prompt])
        keywords = response.text.strip().split(', ')

        return keywords

    except Exception as e:
        print(f"Error in generating keywords using model - {GEMINI_MODEL}: {e}")
        return []
