"""
Mouse movement automation module.
This module contains functions for automating mouse movements and clicks.
"""
import time
import logging
import random
import math
from datetime import datetime, timedelta
from typing import NoReturn, List, Tuple, Callable

from pynput.mouse import Button, Controller

from define import mouse_movement_type, fiverr_press_links

# Configure logging
logger = logging.getLogger(__name__)

# Initialize pynput mouse controller
mouse = Controller()

# Easing functions for smooth movement
def ease_out_quad(t: float) -> float:
    """Quadratic easing out - decelerating to zero velocity."""
    return -t * (t - 2)

def ease_in_quad(t: float) -> float:
    """Quadratic easing in - accelerating from zero velocity."""
    return t * t

def ease_in_out_quad(t: float) -> float:
    """Quadratic easing in/out - acceleration until halfway, then deceleration."""
    if t < 0.5:
        return 2 * t * t
    else:
        return -1 + (4 - 2 * t) * t

def ease_out_cubic(t: float) -> float:
    """Cubic easing out - decelerating to zero velocity."""
    return (t - 1) * (t - 1) * (t - 1) + 1

def ease_in_cubic(t: float) -> float:
    """Cubic easing in - accelerating from zero velocity."""
    return t * t * t

def ease_in_out_cubic(t: float) -> float:
    """Cubic easing in/out - acceleration until halfway, then deceleration."""
    if t < 0.5:
        return 4 * t * t * t
    else:
        return (t - 1) * (2 * t - 2) * (2 * t - 2) + 1

# Dictionary mapping easing function names to actual functions
easing_functions = {
    'easeOutQuad': ease_out_quad,
    'easeInQuad': ease_in_quad,
    'easeInOutQuad': ease_in_out_quad,
    'easeOutCubic': ease_out_cubic,
    'easeInCubic': ease_in_cubic,
    'easeInOutCubic': ease_in_out_cubic,
}

def get_bezier_points(start_pos: Tuple[int, int], end_pos: Tuple[int, int], 
                      control_points_count: int = 2) -> List[Tuple[int, int]]:
    """
    Generate control points for a Bézier curve between start_pos and end_pos.

    Args:
        start_pos: Starting position (x, y)
        end_pos: Ending position (x, y)
        control_points_count: Number of control points to generate

    Returns:
        List of control points including start and end positions
    """
    # Start with the start and end positions
    points = [start_pos, end_pos]

    # Calculate the distance between start and end
    distance = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)

    # Generate random control points
    for _ in range(control_points_count):
        # Create a point that's somewhat between start and end, but with some randomness
        # The randomness increases with distance to simulate more natural curves for longer movements
        random_offset_x = random.uniform(-0.25, 0.25) * distance
        random_offset_y = random.uniform(-0.25, 0.25) * distance

        # Calculate a point between start and end
        t = random.uniform(0.3, 0.7)  # Position along the line (30% to 70%)
        x = start_pos[0] + t * (end_pos[0] - start_pos[0]) + random_offset_x
        y = start_pos[1] + t * (end_pos[1] - start_pos[1]) + random_offset_y

        # Insert the control point between start and end
        points.insert(1, (int(x), int(y)))

    return points

def bezier_curve(points: List[Tuple[int, int]], t: float) -> Tuple[int, int]:
    """
    Calculate a point on a Bézier curve at parameter t.

    Args:
        points: List of control points
        t: Parameter between 0 and 1

    Returns:
        Point (x, y) on the curve at parameter t
    """
    n = len(points) - 1
    x = 0
    y = 0

    for i, point in enumerate(points):
        # Bernstein polynomial
        binomial = math.comb(n, i)
        polynomial = binomial * (t ** i) * ((1 - t) ** (n - i))

        # Add weighted point
        x += point[0] * polynomial
        y += point[1] * polynomial

    return int(x), int(y)


def fiverr_auto_mouse_mover() -> NoReturn:
    """
    Main function for automating mouse movements.
    This function runs in an infinite loop, moving the mouse and performing actions.
    """
    try:
        while True:
            try:
                # Randomly choose between navigation and random movement
                if random.randint(0, 1) == 0:
                    perform_random_movement()
                else:
                    perform_navigation()

                # Sleep between actions
                sleep_duration = random.randint(15, 30)
                logger.info(f"Sleeping for {sleep_duration} seconds")
                time.sleep(sleep_duration)

            except Exception as e:
                logger.error(f"Unexpected error during mouse movement: {e}", exc_info=True)
                time.sleep(5)  # Wait a bit before retrying
    except KeyboardInterrupt:
        logger.info("Mouse mover interrupted by keyboard")


def perform_random_movement() -> None:
    """
    Perform random mouse movements for a short duration.
    """
    try:
        logger.info("Performing random mouse movements")
        end_time = datetime.now() + timedelta(seconds=random.uniform(1.6, 3.7))

        while datetime.now() < end_time:
            # Generate random coordinates within screen bounds
            x = random.randint(100, 1777)
            y = random.randint(126, 1025)
            duration = random.uniform(0.6, 2.7)
            easing_function = random.choice(mouse_movement_type)

            logger.debug(f"Moving to ({x}, {y}) with {easing_function} easing")
            move_mouse_to(x, y, duration)
    except Exception as e:
        logger.error(f"Error during random movement: {e}")
        # Don't re-raise, let the main loop handle it


