"""
Module containing the 'ImagePresenter' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models.response.implementations import ImageResponseModel
    from src.infrastructure.ui.interfaces.ui_interface import UIInterface

# MODULE IMPORTS
from src.adapters.presenters.interfaces.presenter_interface import PresenterInterface


class ImagePresenter(PresenterInterface):
    """
    Class to represent a presenter (response) for showing an image to the user interface.
    """
    _user_interface: UIInterface

    def __init__(self) -> None:
        """"""
        self._inject_user_interface_dependency()

    def _inject_user_interface_dependency(self) -> None:
        """
        Method to set the '_user_interface' attribute value based on a global constant.

        The import is located inside this method to avoid circular imports.
        # TODO: IMPLEMENT A WAY THAT AVOID CIRCULAR IMPORTS AND THE IMPORT STAYS IN THE BEGGINING OF THE FILE.
        """
        from src.dependencies.dependecies import USER_INTERFACE_INJECTION

        self._user_interface = USER_INTERFACE_INJECTION

    def execute(self, response_model: ImageResponseModel) -> None:
        """
        Method to execute the presenter.

        In this case, to return the loaded image to the delivery mechanism.
        """
        self._user_interface.show_image(response_model)
