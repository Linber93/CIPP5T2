import streamlit as st
import os
from app_pages.data_visualization import image_montage


def project_hypothesis():
    """Content to summarize the project"""


st.write("## Project Hypothesis and Validation")

st.write("### Hypothesis 1")
st.info(
    f"* We suspect that the Mildew infected plants can be identified "
    f"by white powdery spot on the leaves and stem."
)

my_data_dir = 'inputs/datasets/cherry-leaves/cherry-leaves'
labels = os.listdir(my_data_dir + '/validation')
label_to_display = st.selectbox(label="Select label", options=labels, index=0)
image_montage(dir_path=my_data_dir + '/validation',
              label_to_display=label_to_display,
              nrows=3, ncols=3, figsize=(6, 20))

st.success(
    f"Looking at"
)