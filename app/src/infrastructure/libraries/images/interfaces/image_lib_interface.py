"""
Module containing the "ImageLibraryInterface" Interface.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class ImageLibraryInterface(ABC):
    """
    Interface containing all required methods that all image libraries must implement.
    """

    @abstractmethod
    def get_original_image(self) -> Any:
        """"""

    @abstractmethod
    def load(self, image_path: Path) -> Any:
        """
        Abstract Method to load an image.

        Parameters
        ----------
        image_path : Path
            The path to load the image.

        This method must be implemented in all "ImageLibrary" classes.
        """

    @abstractmethod
    def save(self, image_path: Path) -> None:
        """
        Abstract Method to save an image.

        Parameters
        ----------
        image_path : Path
            The path to save the image.

        This method must be implemented in all "ImageLibrary" classes.
        """

    @abstractmethod
    def crop(self) -> Any:
        """
        Abstract Method to crop an image.

        This method must be implemented in all "ImageLibrary" classes.
        """

    @abstractmethod
    def rotate(self, angle: float) -> Any:
        """
        Abstract Method to rotate an image based on the angle received as argument.]

        Parameters
        ----------
        angle : float
            The angle to rotate the image.

        This method must be implemented in all "ImageLibrary" classes.
        """
