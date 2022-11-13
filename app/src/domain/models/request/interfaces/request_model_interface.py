"""
Module containing the 'RequestModelInterface' Abstract Data Structure.
"""

from abc import ABC, abstractmethod


class RequestModelInterface(ABC):
    """
    Class to represent an Abstract Data Structure containing
    all the data needed to perform a use case.
    """

    @abstractmethod
    def build_request(self, request_data: dict[str, str]) -> None:
        """
        Abstract Method to build the request (map the raw data to the class attributes).

        This method must be implemented in all request models.

        Parameters
        ----------
        request_data : dict[str, str]
            The raw data to create the request model.
        """
