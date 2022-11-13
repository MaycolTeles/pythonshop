"""
Module containing the "Tkinter" Class.
"""

import pathlib

import customtkinter
from PIL import ImageTk
from tkinter import filedialog, Canvas

from src.infrastructure.ui.interfaces import UIInterface
from src.adapters.controllers.implementations import LoadImageController, RotateImageController, ResetImageController
from src.adapters.presenters.implementations import ImagePresenter


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Tkinter(UIInterface, customtkinter.CTk):
    """
    Class to represent a "Tkinter" UserInterface.
    """
    CURRENT_PATH = pathlib.Path().resolve()

    def execute(self) -> None:
        """"""
        self._create_interface()
        self.mainloop()

    def _create_interface(self) -> None:
        """"""
        self._setup()
        self._main_frame_setup()
        self._create_frames()

    def _setup(self) -> None:
        """"""
        self.title("PYTHONSHOP")
        self.attributes('-zoomed', True)

        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _create_frames(self) -> None:
        """"""
        self._create_options_frame()
        self._create_image_frame()
        self._create_tools_frame()

    def _main_frame_setup(self) -> None:
        """"""
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _create_options_frame(self) -> None:
        """"""
        # configure grid layout (1x11)
        frm_options = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        frm_options.grid(row=0, column=0, pady=10, padx=10, sticky="ns")

        frm_options.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(1, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(2, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(3, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(4, minsize=20)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(5, weight=1)    # empty row as spacing
        frm_options.grid_rowconfigure(6, minsize=10)  # empty row with minsize as spacing
        frm_options.grid_rowconfigure(7, minsize=20)  # empty row with minsize as spacing

        lbl_options = customtkinter.CTkLabel(
            master=frm_options,
            text="OPTIONS",
            text_font=("Roboto Medium", 16) # font name and size in px
        )
        lbl_options.grid(row=0, column=0, pady=10, padx=10)

        btn_load_image = customtkinter.CTkButton(
            master=frm_options,
            text="Load Image",
            command=self.load_image
        )
        btn_load_image.grid(row=1, column=0, pady=10, padx=20)

        self.color = btn_load_image.cget('bg')

        btn_save_image = customtkinter.CTkButton(
            master=frm_options,
            text="Save Image",
            command=self.save_image
        )
        btn_save_image.grid(row=2, column=0, pady=10, padx=20)

        btn_reset_image = customtkinter.CTkButton(
            master=frm_options,
            text="Reset Image",
            command=self.reset_image
        )
        btn_reset_image.grid(row=3, column=0, pady=10, padx=20)

        btn_apply_changes = customtkinter.CTkButton(
            master=frm_options,
            text="Apply Changes",
            command=self.apply_changes_to_image
        )
        btn_apply_changes.grid(row=4, column=0, pady=10, padx=20)

        lbl_space = customtkinter.CTkLabel(master=frm_options, text="")
        lbl_space.grid(row=5, column=0)

        lbl_mode = customtkinter.CTkLabel(master=frm_options, text="Appearance Mode:")
        lbl_mode.grid(row=6, column=0, pady=0, padx=20)

        mnu_appearance = customtkinter.CTkOptionMenu(
            master=frm_options,
            values=["Dark", "Light", "System"],
            command=self.change_appearance_mode
        )
        mnu_appearance.grid(row=7, column=0, pady=(0,20), padx=20)
        mnu_appearance.set("Dark")

    def _create_image_frame(self) -> None:
        """"""
        frm_image = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        frm_image.grid(row=0, column=1, pady=10, padx=10, sticky="nswe")

        # frm_image.rowconfigure(0)
        # frm_image.rowconfigure(1, weight=1)
        # frm_image.rowconfigure(2)
        # frm_image.columnconfigure(0, weight=1)

        lbl_image = customtkinter.CTkLabel(
            master=frm_image,
            text="IMAGE",
            text_font=("Roboto Medium", 16) # font name and size in px
        )
        lbl_image.grid(column=0, row=0, padx=10, pady=10)

        self.canvas = Canvas(frm_image, bg="#2A2D2E", highlightthickness=0)
        self.canvas.grid(row=1, column=0, sticky="nswe")

        frm_image.grid_rowconfigure(1, weight=1)
        frm_image.grid_columnconfigure(0, weight=1)

        slider_1 = customtkinter.CTkSlider(
            master=frm_image,
            from_=0,
            to=1,
            number_of_steps=3,
            command=self.btn_event
        )
        slider_1.grid(row=2, column=0, pady=10, padx=20)
        slider_1.set(0.2)

        slider_2 = customtkinter.CTkSlider(
            master=frm_image,
            command=self.btn_event
        )
        slider_2.grid(row=3, column=0, columnspan=2, pady=10, padx=20)
        slider_2.set(0.7)

    def _create_tools_frame(self) -> None:
        """"""
        frm_tools = customtkinter.CTkFrame(
            master=self,
            corner_radius=20
        )
        frm_tools.grid(row=0, column=2, pady=10, padx=10, sticky="ns")

        # TODO: CHECK
        # configure grid layout (3x7)
        # frm_tools.rowconfigure((0, 1, 2, 3), weight=1)
        # frm_tools.rowconfigure(7, weight=10)
        # frm_tools.columnconfigure((0, 1), weight=1)
        # frm_tools.columnconfigure(2, weight=0)

        lbl_rotate = customtkinter.CTkLabel(
            master=frm_tools,
            text="TOOLS",
            text_font=("Roboto Medium", 16) # font name and size in px
        )
        lbl_rotate.grid(row=0, column=0, padx=20, pady=10)

        lbl_rotate = customtkinter.CTkLabel(
            master=frm_tools,
            text="Rotation",
            text_font=(16,),
            fg_color=("white", "gray38"),
            corner_radius=5
        )
        lbl_rotate.grid(row=1, column=0)

        self.ent_rotate = customtkinter.CTkEntry(
            master=frm_tools,
            width=160,
            placeholder_text="Type the angle in degrees..."
        )
        self.ent_rotate.grid(row=3, column=0, padx=20, pady=20)

        btn_rotate = customtkinter.CTkButton(
            master=frm_tools,
            text="Rotate",
            text_font=(16,),
            command=self.rotate_image,
            corner_radius=5
        )
        btn_rotate.grid(row=4, column=0, padx=20, pady=0)

    def btn_event(self):
        print("BUTTON PRESSED!")

    def load_image(self) -> None:
        """
        Method to load the image.
        """
        filetypes = (
            ("images", ["*.png", "*.jpg", "*.jpeg", "*.gif", "*.svg"]),
        )

        image_name = filedialog.askopenfilename(
            title="Open Image",
            initialdir=self.CURRENT_PATH,
            filetypes=filetypes
        )

        image_data = {
            "image_path": image_name
        }

        controller = LoadImageController()
        controller.execute(image_data)

    def reset_image(self) -> None:
        """"""
        controller = ResetImageController()
        controller.execute()

    def apply_changes_to_image(self) -> None:
        """"""

    def show_image(self, image_data: ImagePresenter) -> None:
        """
        TODO: FIX image_data type!!
        """
        image = image_data.image

        # TODO: UI CALLING THE IMAGE LIB METHOD. MUST CHANGE IT.
        # RESIZING THE IMAGE
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        resized_image = image.resize((canvas_width, canvas_height)) 

        # DISPLAYING THE IMAGE
        tk_image = ImageTk.PhotoImage(resized_image)

        self.canvas.create_image(0, 0, image=tk_image, anchor="nw")
        self.canvas.image = tk_image

    def save_image(self) -> None:
        """
        Method to save the image.
        """
        image_name = filedialog.asksaveasfilename(
            title="Save Image",
            initialdir=self.CURRENT_PATH
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
        rotation_angle = self.ent_rotate.get()

        image_data = {
            "rotation_angle": rotation_angle
        }

        controller = RotateImageController()
        controller.execute(image_data)

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def _on_closing(self):
        """"""
        self.destroy()
