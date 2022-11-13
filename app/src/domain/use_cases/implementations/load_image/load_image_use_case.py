"""
Module containing the 'LoadImageUseCase' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.adapters.presenters.interfaces.presenter_interface import PresenterInterface
    from src.domain.models.request.implementations.load_image_request_model.load_image_request_model import LoadImageRequestModel

# MODULE IMPORTS
from src.domain.entities.image.image_entity import ImageEntity
from src.domain.models.response.implementations import ImageResponseModel
from src.domain.use_cases.interfaces.use_case_interface import UseCaseInterface


class LoadImageUseCase(UseCaseInterface):
    """
    Class containing all the functionalities to load an image.
    """
    _presenter: PresenterInterface

    def __init__(self, presenter: PresenterInterface) -> None:
        """"""
        self._presenter = presenter

    def execute(self, request_model: LoadImageRequestModel) -> None:
        """
        Method to execute the use case.
        
        In this case, to load the image.
        """
        image_path = request_model.image_path

        entity = ImageEntity()
        image = entity.load(image_path)

        response_data = self._build_response_data(image)
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
