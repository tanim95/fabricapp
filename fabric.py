# import numpy as np
# import matplotlib.pyplot as plt
# from tkinter import Tk, Label, Entry, Button


# def generate_fabric_image(epi, ppi, weaving_pattern):
#     # Create the fabric pattern image
#     fabric_image = np.zeros((ppi, epi, 3))

#     # Set the RGB values based on the weaving pattern
#     for i in range(ppi):
#         for j in range(epi):
#             if weaving_pattern[i % len(weaving_pattern)] == '1':
#                 if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
#                     fabric_image[i, j] = [255, 0, 0]  # Red color for weave
#                 else:
#                     # White color for non-weave
#                     fabric_image[i, j] = [255, 255, 255]
#             else:
#                 # White color for non-weave
#                 fabric_image[i, j] = [255, 255, 255]

#     return fabric_image


# def show_fabric_image(fabric_image):
#     # Display the fabric pattern image
#     plt.imshow(fabric_image)
#     plt.axis('off')
#     plt.show()


# def generate_fabric_pattern():
#     # Get fabric parameters from user input
#     epi = int(entry_epi.get())
#     ppi = int(entry_ppi.get())
#     weaving_pattern = entry_weaving_pattern.get()

#     # Generate the fabric image
#     fabric_image = generate_fabric_image(epi, ppi, weaving_pattern)

#     # Display the fabric image
#     show_fabric_image(fabric_image)


# # Create the main window
# window = Tk()
# window.title("Fabric Pattern Generator")

# # Create labels and entry fields for fabric parameters
# label_epi = Label(window, text="EPI (Ends per Inch):")
# label_epi.pack()
# entry_epi = Entry(window)
# entry_epi.pack()

# label_ppi = Label(window, text="PPI (Picks per Inch):")
# label_ppi.pack()
# entry_ppi = Entry(window)
# entry_ppi.pack()

# label_weaving_pattern = Label(
#     window, text="Weaving Pattern (0 = non-weave, 1 = weave):")
# label_weaving_pattern.pack()
# entry_weaving_pattern = Entry(window)
# entry_weaving_pattern.pack()

# # Create a button to generate the fabric pattern
# generate_button = Button(
#     window, text="Generate Fabric Pattern", command=generate_fabric_pattern)
# generate_button.pack()

# # Run the main window loop
# window.mainloop()


# ////////////////////////////////////////////////////////////////////////////////
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from tkinter import Tk, Label, Entry, Button
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# def generate_fabric_image(epi, ppi, weaving_pattern):
#     # Create the fabric pattern image
#     fabric_image = np.zeros((ppi, epi, 3))

#     # Set the RGB values based on the weaving pattern
#     for i in range(ppi):
#         for j in range(epi):
#             if weaving_pattern[i % len(weaving_pattern)] == '1':
#                 if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
#                     fabric_image[i, j] = [255, 0, 0]  # Red color for weave
#                 else:
#                     # White color for non-weave
#                     fabric_image[i, j] = [255, 255, 255]
#             else:
#                 # White color for non-weave
#                 fabric_image[i, j] = [255, 255, 255]

#     return fabric_image


# def show_fabric_image(epi, ppi, weaving_pattern):
#     # Generate the fabric image
#     fabric_image = generate_fabric_image(epi, ppi, weaving_pattern)

#     # Clear the previous image on the canvas
#     canvas.get_tk_widget().delete("all")

#     # Display the fabric pattern image on the canvas
#     img = plt.imshow(fabric_image)
#     plt.axis('off')
#     canvas.draw()


# def generate_fabric_pattern():
#     # Get fabric parameters from user input
#     epi = int(entry_epi.get())
#     ppi = int(entry_ppi.get())
#     weaving_pattern = entry_weaving_pattern.get()

#     # Show the fabric pattern image
#     show_fabric_image(epi, ppi, weaving_pattern)


