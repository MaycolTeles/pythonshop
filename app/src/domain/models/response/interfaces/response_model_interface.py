"""
Module containing the 'ResponseModel' Abstract Data Structure.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .....infrastructure import UserInterface

# MODULE IMPORTS
from abc import ABC, abstractmethod


class ResponseModelInterface(ABC):
    """
    Class to represent an Abstract Data Structure containing
    all the data needed to perform a use case.
    """
    user_interface: UserInterface

    @abstractmethod
    def build_response(self, response_data: dict[str, Any]) -> None:
        """
        Abstract Method to build the response (map the raw data to the class attributes).

        This method must be implemented in all response models.

        Parameters
        ----------
        response_data : dict[str, Any]
            The raw data to create the response model.
        """
