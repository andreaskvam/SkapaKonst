from typing import Text
import streamlit as st
from PIL import Image

import style

st.title('Skapa Konst')

img = st.sidebar.selectbox(
    'Välj bild',
    ('TurningTorso.jpg', 'FamiljenKvam.jpg', 'Stockholm.jpg', 'Tiger.jpg')
)

style_name = st.sidebar.selectbox(
    'Välj stil',
    ('Mosaik', 'Färgstark', 'Modern')
)

st.sidebar.write('Skapad av Andreas Kvam', '[linkedIn](https://linkedin.com/in/andreaskvam)', '[GitHub](https://github.com/andreaskvam)')



model= "saved_models/" + style_name + ".pth"
input_image = "images/content-images/" + img
output_image = "images/output-images/" + style_name + "-" + img

st.write('### Vald bild:')
image = Image.open(input_image)
st.image(image, width=400)

clicked = st.button('Skapa Konst')

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write('### Skapad bild:')
    image = Image.open(output_image)
    st.image(image, width=400)

