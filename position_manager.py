"""
Position manager for the Python Auto Movement application.
This module handles capturing, saving, and loading mouse positions.
"""
import os
import json
import logging
from typing import Dict, List, Any, Optional, Tuple
from pynput.keyboard import Listener as KeyboardListener, Key
from pynput.mouse import Listener as MouseListener, Button

# Configure logging
logger = logging.getLogger(__name__)

# File to store positions
POSITIONS_FILE = "positions.json"

def save_positions(positions: Dict[str, Any]) -> bool:
    """
    Save positions to a JSON file.
    
    Args:
        positions: Dictionary of positions to save
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(POSITIONS_FILE, 'w') as f:
            json.dump(positions, f, indent=4)
        logger.info(f"Positions saved to {POSITIONS_FILE}")
        return True
    except Exception as e:
        logger.error(f"Error saving positions: {e}")
        return False

def load_positions() -> Optional[Dict[str, Any]]:
    """
    Load positions from the JSON file.
    
    Returns:
        Dictionary of positions if file exists, None otherwise
    """
    if not os.path.exists(POSITIONS_FILE):
        logger.info(f"Positions file {POSITIONS_FILE} not found")
        return None
        
    try:
        with open(POSITIONS_FILE, 'r') as f:
            positions = json.load(f)
        logger.info(f"Positions loaded from {POSITIONS_FILE}")
        return positions
    except Exception as e:
        logger.error(f"Error loading positions: {e}")
        return None


def capture_position(element_name: str) -> Optional[Tuple[int, int]]:
    """
    Capture a mouse position only when Shift+Left click is detected.

    Args:
        element_name: Name of the element to capture position for

    Returns:
        Tuple of (x, y) coordinates if successful, None otherwise
    """
    position = None
    shift_pressed = {'state': False}

    def on_key_press(key):
        if key == Key.shift:
            shift_pressed['state'] = True

    def on_key_release(key):
        if key == Key.shift:
            shift_pressed['state'] = False

    def on_click(x, y, button, pressed):
        nonlocal position
        if button == Button.left and pressed and shift_pressed['state']:
            position = (x, y)
            return False  # Stop listener

    print(f"Please Shift+Click on the {element_name} element...")

    # Start both keyboard and mouse listeners
    with KeyboardListener(on_press=on_key_press, on_release=on_key_release) as kl, \
            MouseListener(on_click=on_click) as ml:
        ml.join()  # Wait for mouse click with Shift

    if position:
        logger.info(f"Captured position for {element_name}: {position}")
    else:
        logger.warning(f"Shift+Click not detected for {element_name}")

    return position

def capture_all_positions(elements: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Capture positions for all elements.
    
    Args:
        elements: List of element dictionaries with 'name' keys
        
    Returns:
        Dictionary of positions with element names as keys
    """
    positions = {}
    
    for element in elements:
        element_name = element.get('name', 'Unknown')
        position = capture_position(element_name)
        
        if position:
            x, y = position
            # Create a position dictionary similar to the original format
            positions[element_name] = {
                'name': element_name,
                'width': {
                    'start': x - 10,  # Create a small clickable area
                    'end': x + 10
                },
                'height': {
                    'start': y - 10,
                    'end': y + 10
                }
            }
            
            # If the original element has a sub_menu, ask for those positions too
            if 'sub_menu' in element:
                positions[element_name]['sub_menu'] = []
                for i, sub_item in enumerate(element['sub_menu']):
                    sub_name = sub_item.get('name', f'sub_item_{i+1}')
                    sub_position = capture_position(f"{element_name} > {sub_name}")
                    
                    if sub_position:
                        sub_x, sub_y = sub_position
                        positions[element_name]['sub_menu'].append({
                            'name': sub_name,
                            'width': {
                                'start': sub_x - 10,
                                'end': sub_x + 10
                            },
                            'height': {
                                'start': sub_y - 10,
                                'end': sub_y + 10
                            }
                        })
    
    return positions

def get_positions(elements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Get positions for all elements, either from file or by capturing.
    
    Args:
        elements: List of element dictionaries with 'name' keys
        
    Returns:
        List of position dictionaries
    """
    # Try to load positions from file
    loaded_positions = load_positions()
    
    if loaded_positions:
        # Convert dictionary to list
        position_list = []
        for element in elements:
            element_name = element.get('name', 'Unknown')
            if element_name in loaded_positions:
                position_list.append(loaded_positions[element_name])
        
        if position_list:
            return position_list
    
    # If no positions loaded, capture them
    print("No saved positions found. You will be asked to click on each element.")
    positions = capture_all_positions(elements)
    
    # Save the positions for future use
    save_positions(positions)
    
    # Convert dictionary to list
    return list(positions.values())