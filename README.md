AI CV Screening App

A Streamlit-based AI application to automatically screen resumes against job descriptions. The app extracts skills, identifies entities, and provides a match score to help recruiters shortlist candidates efficiently.


---

📝 Features

Job Description Input: Paste the job description for the desired role.

Resume Upload: Upload candidate resumes in PDF format.

Screening Result: Provides a match score and decision (Shortlisted / Not Shortlisted).

Skill Extraction: Automatically identifies skills like Python, SQL, TensorFlow, etc.

Named Entity Recognition (NER): Extracts candidate details such as names, organizations, education, and dates.



---

🛠 Tech Stack

Python – Core programming language

Streamlit – Web interface

spaCy – NLP for skill extraction and NER

PyPDF2 / pdfminer – PDF parsing

Pandas – Data handling



---

🚀 Installation

1. Clone the repository



git clone https://github.com/shafnajasnin98/cv_screeningApp.git
cd cv_screeningApp

2. Create a virtual environment



python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install dependencies



pip install -r requirements.txt

4. Download spaCy model



python -m spacy download en_core_web_sm


---

⚡ Usage

streamlit run app.py

Paste the job description.

Upload the candidate's resume (PDF).

View the Screening Result, Extracted Skills, and Entities.
