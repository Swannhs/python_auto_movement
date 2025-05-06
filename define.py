"""
Constants and configuration for the Python Auto Movement application.
This module defines the mouse movement types and UI element coordinates.
"""
from typing import List, Dict, Any, Union

# Available easing functions for mouse movement
# These are the names of functions in the PyAutoGUI library
mouse_movement_type: List[str] = [
    'easeInQuad',
    'easeOutQuad',
    'easeInOutQuad',
    'easeInCubic',
    'easeOutCubic',
    'easeInOutCubic',
    'easeInQuart',
    'easeOutQuart',
    'easeInOutQuart',
    'easeInQuint',
    'easeOutQuint',
    'easeInOutQuint',
    'easeInSine',
    'easeOutSine',
    'easeInOutSine',
    'easeInExpo',
    'easeOutExpo',
    'easeInOutExpo',
    'easeInCirc',
    'easeOutCirc',
    'easeInOutCirc',
    'easeInElastic',
    'easeOutElastic',
    'easeInOutElastic',
    'easeInBack',
    'easeOutBack',
    'easeInOutBack',
    'easeInBounce',
    'easeOutBounce',
    'easeInOutBounce',
]

# UI element coordinate definitions
# Each element has a width and height range for mouse targeting

# Dashboard element
dashboard: Dict[str, Union[str, Dict[str, Dict[str, int]]]] = {
    'name': 'dashboard',
    'width': {
        'start': 287,
        'end': 410
    },
    'height': {
        'start': 120,
        'end': 150
    }
}

# My Business element with sub-menu items
my_business: Dict[str, Union[str, Dict[str, Dict[str, int]], List[Dict[str, Dict[str, int]]]]] = {
    'name': 'my_business',
    'width': {
        'start': 427,
        'end': 581
    },
    'height': {
        'start': 128,
        'end': 158
    },
    'sub_menu': [
        {
            'name': 'sub_item_1',
            'width': {
                'start': 440,
                'end': 558
            },
            'height': {
                'start': 202,
                'end': 214
            },
        },
        {
            'name': 'sub_item_2',
            'width': {
                'start': 440,
                'end': 558
            },
            'height': {
                'start': 253,
                'end': 263
            },
        },
        {
            'name': 'sub_item_3',
            'width': {
                'start': 440,
                'end': 558
            },
            'height': {
                'start': 311,
                'end': 325
            },
        }
    ]
}

# Notifications element
notifications: Dict[str, Union[str, Dict[str, Dict[str, int]]]] = {
    'name': 'notifications',
    'width': {
        'start': 1530,
        'end': 1545
    },
    'height': {
        'start': 125,
        'end': 146
    }
}

# Messages element
messages: Dict[str, Union[str, Dict[str, Dict[str, int]]]] = {
    'name': 'messages',
    'width': {
        'start': 1561,
        'end': 1608
    },
    'height': {
        'start': 125,
        'end': 146
    }
}

# Profile element with sub-menu items
profile: Dict[str, Union[str, Dict[str, Dict[str, int]], List[Dict[str, Dict[str, int]]]]] = {
    'name': 'profile',
    'width': {
        'start': 1711,
        'end': 1734
    },
    'height': {
        'start': 129,
        'end': 138
    },
    'sub_menu': [
        {
            'name': 'profile_settings',
            'width': {
                'start': 1415,
                'end': 1632
            },
            'height': {
                'start': 382,
                'end': 400
            },
        }
    ]
}

# List of all clickable elements
fiverr_press_links: List[Dict[str, Any]] = [dashboard, messages, notifications, my_business]
