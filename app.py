import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from pdf2image import convert_from_path
import pytesseract
import pdfplumber
from PIL import Image

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
        st.error(f"Direct text extraction failed: {e}")

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
# Page title and description
st.markdown("# Free ATS Resume Checker")
st.markdown(
    "Get hired faster with an ATS-friendly resume. Our free ATS Resume Checker scans resume in depth and delivers instant suggestions to improve your resume score — right from your desktop or mobile device."
)

# Custom CSS
st.markdown(
    """
    <style>
        .stApp {background-color: #0c2340; color: white; padding: 20px; border-radius: 10px;}
        .stButton>button {
            background-color: #00b4d8;
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }
        .title-text {
                font-size: 40px;
                font-weight: bold;
            }
        .subtitle-text {
                font-size: 20px;
                margin-bottom: 20px;
            }
        .stButton>button:hover {
            background-color: #028090;
        }
        .upload-box {
                border: 2px dashed white;
                padding: 20px;
                text-align: center;
                border-radius: 10px;
                background-color: #112b4e;
            }
        .st-emotion-cache-ue6h4q {color: white;}
        .stTextInput, .stTextArea {border-radius: 8px; border: 1px solid #ccc; padding: 12px; width: 100%; font-size: 14px;}
        .stFileUploader {border: 2px dashed white; padding: 20px; border-radius: 12px; text-align: center; background-color: #112b4e; color: white;}
        .stFileUploader:hover {border-color: #128477;}
        .header {text-align: center; font-size: 28px; font-weight: bold; color: #333;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Two-Column Layout
col1, col2 = st.columns([1, 1])
with col1:
    # Why Use an ATS Resume Checker?
    st.markdown("### 📌 Why Optimize Your Resume for ATS?")
    st.write(
        "Most companies use an Applicant Tracking System (ATS) to filter resumes before they reach human recruiters. If your resume isn't optimized, it might never get seen! Our AI-powered tool scans your resume and provides instant suggestions to improve its ATS compatibility."
    )

    # Why Choose AI SmartScan?
    st.markdown("### 🔍 Why Use AI SmartScan?")
    st.write(
        "- **100% Free**: No hidden charges, unlimited scans!"
        "\n- **AI-Powered Analysis**: Get real-time insights powered by cutting-edge AI."
        "\n- **Instant Feedback**: No waiting—get results in seconds."
        "\n- **Simple & User-Friendly**: Upload, scan, and improve your resume with ease."
    )

with col2:
    # Displaying a GIF
    gif_path = "assets/giphy.gif"  # Replace with actual GIF file
    st.image(gif_path, use_container_width=True)

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
