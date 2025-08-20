import streamlit as st
from resume_parser import extract_text_from_pdf, extract_skills, extract_entities
from jd_matcher import calculate_similarity

st.title("📄 AI CV Screening App")

jd_input = st.text_area("Paste Job Description Here")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_resume and jd_input:
    resume_text = extract_text_from_pdf(uploaded_resume)
    score = calculate_similarity(jd_input, resume_text)

    # Extract info
    skills = extract_skills(resume_text)
    entities = extract_entities(resume_text)

    st.subheader("✅ Screening Result")
    st.write("Match Score:", round(score, 2), "%")

    if score > 60:
        st.success("✅ Shortlisted")
    elif score > 40:
        st.warning("⚠️ Review Required")
    else:
        st.error("❌ Not Suitable")

    st.subheader("📌 Extracted Skills")
    st.write(", ".join(skills) if skills else "No major skills detected")

    st.subheader("📌 Extracted Entities (NER)")
    st.json(entities)
