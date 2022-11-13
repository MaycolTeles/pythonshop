"""
Module containing the 'SaveImageController' Class.
"""

from typing import Any

from ...interfaces import Controller
from .....domain import SaveImageRequestModel, SaveImageUseCase


class SaveImageController(Controller):
    """
    Class to represent a Controller to save an image.
    """

    def execute(self, data: dict[str, str]) -> None:
        """
        Method to execute the controller to save an image.
        """
        request_model = SaveImageRequestModel()
        request_model.build_request(data)

        use_case = SaveImageUseCase()
        use_case.execute(request_model)
