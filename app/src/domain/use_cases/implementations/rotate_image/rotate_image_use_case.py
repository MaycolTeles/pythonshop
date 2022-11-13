"""
Module containing the 'RotateImageUseCase' Class.
"""

from typing import Any

from src.adapters.presenters.interfaces.presenter_interface import PresenterInterface
from src.domain.entities import ImageEntity
from src.domain.use_cases import UseCaseInterface
from src.domain.models.request.implementations import RotateImageRequestModel
from src.domain.models.response.implementations import ImageResponseModel


class RotateImageUseCase(UseCaseInterface):
    """
    Class containing all the functionalities to rotate an image.
    """
    _presenter: PresenterInterface

    def __init__(self, presenter: PresenterInterface) -> None:
        """"""
        self._presenter = presenter

    def execute(self, request_model: RotateImageRequestModel) -> None:
        """
        Method to execute the use case. In other words, to rotate the image.

        This method must be implemented in all "UseCases" classes.
        """
        rotating_angle = request_model.rotating_angle

        image = ImageEntity()
        rotated_image = image.rotate(rotating_angle)

        response_data = self._build_response_data(rotated_image)
        self._send_response(response_data)

    def _build_response_data(self, image: Any) -> dict[str, Any]:
        """"""
        return {
            "image": image
        }

    def _send_response(self, response_data: dict[str, Any]) -> None:
        """
        Method to send the response to the client, using the presenter.
        """
        response_model = ImageResponseModel()
        response_model.build_response(response_data)

        self._presenter.execute(response_model)
