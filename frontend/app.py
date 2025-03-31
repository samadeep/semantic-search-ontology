
import streamlit as st
import requests

st.title("🩺 Semantic Symptom Search")

symptom_input = st.text_input("Enter symptoms (comma separated)", "persistent cough, fatigue")
age = st.slider("Patient age", 0, 100, 30)
gender = st.selectbox("Gender", ["all", "male", "female"])

if st.button("Search Conditions"):
    symptoms_list = [s.strip() for s in symptom_input.split(",") if s.strip()]
    params = {"symptoms_query": symptoms_list, "age": age, "gender": gender}
    response = requests.get("http://localhost:8000/query", params=params)
    if response.status_code == 200:
        results = response.json()["results"]
        st.subheader("Possible Conditions")
        for res in results:
            st.write(f"**{res['condition']}** - Score: {res['score']:.2f}")
    else:
        st.error("Failed to fetch results from the backend.")