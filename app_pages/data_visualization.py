import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def data_visualization():
    """Content to fulfil the the first business requirement"""
    st.write("### Leaf Visualizer")
    st.info(f"The client is interested in conducting a study to "
            f"visually differentiates a healthy leaf from a infected leaf")

    version = 'v1'

    selected_items = st.multiselect('Visualize', ['Difference average and variability image',
                                                  'Differences between average parasitised and average healthy leaves',
                                                  'Image Montage'
                                                  ])


    if not selected_items:
        st.write('Please select an item')
    else:
        if 'Difference average and variability image' in selected_items:
            items = ', '.join(selected_items)

            avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
            avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

            st.warning(
                f"* Small differences could be noticed in average and "
                f"variability images. The difference between them is that the "
                f"infected leaves appear more 'cloudy' than the average healthy leaf"
            )

            st.image(avg_powdery_mildew, caption='Infected leaf - Average and Variability')
            st.image(avg_healthy, caption='Healthy leaf - Average and Variability')
            st.write("---")
        if 'Differences between average parasitised and average healthy leaves' in selected_items:
            avg_diff = plt.imread(f"outputs/{version}/avg_diff.png")

            st.warning(
                f"* We notice this study didn't show "
                f"patterns where we could intuitively differentiate one from another.")
            st.image(avg_diff, caption='Difference between average images')

