from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import font as tkFont
import numpy as np
import distribution_window
import inverse_transform_sampling
import linear_transformation_window
import pca_window
import monte_carlo_window
import image_compression_window
import svd_window
import matched_filter_window
import mixer_matrix_multiplication


root = Tk()
root.title("Math Visualizer")
root.geometry("1920x1080")
root.configure(bg='ghost white')

# frame = LabelFrame(root, text="This is frame", padx=50, pady=50)
# frame.grid(row=0, column=800, padx=10, pady=10)

heading = Label(root, text="MATH VISUALISER & STATE MACHINE SIMULATOR", bg="ghost white", padx=10, pady=10, font=("Helvetica", 18))
heading.grid(row=0, column=4)

about = Label(root, text="ABOUT", padx=10, pady=5, bg='ghost white', font=("Helvetica", 12)).grid(row=1, column=0)
exit = Button(root, text="EXIT", command=root.quit, padx=10, pady=10).grid(row=1, column=8)

# description = Label(root, text="This is a software that visulises mathematical concepts and helps you understand them better", padx=20, pady=10).grid(row=2, column=1)

#drop-down menu
def visualize(event):

    global dist_var

    if menu.get() == "Monte Carlo":
        monte_obj = monte_carlo_window.Monte_Window()

    if menu.get() == "Uniform Distribution":
        dist_var = 1
        uniform_obj = distribution_window.Dist_Window(dist_var)

    if menu.get() == "Exponential Distribution":
        dist_var = 2
        exp_object = distribution_window.Dist_Window(dist_var)

    if menu.get() == "Linear Transformation":
        linear_obj = linear_transformation_window.Linear_Transform_Window()

    if menu.get() == "Inverse Transform Sampling":
        sampling_obj = inverse_transform_sampling.ITS()
        sampling_obj.start()

    if menu.get() == "Principal Component Analysis":
        pca_object = pca_window.PCA_Window()

    if menu.get() == "Image Compression":
        image_obj = image_compression_window.Image_Compression_Window()

    if menu.get() == "Singular Value Decomposition":
        svd_obj = svd_window.SVD_Window()

    if menu.get() == "Matched Filter":
        filter_object = matched_filter_window.Matched_Filter_Window()

    if menu.get() == "Mixer - Matrix Multiplication":
        mixer_obj = mixer_matrix_multiplication.Mixer()


options = [
    "Monte Carlo",
    "Uniform Distribution",
    "Exponential Distribution",
    "Linear Transformation",
    "Inverse Transform Sampling",
    "Principal Component Analysis",
    "Image Compression",
    "Singular Value Decomposition",
    "Matched Filter",
    "Mixer - Matrix Multiplication"
    ]

menu = StringVar()
menu.set("SELECT")

# combo = ttk.Combobox(root, value=options)
# combo.current(0)
# combo.bind("<<ComboboxSelected>>", combofunction)
# combo.grid(row=2, column=0, padx=20, pady=50)

drop = OptionMenu(root, menu, *options, command=visualize)

drop_font = tkFont.Font(family="Helvetica", size=11) #to define the font
drop.config(font=drop_font) #to change the font of 'select'

drop_menu_font = root.nametowidget(drop.menuname) #to change the font of drop down options
drop_menu_font.config(font=drop_font)
drop.grid(row=2, column=0, padx=20, pady=50, columnspan=2)


#imageviewer  #550*350
img1 = Image.open("images/uniform_dist.png")
img1 = img1.resize((720, 480))
img1 = ImageTk.PhotoImage(img1)
img2 = Image.open("images/exp_dist.png")
img2 = img2.resize((720, 480))
img2 = ImageTk.PhotoImage(img2)
img3 = Image.open("images/monte-carlo.png")
img3 = img3.resize((720, 480))
img3 = ImageTk.PhotoImage(img3)
img4 = Image.open("images/image_compression.png")
img4 = img4.resize((720, 480))
img4 = ImageTk.PhotoImage(img4)
img5 = Image.open("images/svd.png")
img5 = img5.resize((720, 480))
img5 = ImageTk.PhotoImage(img5)

image_name = ["Uniform Distribution", "Exponential Distribution"]
image_list = [img1, img2, img3, img4, img5]

image_label = Label(image=img1, padx=20, pady=10)
image_label.grid(row=3, column=3, columnspan=4, padx=30)

def forward(img_number):
    global image_label
    global back_button
    global forward_button

    image_label.grid_forget()
    image_label = Label(image=image_list[img_number])
    forward_button = Button(root, text=">>", command=lambda: forward(img_number+1), width=5)
    back_button = Button(root, text="<<", command=lambda: backward(img_number-1), width=5)

    if img_number == 4:
        forward_button = Button(root, text=">>", state=DISABLED, width=5)

    forward_button.grid(row=4, column=7)
    back_button.grid(row=4, column=2)
    image_label.grid(row=3, column=3, columnspan=4, padx=30)


def backward(img_number):
    global image_label
    global back_button
    global forward_button

    image_label.grid_forget()
    image_label = Label(image=image_list[img_number])
    forward_button = Button(root, text=">>", command=lambda: forward(img_number+1), width=5)
    back_button = Button(root, text="<<", command=lambda: backward(img_number-1), width=5)

    if img_number == 0:
        back_button = Button(root, text=">>", state=DISABLED, width=5)
    forward_button.grid(row=4, column=7)
    back_button.grid(row=4, column=2)
    image_label.grid(row=3, column=3, columnspan=4, padx=30)


back_button = Button(root, text="<<", width=5)
forward_button = Button(root, text=">>", command=lambda: forward(1), width=5)

back_button.grid(row=4, column=2)
forward_button.grid(row=4, column=7)


root.mainloop()
