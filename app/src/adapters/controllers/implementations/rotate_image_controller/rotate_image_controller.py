"""
Module containing the 'RotateImageController' Class.
"""

from src.adapters.controllers.interfaces import ControllerInterface
from src.adapters.presenters.implementations import ImagePresenter
from src.domain.models.request.implementations import RotateImageRequestModel
from src.domain.use_cases.implementations import RotateImageUseCase


class RotateImageController(ControllerInterface):
    """
    Class to represent a Controller to rotate an image.
    """

    def execute(self, data: dict[str, str]) -> None:
        """
        Method to execute the controller to rotate an image.
        """
        request_model = RotateImageRequestModel()
        request_model.build_request(data)

        presenter = ImagePresenter()
        use_case = RotateImageUseCase(presenter)

        use_case.execute(request_model)
