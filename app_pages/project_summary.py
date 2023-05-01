import streamlit as st


def project_summary():
    """Content to summarize the project"""
    st.write("## Project Summary")

    st.info(
        f"### **General information**\n\n"
        f"Powdery mildew is a fungal disease tha affects a "
        f"wide range of plants.\n\n"
        f"Powdery mildew is one of the easier plant diseases to identify, "
        f"as its symptoms are quite distinctive. Infected plants display "
        f"white powdery spots on the leaves and stems."
        )

    st.info(
        f"### **Project information**\n\n"
        f"The cherry plantation crop from Farmy & Foods is facing a "
        f"challenge where their cherry plantations have been presenting "
        f"powdery mildew. Currently, the process is manual verification "
        f"if a given cherry tree contains powdery mildew. "
        f"An employee spends around 30 minutes in each tree, taking a "
        f"few samples of tree leaves and verifying visually if "
        f"the leaf tree is healthy or has powdery mildew."
        f" If there is powdery mildew, the employee applies a specific "
        f"compound to kill the fungus. The time spent applying "
        f"this compound is 1 minute.\n\n The company has thousands of"
        f" cherry trees, located on multiple farms across the country."
        f" As a result, this manual process is not scalable due to "
        f"the time spent in the manual process inspection.\n\n"
        f"To save time in this process, the IT team suggested "
        f"an ML system that detects instantly, using a leaf "
        f"tree image, if it is healthy or has powdery mildew."
        f" A similar manual process is in place for other crops for "
        f"detecting pests, and if this initiative is successful, "
        f"there is a realistic chance to replicate "
        f"this project for all other crops. "
    )

    st.info(
        f"### **Business requirement**\n\n"
        f"The Client has provided us with 2 requirements to fulfil "
        f"during this project\n\n"
        f"The client is interested in:\n\n"
        f"1 - conducting a study to visually differentiate a healthy "
        f"cherry leaf from one with powdery mildew.\n\n"
        f"2 - predicting if a cherry leaf is healthy or "
        f"contains powdery mildew."
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Linber93/CIPP5T2/blob/main/README.md)."
    )
