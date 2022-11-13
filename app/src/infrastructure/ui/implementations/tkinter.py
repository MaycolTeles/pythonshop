"""
Module containing the "Tkinter" Class.
"""

import pathlib

import customtkinter
from PIL import ImageTk
import tkinter
from tkinter import filedialog, Canvas

from src.infrastructure.ui.interfaces import UIInterface
from src.adapters.controllers.implementations import LoadImageController, RotateImageController
from src.adapters.presenters.implementations import ImagePresenter


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


CURRENT_PATH = pathlib.Path().resolve()


class Tkinter(UIInterface, customtkinter.CTk):
    """
    Class to represent a "Tkinter" UserInterface.
    """
    WIDTH = 1200
    HEIGHT = 700

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()

        self.title("PYTHONSHOP")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  

        self._create_frame_main()
        self._create_frame_left()
        self._create_frame_right()
        self._create_frame_info()
        self._set_default()

    def _create_frame_main(self) -> None:
        """"""
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._frame_left = customtkinter.CTkFrame(
            master=self,
            width=180,
            corner_radius=0
        )

        self._frame_left.grid(row=0, column=0, sticky="nswe")

        self._frame_right = customtkinter.CTkFrame(master=self)
        self._frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def _create_frame_left(self) -> None:
        """"""
        # configure grid layout (1x11)
        self._frame_left.grid_rowconfigure(0, minsize=10)    # empty row with minsize as spacing
        self._frame_left.grid_rowconfigure(5, weight=1)      # empty row as spacing
        self._frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self._frame_left.grid_rowconfigure(11, minsize=10)   # empty row with minsize as spacing

        self.lbl_1 = customtkinter.CTkLabel(
            master=self._frame_left,
            text="Options",
            text_font=("Roboto Medium", -16) # font name and size in px
        )
        self.lbl_1.grid(row=1, column=0, pady=10, padx=10)

        self.btn_load_image = customtkinter.CTkButton(
            master=self._frame_left,
            text="Load Image",
            command=self.load_image
        )
        self.btn_load_image.grid(row=2, column=0, pady=10, padx=20)

        self.btn_save_image = customtkinter.CTkButton(
            master=self._frame_left,
            text="Save Image",
            command=self.save_image
        )
        self.btn_save_image.grid(row=3, column=0, pady=10, padx=20)

        self.btn_3 = customtkinter.CTkButton(
            master=self._frame_left,
            text="dsadsafsad",
            command=self.crop_image
        )
        self.btn_3.grid(row=4, column=0, pady=10, padx=20)

        self.lbl_mode = customtkinter.CTkLabel(master=self._frame_left, text="Appearance Mode:")
        self.lbl_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(
            master=self._frame_left,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode
        )
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

    def _create_frame_info(self) -> None:
        """"""
        # configure grid layout (1x1)
        self._frame_info.rowconfigure(0, weight=1)
        self._frame_info.columnconfigure(0, weight=1)

        self._img_canvas = Canvas(self._frame_info, width=600, height=400)
        self._img_canvas.grid()

        self.lbl_image = customtkinter.CTkLabel(
            master=self._frame_info,
            text="IMAGE",
            corner_radius=6,                # <- custom corner radius
            fg_color=("white", "gray38"),   # <- custom tuple-color
            justify=tkinter.CENTER
        )
        self.lbl_image.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

    def _create_frame_right(self) -> None:
        """"""
        """"""
        # configure grid layout (3x7)
        self._frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self._frame_right.rowconfigure(7, weight=10)
        self._frame_right.columnconfigure((0, 1), weight=1)
        self._frame_right.columnconfigure(2, weight=0)

        self._frame_info = customtkinter.CTkFrame(master=self._frame_right)
        self._frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        self.radio_var = tkinter.IntVar(value=0)

        self.lbl_radio_group = customtkinter.CTkLabel(
            master=self._frame_right,
            text="CTkRadioButton Group:"
        )
        self.lbl_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_btn_1 = customtkinter.CTkRadioButton(
            master=self._frame_right,
            variable=self.radio_var,
            value=0
        )
        self.radio_btn_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_btn_2 = customtkinter.CTkRadioButton(
            master=self._frame_right,
            variable=self.radio_var,
            value=1
        )
        self.radio_btn_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.radio_btn_3 = customtkinter.CTkRadioButton(
            master=self._frame_right,
            variable=self.radio_var,
            value=2
        )
        self.radio_btn_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.slider_1 = customtkinter.CTkSlider(
            master=self._frame_right,
            from_=0,
            to=1,
            number_of_steps=3,
            command=self.btn_event
        )
        self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_2 = customtkinter.CTkSlider(
            master=self._frame_right,
            command=self.btn_event
        )
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.switch_1 = customtkinter.CTkSwitch(
            master=self._frame_right,
            text="CTkSwitch"
        )
        self.switch_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.switch_2 = customtkinter.CTkSwitch(
            master=self._frame_right,
            text="CTkSwitch"
        )
        self.switch_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_1 = customtkinter.CTkComboBox(
            master=self._frame_right,
            values=["Value 1", "Value 2"]
        )
        self.combobox_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.check_box_1 = customtkinter.CTkCheckBox(
            master=self._frame_right,
            text="CTkCheckBox"
        )
        self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = customtkinter.CTkCheckBox(
            master=self._frame_right,
            text="CTkCheckBox"
        )
        self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.entry = customtkinter.CTkEntry(
            master=self._frame_right,
            width=120,
            placeholder_text="CTkEntry"
        )
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.btn_5 = customtkinter.CTkButton(
            master=self._frame_right,
            text="CTkButton",
            border_width=2,  # <- custom border_width
            fg_color=None,  # <- no fg_color
            command=self.btn_event
        )
        self.btn_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

    def _set_default(self) -> None:
        """"""
        self.optionmenu_1.set("Dark")
        self.btn_3.configure(state="disabled", text="Disabled CTkButton")
        self.combobox_1.set("CTkCombobox")
        self.radio_btn_1.select()
        self.slider_1.set(0.2)
        self.slider_2.set(0.7)
        self.switch_2.select()
        self.radio_btn_3.configure(state=tkinter.DISABLED)
        self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        self.check_box_2.select()

    def btn_event(self):
        print("Button pressed")

    def execute(self) -> None:
        """
        Method to execute the user interface.
        """
        self.mainloop()

    def load_image(self) -> None:
        """
        Method to load the image.
        """
        filetypes = (
            ("images", ["*.png", "*.jpg", "*.jpeg", "*.gif", "*.svg"]),
        )

        image_name = filedialog.askopenfilename(
            title="Open Image",
            initialdir=CURRENT_PATH,
            filetypes=filetypes
        )

        image_data = {
            "image_path": image_name
        }

        controller = LoadImageController()
        controller.execute(image_data)

    def show_image(self, image_data: ImagePresenter) -> None:
        """"""
        image = image_data.image
        tk_image = ImageTk.PhotoImage(image)

        self.lbl_image = customtkinter.CTkLabel(
            master=self._frame_info,
            image=tk_image,
            justify=tkinter.CENTER
        )
        self.lbl_image.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

    def save_image(self) -> None:
        """
        Method to save the image.
        """
        image_name = filedialog.asksaveasfilename(
            title="Save Image",
            initialdir=CURRENT_PATH
        )

        image_data = {
            "image_name": image_name
        }

        controller = SaveImageController()
        controller.execute(image_data)

    def crop_image(self) -> None:
        """
        Method to crop the image.
        """
        # TODO: IMPLEMENT
        print('TODO: IMPLEMENT')

    def rotate_image(self) -> None:
        """
        Method to rotate the image.
        """
        image_data = {
            "rotate_angle": 30
        }

        controller = RotateImageController()
        controller.execute(image_data)

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event: int=0):
        """"""
        self.destroy()
