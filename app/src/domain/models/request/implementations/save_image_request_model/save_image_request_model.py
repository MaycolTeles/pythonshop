"""
Module containing the 'SaveImageRequestModel' Data Structure.
"""

from src.domain.models.request.interfaces import RequestModelInterface


class SaveImageRequestModel(RequestModelInterface):
    """
    Class to represent a Data Structure containing all the data needed to save an image.
    """
    image_path: str

    def build_request(self, request_data: dict[str, str]) -> None:
        """
        Method to build the request (map the raw data to the class attributes).

        Parameters
        ----------
        request_data : dict[str, str]
            The raw data to create the request model.
        """
        self.image_path = request_data.get("image_path", "")
