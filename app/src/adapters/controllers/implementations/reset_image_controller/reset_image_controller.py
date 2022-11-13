"""
Module containing the 'ResetImageController' Class.
"""

from src.adapters.controllers.interfaces.controller_interface import ControllerInterface
from src.adapters.presenters.implementations import ImagePresenter
from src.domain.models.request.implementations.load_image_request_model.load_image_request_model import LoadImageRequestModel
from src.domain.use_cases.implementations import ResetImageUseCase


class ResetImageController(ControllerInterface):
    """
    Class to represent a Controller to reset the image to its original state.
    """

    def execute(self) -> None:
        """
        Method to execute the controller to load an image.
        """
        presenter = ImagePresenter()
        use_case = ResetImageUseCase(presenter)

        use_case.execute()
