# Import libraries
import streamlit as st
import pandas as pd
from io import StringIO
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from streamlit_lottie import st_lottie
import json

# Function to display the gallery
def display_button_gallery(buttons, animation_urls, items_per_row=4):
    num_items = len(buttons)
    num_rows = (num_items - 1) // items_per_row + 1

    for row in range(num_rows):
        cols = st.columns(items_per_row)
        start_index = row * items_per_row
        end_index = min(start_index + items_per_row, num_items)

        for col, index in zip(cols, range(start_index, end_index)):
            button = buttons[index]
            animation_url = animation_urls[index]
            col.button(button)
            st_lottie(animation_url, width=200)

# Streamlit app
def main():
    st.title("De quoi avez-vous besoin ?")
    st.subheader('Si vous aviez un deuxième cerveau, sur quelle tâche lui demanderiez-vous de travailler ?')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("La collecte de données")
        st_lottie("https://assets7.lottiefiles.com/packages/lf20_6tQ2In419R.json", width=200)
    with col2:
        st.button("L'écriture")
        st_lottie("https://assets5.lottiefiles.com/packages/lf20_QdH33DmN0r.json", width=200)
    with col3:
        st.button("Me sentir mieux")
        st_lottie("https://assets2.lottiefiles.com/packages/lf20_pz5BGiTCej.json")
    with col4:
        st.button("Me superviser")
        st_lottie("https://assets5.lottiefiles.com/packages/lf20_FAHP63f8vG.json")


    
    # Example usage
    button_labels = ["La collecte de données", "L'écriture", "Me sentir mieux", "Me superviser"]
    animation_urls = [
        "https://assets7.lottiefiles.com/packages/lf20_6tQ2In419R.json",
        "https://assets5.lottiefiles.com/packages/lf20_QdH33DmN0r.json",
        "https://assets2.lottiefiles.com/packages/lf20_pz5BGiTCej.json",
        "https://assets5.lottiefiles.com/packages/lf20_FAHP63f8vG.json"]
    
    display_button_gallery(button_labels, animation_urls)
    
    next_page = st.button("Suivre Heretica")
    if next_page:
        switch_page("Contact")

if __name__ == "__main__":
    main()
