"""
Test script for the Python Auto Movement application.
This script tests the human-like mouse movement implementation.
"""
import time
import random
import logging
import sys

from mouse_mover import move_mouse_to, perform_random_movement, perform_navigation

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def test_human_like_movement():
    """
    Test the human-like mouse movement by moving to random positions.
    """
    logger.info("Testing human-like mouse movement...")

    # Perform several random movements to demonstrate the human-like behavior
    for i in range(5):
        # Generate random coordinates within screen bounds
        x = random.randint(100, 1777)
        y = random.randint(126, 1025)

        # Random duration between 0.8 and 2.5 seconds
        duration = random.uniform(0.8, 2.5)

        logger.info(f"Movement {i+1}: Moving to ({x}, {y}) over {duration:.2f} seconds")

        # Move the mouse
        move_mouse_to(x, y, duration)

        # Wait a bit between movements
        time.sleep(1)

    logger.info("Human-like movement test completed")

def test_random_movement():
    """
    Test the random movement function.
    """
    logger.info("Testing random movement function...")
    perform_random_movement()
    logger.info("Random movement test completed")

if __name__ == "__main__":
    # Run the tests
    # test_human_like_movement()
    # test_random_movement()
    perform_navigation()