# # Create the main window
# window = Tk()
# window.title("Fabric Pattern Generator")

# # Create labels and entry fields for fabric parameters
# label_epi = Label(window, text="EPI (Ends per Inch):")
# label_epi.pack()
# entry_epi = Entry(window)
# entry_epi.pack()

# label_ppi = Label(window, text="PPI (Picks per Inch):")
# label_ppi.pack()
# entry_ppi = Entry(window)
# entry_ppi.pack()

# label_weaving_pattern = Label(
#     window, text="Weaving Pattern (0 = non-weave, 1 = weave):")
# label_weaving_pattern.pack()
# entry_weaving_pattern = Entry(window)
# entry_weaving_pattern.pack()

# # Create a button to generate the fabric pattern
# generate_button = Button(
#     window, text="Generate Fabric Pattern", command=generate_fabric_pattern)
# generate_button.pack()

# # Create a Matplotlib figure and embed it in a Tkinter canvas
# figure = plt.figure(figsize=(6, 6))
# canvas = FigureCanvasTkAgg(figure, master=window)
# canvas.get_tk_widget().pack()

# # Add a toolbar to the canvas for zooming functionality
# toolbar = NavigationToolbar2Tk(canvas, window)
# toolbar.update()
# canvas.get_tk_widget().pack()

# # Run the main window loop
# window.mainloop()
# ////////////////////////////////////////////////////////////////////////

# import numpy as np
# from PIL import Image, ImageTk
# import tkinter as tk


# def generate_fabric_image(epi, ppi, weaving_pattern):
#     # Create the fabric pattern image
#     fabric_image = np.zeros((ppi, epi, 3), dtype=np.uint8)

#     # Set the RGB values based on the weaving pattern
#     for i in range(ppi):
#         for j in range(epi):
#             if weaving_pattern[i % len(weaving_pattern)] == '1':
#                 if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
#                     fabric_image[i, j] = [255, 0, 0]  # Red color for weave
#                 else:
#                     # White color for non-weave
#                     fabric_image[i, j] = [255, 255, 255]
#             else:
#                 # White color for non-weave
#                 fabric_image[i, j] = [255, 255, 255]

#     return fabric_image


# def show_fabric_image():
#     # Get fabric parameters from user input
#     epi = int(entry_epi.get())
#     ppi = int(entry_ppi.get())
#     weaving_pattern = entry_weaving_pattern.get()

#     # Generate the fabric image
#     fabric_image = generate_fabric_image(epi, ppi, weaving_pattern)

#     # Convert the fabric image to PIL format
#     pil_image = Image.fromarray(fabric_image)

#     # Resize the image to fit the display
#     pil_image = pil_image.resize((400, 400))

#     # Convert PIL image to Tkinter-compatible format
#     tk_image = ImageTk.PhotoImage(pil_image)

#     # Update the image on the label
#     label_image.configure(image=tk_image)
#     label_image.image = tk_image


# def generate_fabric_pattern():
#     show_fabric_image()


# # Create the main window
# window = tk.Tk()
# window.title("Fabric Pattern Generator")

# # Create labels and entry fields for fabric parameters
# label_epi = tk.Label(window, text="EPI (Ends per Inch):")
# label_epi.pack()
# entry_epi = tk.Entry(window)
# entry_epi.pack()

# label_ppi = tk.Label(window, text="PPI (Picks per Inch):")
# label_ppi.pack()
# entry_ppi = tk.Entry(window)
# entry_ppi.pack()

# label_weaving_pattern = tk.Label(
#     window, text="Weaving Pattern (0 = non-weave, 1 = weave):")
# label_weaving_pattern.pack()
# entry_weaving_pattern = tk.Entry(window)
# entry_weaving_pattern.pack()

# # Create a button to generate the fabric pattern
# generate_button = tk.Button(
#     window, text="Generate Fabric Pattern", command=generate_fabric_pattern)
# generate_button.pack()

