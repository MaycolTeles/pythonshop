""""""

from pathlib import Path

from PIL import Image

from src.infrastructure.libraries.images.interfaces import ImageLibraryInterface


class PILImageLibrary(ImageLibraryInterface):
    """"""
    _image: Image.Image

    def load(self, image_path: Path) -> Image.Image:
        """
        Method to load an image.
        """
        self._image = Image.open(image_path)
        return self._image

    def save(self, image_path: Path):
        """
        Method to save an image.
        """
        self._image.save(image_path)

    def rotate(self, angle: float) -> Image.Image:
        """
        Method to rotate an image based on the angle received as argument.
        """
        self._image = self._image.rotate(angle, Image.NEAREST, expand=True)
        return self._image

    def crop(self) -> Image.Image:
        """
        Method to crop an image.
        """
        cropped_image = self._image.crop()
        return cropped_image
