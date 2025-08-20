import fitz  # PyMuPDF
import spacy
from skills_list import skills

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_bytes = uploaded_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    for page in doc:
        text += page.get_text("text")
    return text

def extract_skills(text):
    text_lower = text.lower()
    found_skills = set()
    for skill in skills:
        if skill in text_lower:
            found_skills.add(skill)
    return list(found_skills)

def extract_entities(text):
    doc = nlp(text)
    education, organizations, person_names, dates = [], [], [], []
    for ent in doc.ents:
        if ent.label_ == "ORG":
            organizations.append(ent.text)
        elif ent.label_ == "PERSON":
            person_names.append(ent.text)
        elif ent.label_ in ["DATE", "TIME"]:
            dates.append(ent.text)
        elif ent.label_ in ["GPE", "NORP"]:
            education.append(ent.text)
    return {
        "names": list(set(person_names)),
        "organizations": list(set(organizations)),
        "education": list(set(education)),
        "dates": list(set(dates))
    }
