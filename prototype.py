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

st.title("⬇ Housing Rental App")

# Reading the data
df = pd.read_csv('clean_data.csv', index_col=0)
df = df.transpose().reset_index()
df = df.rename(columns={"index": "date"})
df.index=pd.DatetimeIndex(df["date"], freq='MS')

#Displaying the dataset on the app
#st.header("Time Series Forecasting Model for our House Rental App")
#st.text("""Creating a visualization to see the relation between smoking and cancer, dental health, obesity and depression""")
st.write("Let's look at raw data in the Pandas Data Frame for our time series forecasting.")
st.write(df)

"""### EDA"""
# Create a Streamlit plot using Matplotlib
#st.pyplot(plt.figure(figsize=(12, 6))) # Set the figure size to your desired size

df['Average'].plot(label='Average', color='black')
df['Studio'].plot(label='Studio', color='orange')
df['1-Bedroom'].plot(label='1-Bedroom')
df['2-Bedroom'].plot(label='2-Bedroom')
df['3-Bedroom'].plot(label='3-Bedroom')
df['4-Bedroom'].plot(label='4-Bedroom')
plt.grid()
plt.xlabel('Date')
  
# adding legend to the curve
plt.legend()

# Show the plot
st.pyplot(plt)

st.write("⬇ The metrics for different models")

image1 = Image.open('metrics.jpg')
st.image(image1)

#Selecting the model type
#img = image_select("Select Model type", ["RMSE.jpg", "MDA.jpg", "MAE.jpg", "MAPE.jpg"])
#st.write(img)


def image_select(prompt, options):
    # Display prompt and options
    selected_option = st.selectbox(prompt, options)

    # Load image
    img = Image.open(selected_option)

    # Display image with interactivity
    if img is not None:
        img_size = st.sidebar.slider("Image Size", 100, 500, 300)
        st.image(img, use_column_width=True, width=img_size)
    else:
        st.warning("Failed to load image")

# Define available image options
options = ["RMSE.jpg", "MDA.jpg", "MAE.jpg", "MAPE.jpg"]

# Call image_select function
image_select("Select Model type", options)

#Selecting the model type
st.write("ETS and ARIMA models")

image2 = Image.open('models.png')
st.image(image2)

image3 = Image.open('models2.jpg')
st.image(image3)

#Forecasting

st.write("Forecasting sample")
image4 = Image.open('forecast.png')
st.image(image4)