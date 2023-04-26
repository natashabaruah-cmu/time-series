import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from streamlit_image_select import image_select

st.set_page_config(
    page_title="Housing Rental App", page_icon="⬇", layout="centered"
)

#st.title("Housing Rental App")
st.markdown("<h1 style='text-align: center; color: black;'>Housing Rental App</h1>", unsafe_allow_html=True)


#Showing the forecast for time period 1: 2015-2017 testing period
st.markdown("**:blue[Time period 1: Testing from 2015-2017]**")

# Define the list of image paths
image_paths = ['3 bedroom-1.JPG', '4 bedroom-1.JPG']


# Function to load and display the selected image
def display_image(image_path):
    image = Image.open(image_path)
    st.image(image, caption='Selected bedroom type', use_column_width=True)

# Streamlit app
def main():
   
    # Create a selection box for image options
    selected_option = st.selectbox('Select bedroom type', image_paths)

    # Display the selected image
    display_image(selected_option)

if __name__ == '__main__':
    main()

#Showing the forecast for time period 2: 2015-2018 testing period

st.markdown("**:blue[Time period 2: Testing from 2015-2018]**")

# Define the list of image paths
image_paths = ['3 bedroom-2.JPG', '4 bedroom-2.JPG']

# Function to load and display the selected image
def display_image(image_path):
    image = Image.open(image_path)
    st.image(image, caption='Selected bedroom type', use_column_width=True)

# Streamlit app
def main():
    #st.title('Bedroom Selector')
    #st.write('Select a bedroom type from the options below:')

    # Create a selection box for image options
    selected_option = st.selectbox('Select bedroom type', image_paths)

    # Display the selected image
    display_image(selected_option)

if __name__ == '__main__':
    main()




#Showing the forecast for time period 3: 2015-20189 testing period

st.markdown("**:blue[Time period 3: Testing from 2015-2019]**")

# Define the list of image paths
image_paths = ['3 bedroom-3.JPG', '4 bedroom-3.JPG']

# Function to load and display the selected image
def display_image(image_path):
    image = Image.open(image_path)
    st.image(image, caption='Selected bedroom type', use_column_width=True)

# Streamlit app
def main():

    # Create a selection box for image options
    selected_option = st.selectbox('Select bedroom type', image_paths)

    # Display the selected image
    display_image(selected_option)

if __name__ == '__main__':
    main()


#Model Evaluation Visualization 

st.markdown("**:blue[Model Evaluation Visualization : 3 Bedroom]**")
image3 = Image.open('8.JPG')
st.image(image3)


st.markdown("**:blue[Model Evaluation Visualization : 4 Bedroom]**")
image4 = Image.open('9.JPG')
st.image(image4)

#Model Evaluation Metrics-Merged
st.markdown("**:blue[Model Evaluation Metrics-Merged]**")
st.write("Lets look at some of our parameters in selecting th best model.")

image2 = Image.open('7.JPG')
st.image(image2)

st.markdown("**:green[Triple Mul model works best for 3 bedroom and Triple add works best for 4 bedroom.]**")
