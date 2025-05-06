"""
Main entry point for the Python Auto Movement application.
This module handles the process creation and keyboard event handling.
"""
from multiprocessing import Process
import sys
import logging
from pynput import keyboard

from dislaimer import disclaimer
from mouse_mover import fiverr_auto_mouse_mover

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Global variable to control the automation
automation_running = False


def on_press(key):
    """
    Handle key presses for starting and stopping the automation.
    """
    global automation_running
    try:
        if key == keyboard.Key.ctrl_l:  # Ctrl pressed
            if automation_running:
                logger.info("Stopping mouse automation...")
                automation_running = False
                # Terminate the process safely
                if fiverr_auto_mouse_mover_thread.is_alive():
                    fiverr_auto_mouse_mover_thread.terminate()
                    fiverr_auto_mouse_mover_thread.join(timeout=2)
                logger.info("Automation stopped.")
                return None
            else:
                logger.info("Starting mouse automation...")
                # Start automation
                fiverr_auto_mouse_mover_thread.start()
                automation_running = True
                logger.info("Automation started.")
                return None
        elif key == keyboard.Key.esc:  # Escape to exit
            logger.info("Exiting...")
            return False  # Stop listener
        return None
    except Exception as e:
        logger.error(f"Error on key press: {e}")
        return None


def on_release(key):
    """
    Handle key releases.
    """
    pass


def main():
    """
    Main function that creates and manages the mouse mover process.
    Handles keyboard events for starting and stopping the automation.
    """
    global fiverr_auto_mouse_mover_thread
    try:
        # Display disclaimer
        disclaimer()

        # Create process but don't start it yet
        fiverr_auto_mouse_mover_thread = Process(
            target=fiverr_auto_mouse_mover,
            daemon=True  # Make it a daemon so it exits when main process exits
        )

        # Setup pynput listener for keyboard events
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()

        # Wait for the listener to run
        listener.join()

    except KeyboardInterrupt:
        logger.info("Keyboard interrupt detected")
    except Exception as e:
        logger.error(f"An error occurred in the main function: {e}", exc_info=True)
    finally:
        # Clean up resources
        if 'fiverr_auto_mouse_mover_thread' in locals() and fiverr_auto_mouse_mover_thread.is_alive():
            fiverr_auto_mouse_mover_thread.terminate()
            fiverr_auto_mouse_mover_thread.join(timeout=2)
        logger.info("Application terminated")


if __name__ == '__main__':
    main()
