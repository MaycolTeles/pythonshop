"""
Module containing the 'ImageController' Class.
"""

from src.domain.models.request.implementations import (
    LoadImageRequestModel,
    SaveImageRequestModel,
    RotateImageRequestModel
)
from src.domain.use_cases.implementations import (
    LoadImageUseCase,
    SaveImageUseCase,
    ResetImageUseCase,
    RotateImageUseCase
)


class ImageController():
    """
    Class to represent a Controller to execute all image related functionalities.

    In more details, to call each respectively use case to perform the operation.
    """

    def __init__(self) -> None:
        """
        Constructor to set the 'presenter' attribute value.

        The import is located inside this method to avoid circular imports.
        # TODO: IMPLEMENT A WAY THAT AVOID CIRCULAR IMPORTS AND THE IMPORT STAYS IN THE BEGGINING OF THE FILE.
        """
        from src.adapters.presenters.implementations import ImagePresenter

        self._presenter = ImagePresenter()

    def load_image(self, request: dict[str, str]) -> None:
        """"""
        request_model = LoadImageRequestModel()
        request_model.build_request(request)

        use_case = LoadImageUseCase(self._presenter)
        use_case.execute(request_model)

    def save_image(self, request: dict[str, str]) -> None:
        """
        Method to execute the controller to save an image.
        """
        request_model = SaveImageRequestModel()
        request_model.build_request(request)

        use_case = SaveImageUseCase(self._presenter)
        use_case.execute(request_model)

    def reset_image(self) -> None:
        """"""
        use_case = ResetImageUseCase(self._presenter)
        use_case.execute()

    def rotate_image(self, request: dict[str, str]) -> None:
        """"""
        request_model = RotateImageRequestModel()
        request_model.build_request(request)

        use_case = RotateImageUseCase(self._presenter)
        use_case.execute(request_model)
