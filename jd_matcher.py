from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(jd_text, resume_text):
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(jd_embedding, resume_embedding)
    return float(similarity[0][0]) * 100
