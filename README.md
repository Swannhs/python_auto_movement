# Python Auto Movement

A Python application for automating mouse movements and interactions with a web interface.

## Overview

This application automates mouse movements and clicks on a web interface, specifically designed for Fiverr. It simulates human-like interactions by moving the mouse to different UI elements, clicking, and waiting between actions.

## Features

- Human-like mouse movements using Bézier curves and easing functions
- Natural acceleration and deceleration patterns
- Random micro-movements to simulate human imprecision
- Navigation to different UI elements
- Clicking on elements and sub-menu items
- Configurable sleep durations between actions
- Keyboard shortcuts for controlling the automation

## Requirements

- Python 3.12 or higher
- PyAutoGUI
- Keyboard

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/python_auto_movement.git
   cd python_auto_movement
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Verify the installation by running the test script:
   ```
   python test.py
   ```
   This will demonstrate the human-like mouse movement by moving the mouse to random positions on the screen.

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Use the following keyboard shortcuts:
   - `Ctrl + Enter`: Start the automation
   - `Ctrl + Q`: Stop the current automation
   - `Ctrl + Shift + Q`: Quit the application

## Docker Support

The application can be run in a Docker container:

1. Build the Docker image:
   ```
   docker-compose build
   ```

2. Run the container:
   ```
   docker-compose up
   ```

## Configuration

UI element coordinates and mouse movement types are defined in `define.py`. The application now supports dynamic click positions:

1. On first run, you will be prompted to click on each UI element
2. These positions are saved to a file (`positions.json`)
3. On subsequent runs, the saved positions will be used automatically

To reset the positions and be prompted again, simply delete the `positions.json` file.

## Human-like Mouse Movement

This application implements advanced human-like mouse movement using several techniques:

1. **Bézier Curves**: Instead of moving in straight lines, the mouse follows natural curved paths using Bézier curves with randomly generated control points.

2. **Easing Functions**: The movement uses various easing functions (like quadratic and cubic) to create natural acceleration and deceleration patterns.

3. **Micro-movements**: Small random deviations are added during movement to simulate the natural imprecision of human hand movements.

4. **Variable Speed**: The movement speed varies naturally throughout the path, with more control points for longer distances.

These techniques combine to create mouse movements that are much more natural and human-like, making the automation less detectable.

## Author

Made by Swann

## License

This project is licensed under the MIT License - see the LICENSE file for details.
