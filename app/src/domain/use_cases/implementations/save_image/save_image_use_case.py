"""
Module containing the 'SaveImageUseCase' Class.
"""

from ..interfaces import UseCase
from ...entities import ImageEntity
from ...models.request import SaveImageRequestModel


class SaveImageUseCase(UseCase):
    """
    Class containing all the functionalities to save an image.
    """

    def execute(self, request_model: SaveImageRequestModel) -> None:
        """
        Method to execute the use case. In other words, to save the image.
        """
        image_name = request.image_name

        image = ImageEntity()
        image.save(image_name)
