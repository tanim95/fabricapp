
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk


def generate_fabric_image(epi, ppi, weaving_pattern, yarn_count):
    if yarn_count > 500:
        message = f"Yarn count is too high: {yarn_count}"
        tk_message = tk.Label(window, text=message)
        tk_message.pack()
        return

    fabric_image = np.zeros((ppi, epi, 3), dtype=np.uint8)

    # RGB values based on the weaving pattern and yarn count
    for i in range(ppi):
        for j in range(epi):
            if weaving_pattern[i % len(weaving_pattern)] == '1':
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    fabric_image[i, j] = [255, 0, 0]  # Red color for weave
                else:
                    # Blue color for non-weave
                    fabric_image[i, j] = [0, 0, yarn_count]
            else:
                # White color for non-weave
                fabric_image[i, j] = [255, 255, 255]

    return fabric_image


def show_fabric_image():
    epi = int(entry_epi.get())
    ppi = int(entry_ppi.get())
    weaving_pattern = entry_weaving_pattern.get()
    yarn_count = int(entry_yarn_count.get())

    fabric_image = generate_fabric_image(epi, ppi, weaving_pattern, yarn_count)

    line_width = max(1, int(yarn_count / 100) * 2)  # Adjust line width based on yarn count

    pil_image = Image.fromarray(fabric_image)

    pil_image = pil_image.resize((800, 800))

    zoomed_image = pil_image.resize((600 * line_width, 600 * line_width))

    tk_image = ImageTk.PhotoImage(zoomed_image)

    label_image.configure(image=tk_image)
    label_image.image = tk_image


def create_window():
    global window, label_epi, entry_epi, label_ppi, entry_ppi
    global label_weaving_pattern, entry_weaving_pattern, label_yarn_count
    global entry_yarn_count, generate_button, label_image

    window = tk.Tk()
    window.title("Fabric Pattern Generator")

    label_epi = tk.Label(window, text="EPI (Ends per Inch):")
    label_epi.pack()
    entry_epi = tk.Entry(window)
    entry_epi.pack()

    label_ppi = tk.Label(window, text="PPI (Picks per Inch):")
    label_ppi.pack()
    entry_ppi = tk.Entry(window)
    entry_ppi.pack()

    label_weaving_pattern = tk.Label(
        window, text="Weaving Pattern (0 = non-weave, 1 = weave):")
    label_weaving_pattern.pack()
    entry_weaving_pattern = tk.Entry(window)
    entry_weaving_pattern.pack()

    label_yarn_count = tk.Label(window, text="Yarn Count:")
    label_yarn_count.pack()
    entry_yarn_count = tk.Entry(window)
    entry_yarn_count.pack()

    generate_button = tk.Button(
        window, text="Generate Fabric Pattern", command=generate_fabric_pattern)
    generate_button.pack()

    label_image = tk.Label(window)
    label_image.pack()


def generate_fabric_pattern():
    show_fabric_image()


create_window()
window.mainloop()


