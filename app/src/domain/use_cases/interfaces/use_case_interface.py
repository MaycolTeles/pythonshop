"""
Module containing the 'UseCaseInterface' Interface.
"""

from abc import ABC, abstractmethod

from src.domain.models.request.interfaces.request_model_interface import RequestModelInterface


class UseCaseInterface(ABC):
    """
    Interface containing all required methods that all use cases must implement.
    """

    @abstractmethod
    def execute(self, request_model: RequestModelInterface) -> None:
        """
        Abstract Method to execute the use case.

        This method must be implemented in all "UseCase" classes.
        """
