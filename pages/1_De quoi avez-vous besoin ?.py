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
            col.write(st_lottie(url=animation_url, width=200))

# Streamlit app
def main():
    st.title("De quoi avez-vous besoin ?")
    st.subheader('Si vous aviez un deuxième cerveau, sur quelle tâche lui demanderiez-vous de travailler ?')

    
    # Example usage
    button_labels = ['Button 1', 'Button 2', 'Button 3', 'Button 4']
    animation_urls = [
        "https://assets8.lottiefiles.com/datafiles/qDp9b8XrbOYBk48/data.json",
        "https://assets8.lottiefiles.com/datafiles/MuGgH9MvRcneO2j/data.json",
        "https://assets8.lottiefiles.com/packages/lf20_YjJewb.json",
        "https://assets8.lottiefiles.com/packages/lf20_HrCvuL.json"]
    
    display_button_gallery(button_labels, animation_urls)
    
    next_page = st.button("Suivre Heretica")
    if next_page:
        switch_page("Contact")

if __name__ == "__main__":
    main()
