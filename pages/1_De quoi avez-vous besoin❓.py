# Import libraries
from bokeh.models.widgets import Div
import streamlit as st
import pandas as pd
from io import StringIO
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from streamlit_lottie import st_lottie
import json
import webbrowser

# Function to open a URL
def open_url(url):
    webbrowser.open_new_tab(url)




# Streamlit app
def main():
    st.title("Dites-nous 🎙️")
    st.subheader('Si vous aviez un deuxième cerveau, sur quelle tâche lui demanderiez-vous de travailler ?')

    st.markdown('#')
    st.markdown('#')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button('La collecte de données',on_click=open_url,args=('https://example1.com',),unsafe_allow_html=True)
        link = '[GitHub](http://github.com)'
        st.markdown(link, unsafe_allow_html=True)
        
        st.button('La collecte de données')
        st_lottie("https://assets7.lottiefiles.com/packages/lf20_6tQ2In419R.json", key="col1_lottie", width=200)

    
    with col2:
        button_clicked = st.button("L'écriture")
        if button_clicked:
            open_url("https://example2.com")
        st_lottie("https://assets5.lottiefiles.com/packages/lf20_QdH33DmN0r.json", key="col2_lottie", width=200)
    with col3:
        button_clicked = st.button("Me sentir mieux")
        if button_clicked:
            open_url("https://example3.com")
        st_lottie("https://assets2.lottiefiles.com/packages/lf20_pz5BGiTCej.json", key="col3_lottie")
    with col4:
        button_clicked = st.button("Me superviser")
        if button_clicked:
            open_url("https://example4.com")
        st_lottie("https://assets5.lottiefiles.com/packages/lf20_FAHP63f8vG.json", key="col4_lottie")

    
    next_page = st.button("Suivre Heretica")
    if next_page:
        switch_page("Contact")

if __name__ == "__main__":
    main()
