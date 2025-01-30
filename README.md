AI-Powered Resume Analyzer

Try : https://ai-smartscan-resume.streamlit.app/

# AI-Powered Resume Analyzer

AI-Powered Resume Analyzer is an intelligent application designed to mimic the expertise of an HR professional. This tool leverages Google Generative AI (Gemini) to analyze resumes, evaluate job compatibility, and offer actionable insights for career enhancement.

## 📋 Project Overview

The AI-Powered Resume Analyzer acts as a virtual HR assistant, providing:

- Detailed resume evaluation, including strengths and weaknesses.
- Suggestions for skill improvement and recommended courses.
- Job-specific resume analysis to measure compatibility with job descriptions.
- Match percentage score for job relevance.

Whether you’re a job seeker or a recruiter, this tool simplifies resume assessment and improvement.

---

## 🔑 Features

### 1️⃣ General Resume Analysis
- Summarizes the resume in one line.
- Highlights existing skill sets.
- Identifies skill gaps and suggests improvements.
- Recommends popular courses to enhance the resume.
- Provides a thorough evaluation of strengths and weaknesses.

### 2️⃣ Resume Matching with Job Description
- Analyzes resume compatibility with a specific job description.
- Provides a match score in percentage.
- Highlights missing skills and areas needing improvement.
- Suggests whether the resume is ready for the job or requires further enhancements.

---

## 🛠️ Tech Stack

| Component        | Technology |
|-----------------|------------|
| **Frontend**    | Streamlit  |
| **Backend**     | Python     |
| **AI Model**    | Google Generative AI (Gemini) |
| **PDF Parsing** | pdfplumber |
| **OCR Fallback** | pytesseract |
| **Environment Config** | dotenv (.env) for API key security |

---

## 📊 How It Works

### 1️⃣ Resume Parsing
- Extracts text from PDF files using `pdfplumber`.
- Uses OCR (`pytesseract`) as a fallback for scanned/image-based PDFs.

### 2️⃣ AI Analysis
- Utilizes Google Gemini AI to summarize and analyze resume content.
- Matches skills with job descriptions for compatibility scoring.

### 3️⃣ Insightful Feedback
- Provides actionable suggestions for skill enhancement, including course recommendations.
- Highlights strengths and weaknesses to refine resumes for better opportunities.

---

## 🚀 Getting Started

### 🔹 Prerequisites
- Python 3.8+
- Streamlit
- pdfplumber
- pytesseract
- google-generativeai
- dotenv

### 🔹 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI-Resume-Analyzer.git
   cd AI-Resume-Analyzer
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```
5. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

---

## 🙌 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Submit a pull request with detailed information about your modifications.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For any queries or feedback, reach out to:
- **Developer:** [Himanshu Nagapure](https://www.linkedin.com/in/himanshunagapure)
- **Email:** himunagapure114@gmail.com

---

🚀Developed by **Himanshu Nagapure**
