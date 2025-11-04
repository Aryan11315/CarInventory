# streamlit_app.py

import streamlit as st
import random
from abc import ABC, abstractmethod

# === Class Definitions ===

class Honda(ABC):
    def contract(self, contract):
        self.contract = contract

    def termsandcondition(self, termsandcondition):
        self.termsandcondition = termsandcondition

    @abstractmethod
    def features(self, specdict):
        pass

class Civic2004(Honda):
    def features(self, civic2004dict):
        self.featuresdict = civic2004dict
        return self.featuresdict

class Civic2008(Civic2004):
    def features(self, civic2008dict):
        self.featuresdict = civic2008dict
        return self.featuresdict

# === Streamlit UI ===

st.title("Honda Civic Models Viewer")

# Generate unique model numbers
unique_ids = set()
while len(unique_ids) < 3:
    unique_ids.add(random.randint(10000000, 99999999))
unique_ids = list(unique_ids)

# Predefined data for both models
civic_2004_data = {
    "ModelName": "Civic2004",
    "Price": "$15000",
    "ModelNumber": unique_ids[0]
}

civic_2008_data = {
    "ModelName": "Civic2008",
    "Price": "$20000",
    "ModelNumber": unique_ids[1]
}

# Model selection
model_choice = st.selectbox("Select Civic Model", ["Civic2004", "Civic2008"])

if st.button("Show Features"):
    if model_choice == "Civic2004":
        civic1 = Civic2004()
        features = civic1.features(civic_2004_data)
    elif model_choice == "Civic2008":
        civic2 = Civic2008()
        features = civic2.features(civic_2008_data)

    st.subheader(f"{model_choice} Features")
    for key, value in features.items():
        st.write(f"**{key}**: {value}")
