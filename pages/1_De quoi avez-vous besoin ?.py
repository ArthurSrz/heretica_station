# Import libraries
import streamlit as st
import pandas as pd
from io import StringIO
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.switch_page_button import switch_page


# Streamlit app
def main():
    st.title("De quoi avez-vous besoin ?")
    st.subheader('Si demain vous pouviez avoir un deuxième cerveau, sur quelle tâche lui demanderiez-vous de travailler ?')

    
    next_page = st.button("Suivre Heretica")
    if next_page:
        switch_page("Contact")

if __name__ == "__main__":
    main()
