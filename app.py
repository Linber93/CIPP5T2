import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.project_summary import project_summary


app = MultiPage(app_name= "Mildew Detector")

app.add_page("Project Summary", project_summary)

app.run()