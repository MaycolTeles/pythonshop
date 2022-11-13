"""
Module containing the 'LoadImageController' Class.
"""

from src.adapters.controllers.interfaces.controller_interface import ControllerInterface
from src.adapters.presenters.implementations import ImagePresenter
from src.domain.models.request.implementations.load_image_request_model.load_image_request_model import LoadImageRequestModel
from src.domain.use_cases.implementations.load_image.load_image_use_case import LoadImageUseCase


class LoadImageController(ControllerInterface):
    """
    Class to represent a Controller to load an image.
    """

    def execute(self, data: dict[str, str]) -> None:
        """
        Method to execute the controller to load an image.
        """
        presenter = ImagePresenter()
        use_case = LoadImageUseCase(presenter)

        request_model = LoadImageRequestModel()
        request_model.build_request(data)

        use_case.execute(request_model)