def perform_navigation() -> None:
    """
    Navigate to a random link on the page and possibly a sub-menu item.
    """
    try:
        logger.info("Performing navigation action")

        # Select a random link from the available options
        link_index = random.randint(0, len(fiverr_press_links) - 1)
        link = fiverr_press_links[link_index]

        logger.info(f"Selected link: {link.get('name', f'Link {link_index}')}")

        # Move to and click the selected link
        width = random.randint(link['width']['start'], link['width']['end'])
        height = random.randint(link['height']['start'], link['height']['end'])
        move_and_click(width, height)

        # If the link has a sub-menu, navigate to a random item in it
        if link_index > 2 and 'sub_menu' in link and link['sub_menu']:
            time.sleep(random.uniform(0.5, 1.5))  # Wait for sub-menu to appear

            sub_link_index = random.randint(0, len(link['sub_menu']) - 1)
            sub_link = link['sub_menu'][sub_link_index]

            logger.info(f"Selected sub-menu item: {sub_link_index}")

            width = random.randint(sub_link['width']['start'], sub_link['width']['end'])
            height = random.randint(sub_link['height']['start'], sub_link['height']['end'])
            move_and_click(width, height)
    except Exception as e:
        logger.error(f"Error during navigation: {e}")
        # Don't re-raise, let the main loop handle it


def move_and_click(x: int, y: int) -> None:
    """
    Move the mouse to the specified position and click.

    Args:
        x: The x-coordinate to move to
        y: The y-coordinate to move to
    """
    try:
        logger.debug(f"Moving to position ({x}, {y})")
        move_mouse_to(x, y, random.uniform(0.6, 2.7))

        # Wait a bit before clicking
        time.sleep(random.uniform(0.6, 1))

        # Click
        logger.debug(f"Clicking at ({x}, {y})")
        mouse.click(Button.left)

        # Wait a bit after clicking
        time.sleep(random.uniform(0.6, 1))
    except Exception as e:
        logger.error(f"Error during move and click: {e}")
        raise  # Re-raise to be handled by the caller


def move_mouse_to(x: int, y: int, duration: float) -> None:
    """
    Move the mouse to the specified position using human-like movement.

    This function uses Bézier curves and easing functions to create smooth,
    natural-looking mouse movements that mimic human behavior.

    Args:
        x: The x-coordinate to move to
        y: The y-coordinate to move to
        duration: The duration for the move (in seconds)
    """
    try:
        # Get current mouse position
        start_pos = mouse.position
        end_pos = (x, y)

        # Skip if start and end positions are the same
        if start_pos == end_pos:
            return

        logger.debug(f"Moving from {start_pos} to {end_pos} over {duration} seconds")

        # Select an easing function based on the movement type
        easing_function_name = random.choice(mouse_movement_type)
        # Default to ease_out_quad if the function is not implemented
        easing_function = easing_functions.get(easing_function_name, ease_out_quad)

        logger.debug(f"Using easing function: {easing_function_name}")

        # Generate Bézier curve control points
        # Use more control points for longer distances to create more natural curves
        distance = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
        control_points_count = 2
        if distance > 500:
            control_points_count = 3
        elif distance > 200:
            control_points_count = 2
        else:
            control_points_count = 1

        points = get_bezier_points(start_pos, end_pos, control_points_count)

        # Calculate the number of steps based on duration and distance
        # More steps for longer durations and distances
        steps = max(int(duration * 60), int(distance / 10))
        steps = min(steps, 200)  # Cap at 200 steps to prevent excessive CPU usage

        # Calculate the time interval between steps
        interval = duration / steps

        # Move the mouse along the Bézier curve with easing
        for step in range(steps + 1):
            # Apply easing function to get the parameter t
            t = step / steps
            t_eased = easing_function(t)

            # Calculate the point on the Bézier curve
            point = bezier_curve(points, t_eased)

            # Add small random deviations to simulate human imprecision
            # The deviation decreases as we get closer to the target
            deviation_factor = (1 - t) * 2  # More deviation at the beginning
            deviation_x = random.uniform(-1, 1) * deviation_factor
            deviation_y = random.uniform(-1, 1) * deviation_factor

            # Apply the deviation
            mouse_x = int(point[0] + deviation_x)
            mouse_y = int(point[1] + deviation_y)

            # Set the mouse position
            mouse.position = (mouse_x, mouse_y)

            # Sleep for the calculated interval
            # Add small random variations to the interval to make it more natural
            time.sleep(interval * random.uniform(0.9, 1.1))

        # Ensure we end exactly at the target position
        mouse.position = end_pos

    except Exception as e:
        logger.error(f"Error during mouse move: {e}")
        raise  # Re-raise to be handled by the caller
