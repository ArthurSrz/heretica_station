# Import libraries
import streamlit as st
import pandas as pd
from io import StringIO
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from streamlit_lottie import st_lottie
import json
import webbrowser


# Streamlit app
def main():
    st.title("Dites-nous 🎙️")
    st.subheader('Si vous aviez un deuxième cerveau, sur quelle tâche lui demanderiez-vous de travailler ?')

    st.markdown('#')
    st.markdown('#')

    col1, col2, col3, col4 = st.columns(4)
    with col1:

        button_md1 = '''
    <a href="https://www.example.com" class="github-button" aria-label="Open", style="display: inline-block; text-align: center; width: 100%;">Open</a>
    '''
        st.markdown(button_md1, unsafe_allow_html=True)
        st_lottie("https://assets7.lottiefiles.com/packages/lf20_6tQ2In419R.json", key="col1_lottie", width=200)

        button_md = '''[Open External URL](https://www.google.com)'''
        st.markdown(button_md, unsafe_allow_html=True)

        button_md1 = '''
    <a href="https://www.example.com" class="github-button" aria-label="Open">Open</a>
    '''
        st.markdown(button_md1, unsafe_allow_html=True)

    with col2:
        st.button("La collecte de données", key=2)
        st_lottie("https://assets5.lottiefiles.com/packages/lf20_QdH33DmN0r.json", key="col2_lottie", width=200)
    with col3:
        st.button("Me sentir mieux", key=3)
        st_lottie("https://assets2.lottiefiles.com/packages/lf20_pz5BGiTCej.json", key="col3_lottie")
    with col4:
        st.button("Me superviser", key=4)
        st_lottie("https://assets5.lottiefiles.com/packages/lf20_FAHP63f8vG.json", key="col4_lottie")

    
    next_page = st.button("Suivre Heretica")
    if next_page:
        switch_page("Contact")

if __name__ == "__main__":
    main()
