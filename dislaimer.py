"""
Disclaimer module for the Python Auto Movement application.
This module provides the disclaimer and version information.
"""
import logging
from typing import NoReturn

# Configure logging
logger = logging.getLogger(__name__)


def disclaimer() -> None:
    """
    Display the application disclaimer, version information, and usage instructions.

    This function prints a formatted message with the application's author,
    version, and keyboard shortcuts for controlling the application.
    """
    try:
        # Application header
        print("=====================================================================")
        print("                       Python Auto Movement                          ")
        print("                         Made By Swann                               ")
        print("                         Version 1.0.0                               ")
        print("=====================================================================")

        # Usage instructions
        print("\nKeyboard Controls:")
        print("  - Press Ctrl + Enter to start the automation")
        print("  - Press Ctrl + Q to stop the current automation")
        print("  - Press Ctrl + Shift + Q to quit the application")

        # Dynamic positions information
        print("\nDynamic Click Positions:")
        print("  - On first run, you will be prompted to click on each UI element")
        print("  - These positions are saved for future use")
        print("  - To reset positions, delete the 'positions.json' file")
        print("\n")

        logger.info("Disclaimer displayed successfully")
    except Exception as e:
        logger.error(f"Error displaying disclaimer: {e}")
