"""
Module to run the application.
"""

from src.dependencies import USER_INTERFACE_INJECTION


def run() -> None:
    """
    Function to run the application.
    """
    user_interface = USER_INTERFACE_INJECTION
    user_interface.execute()


if __name__ == "__main__":
    run()
