# Import libraries
import streamlit as st
import pandas as pd
from io import StringIO
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.switch_page_button import switch_page


#function to display buttons
def display_button_gallery(buttons, items_per_row=4):
    num_items = len(buttons)
    num_rows = (num_items - 1) // items_per_row + 1

    for row in range(num_rows):
        cols = st.columns(items_per_row)
        start_index = row * items_per_row
        end_index = min(start_index + items_per_row, num_items)

        for col, index in zip(cols, range(start_index, end_index)):
            button = buttons[index]
            col.button(button)
            

# Streamlit app
def main():
    st.title("De quoi avez-vous besoin ?")
    st.subheader('Si vous aviez un deuxième cerveau, sur quelle tâche lui demanderiez-vous de travailler ?')

    
    # Display
    button_labels = ['Button 1', 'Button 2', 'Button 3', 'Button 4', 'Button 5', 'Button 6', 'Button 7', 'Button 8']
    display_button_gallery(button_labels)
    
    next_page = st.button("Suivre Heretica")
    if next_page:
        switch_page("Contact")

if __name__ == "__main__":
    main()
