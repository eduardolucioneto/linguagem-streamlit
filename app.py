import streamlit as st
from streamlit_ace import st_ace, THEMES, LANGUAGES

st.title('Nosso editor de texto!')

c1, c2 = st.columns([3, 1])

with c1:
    content = st_ace(
        theme=c2.selectbox('Tema',options=THEMES),
        language=c2.selectbox('Linguagem',options=LANGUAGES, index=121),
        font_size=c2.slider('Tam. Fonte', 20),
        min_lines=30
    )    

    content