# # Create a label to display the fabric image
# label_image = tk.Label(window)
# label_image.pack()

# # Run the main window loop
# window.mainloop()

# /////////////////////////

# import numpy as np
# from PIL import Image, ImageTk
# import tkinter as tk


# def generate_fabric_image(epi, ppi, weaving_pattern, yarn_count):
#     # Create the fabric pattern image
#     fabric_image = np.zeros((ppi, epi, 3), dtype=np.uint8)

#     # Set the RGB values based on the weaving pattern and yarn count
#     for i in range(ppi):
#         for j in range(epi):
#             if weaving_pattern[i % len(weaving_pattern)] == '1':
#                 if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
#                     fabric_image[i, j] = [255, 0, 0]  # Red color for weave
#                 else:
#                     # Blue color for non-weave
#                     fabric_image[i, j] = [0, 0, yarn_count]
#             else:
#                 # White color for non-weave
#                 fabric_image[i, j] = [255, 255, 255]

#     return fabric_image


# def show_fabric_image():
#     # Get fabric parameters from user input
#     epi = int(entry_epi.get())
#     ppi = int(entry_ppi.get())
#     weaving_pattern = entry_weaving_pattern.get()
#     yarn_count = int(entry_yarn_count.get())

#     # Generate the fabric image
#     fabric_image = generate_fabric_image(epi, ppi, weaving_pattern, yarn_count)

#     # Convert the fabric image to PIL format
#     pil_image = Image.fromarray(fabric_image)

#     # Resize the image to fit the display
#     pil_image = pil_image.resize((400, 400))

#     # Convert PIL image to Tkinter-compatible format
#     tk_image = ImageTk.PhotoImage(pil_image)

#     # Update the image on the label
#     label_image.configure(image=tk_image)
#     label_image.image = tk_image


# def generate_fabric_pattern():
#     show_fabric_image()


# # Create the main window
# window = tk.Tk()
# window.title("Fabric Pattern Generator")

# # Create labels and entry fields for fabric parameters
# label_epi = tk.Label(window, text="EPI (Ends per Inch):")
# label_epi.pack()
# entry_epi = tk.Entry(window)
# entry_epi.pack()

# label_ppi = tk.Label(window, text="PPI (Picks per Inch):")
# label_ppi.pack()
# entry_ppi = tk.Entry(window)
# entry_ppi.pack()

# label_weaving_pattern = tk.Label(
#     window, text="Weaving Pattern (0 = non-weave, 1 = weave):")
# label_weaving_pattern.pack()
# entry_weaving_pattern = tk.Entry(window)
# entry_weaving_pattern.pack()

# label_yarn_count = tk.Label(window, text="Yarn Count:")
# label_yarn_count.pack()
# entry_yarn_count = tk.Entry(window)
# entry_yarn_count.pack()

# # Create a button to generate the fabric pattern
# generate_button = tk.Button(
#     window, text="Generate Fabric Pattern", command=generate_fabric_pattern)
# generate_button.pack()

# # Create a label to display the fabric image
# label_image = tk.Label(window)
# label_image.pack()

# # Run the main window loop
# window.mainloop()

# /////////////////////////////////////////////


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

    # Set the RGB values based on the weaving pattern and yarn count
    for i in range(ppi):
        for j in range(epi):
            if weaving_pattern[i % len(weaving_pattern)] == '1':
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    fabric_image[i, j] = [0, 255, 0]  # Red color for weave
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

    line_width = max(1, int(yarn_count / 100))

    pil_image = Image.fromarray(fabric_image)

    pil_image = pil_image.resize((800, 800))

    zoomed_image = pil_image.resize((600 * line_width, 600 * line_width))

    tk_image = ImageTk.PhotoImage(zoomed_image)

    label_image.configure(image=tk_image)
    label_image.image = tk_image


def generate_fabric_pattern():
    show_fabric_image()


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


window.mainloop()
