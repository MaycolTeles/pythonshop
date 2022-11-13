"""
Module containing the 'RotateImageRequestModel' Data Structure.
"""

from src.domain.models.request.interfaces import RequestModelInterface


class RotateImageRequestModel(RequestModelInterface):
    """
    Class to represent a Data Structure containing all the data needed to rotate an image.
    """
    rotating_angle: float

    def build_request(self, request_data: dict[str, str]) -> None:
        """
        Method to build the request (map the raw data to the class attributes).

        Parameters
        ----------
        request_data : dict[str, str]
            The raw data to create the request model.
        """
        rotate_angle_str = request_data.get("rotation_angle", 0.0)
        self.rotating_angle = float(rotate_angle_str)
