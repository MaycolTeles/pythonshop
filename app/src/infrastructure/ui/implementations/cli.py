"""
Module containing the "CLI" Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models.response.implementations import ImageResponseModel

# MODULE IMPORTS
import sys

from src.infrastructure.ui.interfaces.ui_interface import UIInterface
from src.adapters.controllers import ImageController


class CLI(UIInterface):
    """
    Class to represent a "CLI" (Command Line Interface) user interface.
    """

    def execute(self) -> None:
        """
        Method to execute the user interface.
        """
        self._show_intro()
        self._show_menu()

    def _show_intro(self) -> None:
        """"""
        print('Welcome to PythonShop! Here you can manipulate your images.')

    def _show_menu(self) -> None:
        """"""
        AVAILABE_MENU_OPTIONS = {
            "1": self.load_image,
            "2": self.save_image,
            "3": self.rotate_image,
            "4": self.crop_image,
            "5": self._show_exit
        }

        self._show_menu_options()
        user_option = self._get_user_option()
        menu_function = AVAILABE_MENU_OPTIONS.get(user_option, self._no_valid_option)

        return menu_function()

    def _no_valid_option(self) -> None:
        """"""
        print("Sorry, but that's not a valid option. Please, try again.")
        self._show_menu()

    def _show_menu_options(self) -> None:
        """"""
        print("""
            Choose an option from menu below:

            1 - Open an image
            2 - Save the image
            3 - Rotate the image
            4 - Crop the image
            5 - Exit
        """)

    def _get_user_option(self) -> str:
        option = input("Type your option: ")
        return option

    def show_image(self, response_model: ImageResponseModel) -> None:
        """
        Method to show the image.
        """
        image = response_model.image

        # TODO: USER INTERFACE CALLING METHODS FROM THE IMAGE LIBRARY???
        # THIS IS CRIMINAL!!!
        image.show()

        return self._show_menu()

    def load_image(self) -> None:
        """
        Method to load the image.
        """
        image_path = input("Type your image name with its full path: ")

        image_data = {
            "image_path": image_path
        }

        controller = ImageController()
        controller.load_image(image_data)

        return self._show_menu()

    def save_image(self) -> None:
        """
        Method to save the image.
        """
        return self._show_menu()

    def crop_image(self) -> None:
        """
        Method to crop the image.
        """
        return self._show_menu()

    def rotate_image(self) -> None:
        """
        Method to rotate the image.
        """
        rotation_angle = input("Please, type the angle that you want the image to be rotated: ")

        angle_data = {
            "rotation_angle": rotation_angle
        }

        controller = ImageController()
        controller.rotate_image(angle_data)

        return self._show_menu()

    def _show_exit(self) -> None:
        """
        Method to show the program exit.
        """
        print('Thank you for using our application. Bye!')
        sys.exit()
