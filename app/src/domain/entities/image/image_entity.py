"""
Class containing the "ImageEntity" Class.
"""

from pathlib import Path
from typing import Any

from src.infrastructure.libraries.images.interfaces.image_lib_interface import ImageLibraryInterface


class ImageEntity():
    """
    Class to represent an Image.
    """
    _image_lib: ImageLibraryInterface

    def __init__(self) -> None:
        """"""
        self._inject_library_dependency()

    def _inject_library_dependency(self) -> None:
        """
        Method to set the '_image_lib' attribute value based on a global constant.

        The import is located inside this method to avoid circular imports.
        # TODO: IMPLEMENT A WAY THAT AVOID CIRCULAR IMPORTS AND THE IMPORT STAYS IN THE BEGGINING OF THE FILE.
        """
        from src.dependencies import IMAGE_LIBRARY_INJECTION

        self._image_lib = IMAGE_LIBRARY_INJECTION

    def get_original_image(self) -> Any:
        """"""
        image = self._image_lib.get_original_image()
        return image

    def load(self, image_path: Path) -> Any:
        """
        Method to load the image based on its path received as argument.

        Parameters
        ----------
        image_path : Path
            The image path.
        """
        image = self._image_lib.load(image_path)
        return image

    def save(self, image_path: Path):
        """
        Method to save the image with the path received as argument.

        Parameters
        ----------
        image_path : Path
            The path to save the image.
        """
        self._image_lib.save(image_path)

    def crop(self):
        """
        Method to crop the image.
        """
        cropped_image = self._image_lib.crop()
        return cropped_image

    def rotate(self, angle: float):
        """
        Method to rotate the image based on the angle received as argument.

        Parameters
        ----------
        angle : float
            The angle the image will be rotated.
        """
        rotated_image = self._image_lib.rotate(angle)
        return rotated_image
