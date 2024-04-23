import streamlit as st
import cv2
import numpy as np
import joblib
from io import BytesIO

model = joblib.load('model.pkl')

def preprocess_image(image):
    resized_image = cv2.resize(image, (50, 50))
    new_image = np.expand_dims(resized_image, axis=0)
    return new_image

def is_valid_image(image):
    # Check if the image contains only two unique values (black and white)
    unique_values = np.unique(image)
    if len(unique_values) != 2:
        return False
    return True

def main():
    st.title('White Spot Predictor')
    st.text('Upload an image to predict the coordinates of the white spot.')

    # Upload image
    uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'png'])

    if uploaded_file is not None:
        # Convert BytesIO object to byte array
        file_bytes = uploaded_file.getvalue()

        try:
            # Decode byte array to image
            image = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_GRAYSCALE)
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Check if the uploaded image is valid
            if not is_valid_image(image):
                st.error("Invalid image! Please upload an image with a black background and one white spot.")
                return

            # Preprocess the image
            preprocessed_image = preprocess_image(image)

            # Make prediction
            predicted_coords = model.predict(preprocessed_image).astype('int')

            # Display prediction
            st.write(f'Predicted Coordinates: {predicted_coords}')

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
