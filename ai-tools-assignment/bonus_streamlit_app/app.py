import streamlit as st

st.title("MNIST Handwritten Digit Classifier")

uploaded_file = st.file_uploader("Upload an image of a digit", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Digit", use_column_width=True)
    st.write("Classifying...")
    # Placeholder for prediction logic
