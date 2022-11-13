"""
Module containing the 'LoadImageRequestModel' Data Structure.
"""

from pathlib import Path

from src.domain.models.request.interfaces.request_model_interface import RequestModelInterface


class LoadImageRequestModel(RequestModelInterface):
    """
    Class to represent a Data Structure containing all the data needed to load an image.
    """
    image_path: Path

    def build_request(self, request_data: dict[str, str]) -> None:
        """
        Method to build the request (map the raw data to the class attributes).

        Parameters
        ----------
        request_data : dict[str, str]
            The raw data to create the request model.
        """
        image_path_str = request_data.get("image_path", "")
        self.image_path = Path(image_path_str)
