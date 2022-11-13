"""
Module containing the 'UserInterface' Interface.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models.response.implementations import ImageResponseModel


# MODULE IMPORTS
from abc import ABC, abstractmethod


class UIInterface(ABC):
    """
    Interface containing all the methods that all user interfaces must implement.
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Abstract Method to execute the user interface.

        This method must be implemented in all "UserInterfaces" classes.
        """

    @abstractmethod
    def show_image(self, response_model: ImageResponseModel) -> None:
        """
        Abstract Method to show the image.

        This method must be implemented in all "UserInterfaces" classes.
        """

    @abstractmethod
    def load_image(self) -> None:
        """
        Abstract Method to load the image.

        This method must be implemented in all "UserInterfaces" classes.
        """

    @abstractmethod
    def save_image(self) -> None:
        """
        Abstract Method to save the image.

        This method must be implemented in all "UserInterfaces" classes.
        """

    @abstractmethod
    def crop_image(self) -> None:
        """
        Abstract Method to crop the image.

        This method must be implemented in all "UserInterfaces" classes.
        """

    @abstractmethod
    def rotate_image(self) -> None:
        """
        Abstract Method to rotate the image.

        This method must be implemented in all "UserInterfaces" classes.
        """
