""""""

from pathlib import Path

from PIL import Image

from src.infrastructure.libraries.images.interfaces import ImageLibraryInterface


class PILImageLibrary(ImageLibraryInterface):
    """"""
    _original_image: Image.Image
    _image: Image.Image

    def get_original_image(self) -> Image.Image:
        """"""
        return self._original_image

    def load(self, image_path: Path) -> Image.Image:
        """
        Method to load an image.
        """
        self._image = Image.open(image_path)
        self._original_image = self._image
        return self._image

    def save(self, image_path: Path):
        """
        Method to save an image.
        """
        DEFAULT_IMAGE_EXTENSION = "PNG"
        image_path_plus_extension = image_path.with_suffix(".png")
        self._image.save(image_path_plus_extension, DEFAULT_IMAGE_EXTENSION)

    def rotate(self, angle: float) -> Image.Image:
        """
        Method to rotate an image based on the angle received as argument.
        """
        _image = self._image.rotate(angle)
        return _image

    def crop(self) -> Image.Image:
        """
        Method to crop an image.
        """
        cropped_image = self._image.crop()
        return cropped_image
