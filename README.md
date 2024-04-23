# White Dot Detection Project
This project helps you predict the coordinates of white dots in images with black backgrounds. It uses a custom Convolutional Neural Network (CNN) trained specifically for this purpose.

# Environment Variables
The .env file contains the following configuration options:
1. CSV_FILENAME: The name of the CSV file where the predicted coordinates will be saved.
2. LOCATION: The directory where the images with white dots are located.
3. num_images: The number of images you want to generate for the dataset
4. model_name: The name of the trained model

# How to Train Your Model
If you want to train your own model, follow these steps:
1. Update Environment Variables: Modify the .env file to specify the training parameters and dataset paths.
2. Prepare Training Data: Create a dataset of images with black backgrounds and one white dot in each image.
3. Run Training Script: Run the training script to train the model using your dataset.

# Using a Pre-trained Model
If you prefer to use a pre-trained model, you can simply run the Streamlit app:

```python
streamlit run app.py
```

This will deploy the pre-trained model, allowing you to upload images and get predictions for the coordinates of white dots.



# Requirements
Make sure you have the necessary Python packages installed. You can install them using pip by running pip install -r requirements.txt.
