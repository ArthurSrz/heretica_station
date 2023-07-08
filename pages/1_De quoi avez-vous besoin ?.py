# Import libraries
import streamlit as st
import pandas as pd
from io import StringIO
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from streamlit_lottie import st_lottie
import json

# Streamlit app
def main():
    st.title("De quoi avez-vous besoin ?")
    st.subheader('Si vous aviez un deuxième cerveau, sur quelle tâche lui demanderiez-vous de travailler ?')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.empty()
        st.button("La collecte de données")
        st_lottie("https://assets7.lottiefiles.com/packages/lf20_6tQ2In419R.json", width=200)
        st.empty()
    with col2:
        st.empty()
        st.button("L'écriture")
        st_lottie("https://assets5.lottiefiles.com/packages/lf20_QdH33DmN0r.json", width=200)
        st.empty()
    with col3:
        st.empty()
        st.button("Me sentir mieux")
        st_lottie("https://assets2.lottiefiles.com/packages/lf20_pz5BGiTCej.json")
        st.empty()
    with col4:
        st.empty()
        st.button("Me superviser")
        st_lottie("https://assets5.lottiefiles.com/packages/lf20_FAHP63f8vG.json")
        st.empty()

    
    next_page = st.button("Suivre Heretica")
    if next_page:
        switch_page("Contact")

if __name__ == "__main__":
    main()
