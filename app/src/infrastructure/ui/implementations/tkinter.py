"""
Module containing the "Tkinter" Class.
"""

import pathlib

import customtkinter
from PIL import ImageTk
import tkinter
from tkinter import RIDGE, filedialog, Canvas

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

    def execute(self) -> None:
        """"""
        self._create_interface()
        self.mainloop()

    def _create_interface(self) -> None:
        """"""
        self._setup()
        self._main_frame_setup()
        self._create_frames()
        self._set_default_configs()

    def _setup(self) -> None:
        """"""
        self.title("PYTHONSHOP")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _create_frames(self) -> None:
        """"""
        self._create_options_frame()
        self._create_image_frame()
        self._create_tools_frame()

    def _main_frame_setup(self) -> None:
        """"""
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _create_options_frame(self) -> None:
        """"""
        # configure grid layout (1x11)
        self._frm_options = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        self._frm_options.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self._frm_options.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self._frm_options.grid_rowconfigure(1, minsize=20)  # empty row with minsize as spacing
        self._frm_options.grid_rowconfigure(2, minsize=20)  # empty row with minsize as spacing
        self._frm_options.grid_rowconfigure(3, weight=1)    # empty row as spacing
        self._frm_options.grid_rowconfigure(4, minsize=10)  # empty row with minsize as spacing
        self._frm_options.grid_rowconfigure(5, minsize=20)  # empty row with minsize as spacing

        self.lbl_options = customtkinter.CTkLabel(
            master=self._frm_options,
            text="OPTIONS",
            text_font=("Roboto Medium", 16) # font name and size in px
        )
        self.lbl_options.grid(row=0, column=0, pady=10, padx=10)

        self.btn_load_image = customtkinter.CTkButton(
            master=self._frm_options,
            text="Load Image",
            command=self.load_image
        )
        self.btn_load_image.grid(row=1, column=0, pady=10, padx=20)

        self.btn_save_image = customtkinter.CTkButton(
            master=self._frm_options,
            text="Save Image",
            command=self.save_image
        )
        self.btn_save_image.grid(row=2, column=0, pady=10, padx=20)

        self.lbl_space = customtkinter.CTkLabel(master=self._frm_options, text="")
        self.lbl_space.grid(row=3, column=0, pady=0, padx=20, sticky="s")

        self.lbl_mode = customtkinter.CTkLabel(master=self._frm_options, text="Appearance Mode:")
        self.lbl_mode.grid(row=4, column=0, pady=0, padx=20, sticky="s")

        self.mnu_appearance = customtkinter.CTkOptionMenu(
            master=self._frm_options,
            values=["Dark", "Light", "System"],
            command=self.change_appearance_mode
        )
        self.mnu_appearance.grid(row=5, column=0, pady=10, padx=20, sticky="w")

    def _create_image_frame(self) -> None:
        """"""
        self._frm_image = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        self._frm_image.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

        self._frm_image.rowconfigure(0, weight=1)
        self._frm_image.columnconfigure(0, weight=1)

        # TODO: CHECK
        self.lbl_image = customtkinter.CTkLabel(
            master=self._frm_image,
            text="IMAGE",
            corner_radius=6,                # <- custom corner radius
            fg_color=("white", "gray38"),   # <- custom tuple-color
            justify=tkinter.CENTER
        )
        self.lbl_image.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.slider_1 = customtkinter.CTkSlider(
            master=self._frm_image,
            from_=0,
            to=1,
            number_of_steps=3,
            command=self.btn_event
        )
        self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_2 = customtkinter.CTkSlider(
            master=self._frm_image,
            command=self.btn_event
        )
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

    def _create_tools_frame(self) -> None:
        """"""
        self._frm_tools = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        self._frm_tools.grid(row=0, column=2, sticky="nswe", padx=10, pady=10)

        # TODO: CHECK
        # configure grid layout (3x7)
        # self._frm_tools.rowconfigure((0, 1, 2, 3), weight=1)
        # self._frm_tools.rowconfigure(7, weight=10)
        # self._frm_tools.columnconfigure((0, 1), weight=1)
        # self._frm_tools.columnconfigure(2, weight=0)

        self.lbl_rotate = customtkinter.CTkLabel(
            master=self._frm_tools,
            text="TOOLS",
            text_font=("Roboto Medium", 16) # font name and size in px
        )
        self.lbl_rotate.grid(row=0, column=0, pady=20, padx=10)

        self.lbl_rotate = customtkinter.CTkLabel(
            master=self._frm_tools,
            text="Rotate",
            text_font=(16,)
        )
        self.lbl_rotate.grid(row=1, column=0, sticky="")

        self.lbl_rotate = customtkinter.CTkLabel(
            master=self._frm_tools,
            text="Type the angle in degress.",
        )
        self.lbl_rotate.grid(row=2, column=0, sticky="n")

        self.ent_rotate = customtkinter.CTkEntry(
            master=self._frm_tools,
            width=160,
            placeholder_text="Rotation in degress..."
        )
        self.ent_rotate.grid(row=3, column=0, sticky="n")

    def _set_default_configs(self) -> None:
        """"""
        self.mnu_appearance.set("Dark")
        self.slider_1.set(0.2)
        self.slider_2.set(0.7)

    def btn_event(self):
        print("Button pressed")

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
        """
        TODO: FIX image_data type!!
        """
        image = image_data.image
        image.thumbnail((350, 350))

        tk_image = ImageTk.PhotoImage(image)

        self._img_canvas.create_image(10, 10, image=tk_image)
        self._img_canvas.image = tk_image

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

    # def on_closing(self, event: int=0):
    #     """"""
    #     self.destroy()
    # TODO: CHECK IF CAN BE REMOVABLE

    def _on_closing(self):
        """"""
        self.destroy()
