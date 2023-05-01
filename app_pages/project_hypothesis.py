import streamlit as st


def project_hypothesis():
    """Content to projects hypothesises"""

    st.write("## Project Hypothesis and Validation")

    st.write("### Hypothesis 1")
    st.info(
        f"* We suspect that the Mildew infected plants can be identified "
        f"by white powdery spot on the leaves and stem."
    )

    st.success(
        f"The image montage in 'Data visualization' we can confirm that "
        f"the infected leaves is easily identifiable by the "
        f"powder white spots on leaves and steam."
    )

    st.write("### Hypothesis 2")
    st.info(
        f"* It can be assumed that a working model could predict if the "
        f"leaf is infected despite being provided with images "
        f"in different orientations."
    )
    st.warning(
        f"I can partially be validated by the model performning well"
        f" after the images being augmented before being fitted."
    )

    st.write("### Hypothesis 3")
    st.info(
        f"We suspect that mildew could also be detected"
        f" on other plants and leaves."
    )
    st.error(
        f"We could NOT validate this hypothesis.\n\n"
        f"When tried predicting mildew on other plants the model"
        f"did wrongly predict mildew.\n\n"
        f"Additionally when the model was provided with and "
        f"image of something "
        f"else but a leaf it tried to make a prediction on that too"
        f"instead of rejecting the input.\n\n"
        f"Further training required to implement such features "
    )
