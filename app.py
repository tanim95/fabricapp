import streamlit as st
import numpy as np
from PIL import Image

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return [r, g, b]

def generate_fabric_image(screen_width, screen_height, weaving_pattern, epi, ppi, epi_color, ppi_color):
    square_size = 10

    fabric_width = screen_width // square_size
    fabric_height = screen_height // square_size

    fabric_image = np.zeros((fabric_height, fabric_width, 3), dtype=np.uint8)

    for i in range(fabric_width):
        for j in range(fabric_height):
            if weaving_pattern[(i * epi // square_size) % len(weaving_pattern)] == '1':
                if (i * ppi // square_size) % 2 == 0 and (j * ppi // square_size) % 2 == 0:
                    fabric_image[j, i] = epi_color
                else:
                    fabric_image[j, i] = ppi_color
            else:
                fabric_image[j, i] = [0, 0, 0]  # Non weave color

    thickened_fabric_image = np.kron(fabric_image, np.ones(
        (square_size, square_size, 1), dtype=np.uint8))

    image = Image.fromarray(thickened_fabric_image)
    return image, None

def main():
    st.title('Fabric Pattern Generator')

    weaving_pattern = st.text_input('Weaving Pattern')
    epi = st.number_input('Ends Per Inch (EPI)', value=10)
    ppi = st.number_input('Picks Per Inch (PPI)', value=10)
    epi_color = st.color_picker('EPI Color')
    ppi_color = st.color_picker('PPI Color')

    if st.button('Generate Pattern'):
        # screen resolution
        screen_width, screen_height = 800, 600
        image, error = generate_fabric_image(
            screen_width, screen_height, weaving_pattern, epi, ppi, epi_color, ppi_color)

        if error:
            st.error(error)
        else:
            st.image(image, caption='Fabric Pattern', use_column_width=True)

if __name__ == '__main__':
    main()
