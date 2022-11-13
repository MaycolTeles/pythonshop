"""
Module containing the 'ControllerInterface' Interface.
"""

from abc import ABC, abstractmethod
from typing import Any


class ControllerInterface(ABC):
    """
    Interface containing all required methods that all controllers must implement.
    """

    @abstractmethod
    def execute(self, data: dict[str, str]) -> None:
        """
        Abstract Method to execute the controller.

        This method must be implemented in all "Controller" classes.
        """
