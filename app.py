import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from pdf2image import convert_from_path
import pytesseract
import pdfplumber

# Load environment variables
load_dotenv()

# Configure Google Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        # Try direct text extraction
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        if text.strip():
            return text.strip()
    except Exception as e:
        print(f"Direct text extraction failed: {e}")

    # Fallback to OCR for image-based PDFs
    print("Falling back to OCR for image-based PDF.")
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            page_text = pytesseract.image_to_string(image)
            text += page_text + "\n"
    except Exception as e:
        st.error(f"OCR failed: {e}")

    return text.strip()

# Function to get response from Gemini AI
def analyze_resume(resume_text, job_description=None):
    if not resume_text:
        return {"Error": "Resume text is required for analysis."}
    
    base_prompt = f"""
    ou are an experienced HR with Technical Experience in the field of any one job role from Data Science, Data Analyst, DevOPS, Machine Learning Engineer, Prompt Engineer, AI Engineer, Full Stack Web Development, Big Data Engineering, Marketing Analyst, Human Resource Manager, Software Developer. Your task is to review the provided resume.
    Please share your professional evaluation on whether the candidate's profile aligns with the role. Identify current Skills, strengths, weaknesses and USP. Also suggest some skills to improve his resume and suggest some courses to improve the skills.

    Resume:
    {resume_text}
    """

    if job_description:
        base_prompt += f"""
        Additionally, compare this resume against the following job description. Start by providing match percentage if the resume matches. Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements. At the end mention missing keywords to add and last final thoughts.
        
        Job Description:
        {job_description}
        
        """

    response = model.generate_content(base_prompt)

    analysis = response.text.strip()
    return analysis


# Streamlit app

st.set_page_config(page_title="AI SmartScan", page_icon="📊", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
        .main {background-color: #f4f4f4; padding: 20px; border-radius: 10px;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 16px; padding: 12px; border-radius: 8px; border: none; cursor: pointer; transition: 0.3s;}
        .stButton>button:hover {background-color: #45a049;}
        .stTextInput, .stTextArea {border-radius: 8px; border: 1px solid #ccc; padding: 12px; width: 100%; font-size: 14px;}
        .stFileUploader {border: 2px dashed #aaa; padding: 20px; border-radius: 12px; text-align: center; background-color: #fff;}
        .stFileUploader:hover {border-color: #4CAF50;}
        .header {text-align: center; font-size: 28px; font-weight: bold; color: #333;}
    </style>
    """,
    unsafe_allow_html=True,
)
# Title
st.markdown("<h1 class='header'> AI-Powered Resume Screening System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Analyze your resume and get feedback on how well it matches a job description.</p>", unsafe_allow_html=True)

col1 , col2 = st.columns([1,1])
with col1:
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
with col2:
    job_description = st.text_area("Enter Job Description:", placeholder="Paste the job description here...")

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")
else:
    st.warning("Please upload a resume in PDF format.")


st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
if uploaded_file:
    # Save uploaded file locally for processing
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    # Extract text from PDF
    resume_text = extract_text_from_pdf("uploaded_resume.pdf")

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing..."):
            try:
                # Analyze resume
                analysis = analyze_resume(resume_text, job_description)
                st.success("✅ Analysis complete!")
                st.markdown("### 📊 Analysis Report")
                st.write(analysis)
                st.download_button("📥 Download Report", analysis, file_name="Resume_Analysis.txt")
            except Exception as e:
                st.error(f"Analysis failed: {e}")

#Footer
st.markdown("---")
st.markdown("""<p style= 'text-align: center;' >🚀 Powered by <b>Streamlit</b> and <b>Google Gemini AI</b> | Developed by <a href="https://www.linkedin.com/in/himanshunagapure"  target="_blank" style='text-decoration: none; color: light blue'><b>Himanshu Nagapure</b></a></p>""", unsafe_allow_html=True)