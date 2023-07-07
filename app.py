import streamlit as st 
from streamlit_player import st_player
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo
from streamlit_lottie import st_lottie


# Streamlit app
def main():
    #set title of the app
    st.title("Heretica basecamp")
    #add a subheader
    st.subheader('Equipez-vous pour l\'ascension de vos recherches')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st_lottie("https://assets3.lottiefiles.com/packages/lf20_eeTaAMa5ER.json", height = 250)
    with col2:
        st_lottie("https://assets3.lottiefiles.com/packages/lf20_dfJkYwImTB.json", height = 250)
    with col3:
        st_lottie("https://assets3.lottiefiles.com/packages/lf20_dfJkYwImTB.json", height=250)

    
    #add a logo
    add_logo("gallery/heretica.png", height=20)
  
    
    next_page = st.button("Begin 🍾 ! ")
    if next_page:
        switch_page("Let's go ⏯️ !")

if __name__ == "__main__":
    main()
