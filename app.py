import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.project_summary import project_summary
from app_pages.project_hypothesis import project_hypothesis
from app_pages.data_visualization import data_visualization
from app_pages.mildew_detector import mildew_detector
from app_pages.ml_performance import ml_performance


app = MultiPage(app_name="Mildew Detector")

app.add_page("Project Summary", project_summary)
app.add_page("Project Hypothesis", project_hypothesis)
app.add_page("Data Visualization", data_visualization)
app.add_page("Mildew Detector", mildew_detector)
app.add_page("Ml Performance", ml_performance)


app.run()
