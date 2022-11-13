"""
Module containing the 'PresenterInterface' Interface.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models.response.interfaces.response_model_interface import ResponseModelInterface

# MODULE IMPORTS
from abc import ABC, abstractmethod


class PresenterInterface(ABC):
    """
    Interface containing all the methods that all presenters must implement.
    """

    @abstractmethod
    def execute(self, response_model: ResponseModelInterface) -> None:
        """
        Abstract Method to execute the presenter.

        This method must be implemented in all presenters classes.
        """
