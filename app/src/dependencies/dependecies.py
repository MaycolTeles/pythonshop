""""""

from src.infrastructure.libraries.images.implementations.pil import PILImageLibrary
from src.infrastructure.ui.implementations.cli import CLI
# from src.infrastructure.ui.implementations.tkinter import Tkinter


IMAGE_LIBRARY_INJECTION = PILImageLibrary()
USER_INTERFACE_INJECTION = CLI()
