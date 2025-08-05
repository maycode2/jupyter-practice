import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('mnist_model.h5')
    return model

model = load_model()

# Title
st.title("MNIST Digit Classifier")

# File uploader
uploaded_file = st.file_uploader("Upload an image of a digit (28x28 grayscale)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')  # Convert to grayscale
    image = ImageOps.invert(image)  # Invert colors (white digit on black background)
    image = image.resize((28, 28))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    st.image(image, caption='Processed Image', width=150)
    
    prediction = model.predict(img_array)
    digit = np.argmax(prediction)

    st.subheader(f"Predicted Digit: {digit}")
model.save('mnist_model.h5')
