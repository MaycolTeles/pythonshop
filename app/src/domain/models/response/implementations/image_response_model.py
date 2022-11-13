"""
Module containing the 'ImageResponseModel' Data Structure.
"""

from typing import Any

from src.domain.models.response.interfaces.response_model_interface import ResponseModelInterface


class ImageResponseModel(ResponseModelInterface):
    """
    Class to represent a Data Structure containing all the data needed to return the processed image.
    """
    image: dict[str, Any]

    def build_response(self, response_data: dict[str, Any]) -> None:
        """
        Method to build the response (map the raw data to the class attributes).

        Parameters
        ----------
        response_data : dict[str, Any]
            The raw data to create the response model.
        """
        self.image = response_data.get("image", None)
