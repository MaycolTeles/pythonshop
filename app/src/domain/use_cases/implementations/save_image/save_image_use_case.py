"""
Module containing the 'SaveImageUseCase' Class.
"""

from pathlib import Path
from typing import Any

from ...interfaces import UseCaseInterface
from src.adapters.presenters.interfaces import PresenterInterface
from src.domain.entities import ImageEntity
from src.domain.models.request.implementations import SaveImageRequestModel
from src.domain.models.response.implementations import ImageResponseModel


class SaveImageUseCase(UseCaseInterface):
    """
    Class containing all the functionalities to save an image.
    """
    _presenter: PresenterInterface

    def __init__(self, presenter: PresenterInterface) -> None:
        """"""
        self._presenter = presenter

    def execute(self, request_model: SaveImageRequestModel) -> None:
        """
        Method to execute the use case. In other words, to save the image.
        """
        image_path = request_model.image_path

        image = ImageEntity()
        image.save(image_path)

    def _build_response_data(self, image_path: Path) -> dict[str, str]:
        """"""
        return {
            "message": f"Image successfully saved in {image_path}"
        }

    def _send_response(self, response_data: dict[str, Any]) -> None:
        """
        Method to send the response to the client, using the presenter.
        """
        response_model = ImageResponseModel()
        response_model.build_response(response_data)

        self._presenter.execute(response_model)
