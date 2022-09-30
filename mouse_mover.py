import time
from datetime import datetime, timedelta
import random

import pyautogui

from define import mouse_movement_type, fiverr_press_links


def fiverr_mouse_restart():
    print("-------------------------------Restarting-------------------------------------")
    if random.randint(0, 1) != 0:
        fiverr_nav_handler()
    else:
        fiverr_auto_mouse_mover()


def fiverr_mouse_sleep():
    print("--------------------------------Sleeping---------------------------------------")
    time.sleep(random.randint(18, 30))
    fiverr_mouse_restart()


def fiverr_auto_mouse_mover():
    print("---------------------------------Moving----------------------------------------")
    started_time = datetime.now() + timedelta(seconds=random.uniform(1.6, 3.7))
    while datetime.now() < started_time:
        pyautogui.moveTo(random.randint(100, 1777), random.randint(126, 1025), random.uniform(0.6, 2.7),
                         getattr(pyautogui, random.choice(mouse_movement_type)))
    fiverr_mouse_sleep()


def fiverr_nav_handler():
    link = random.randint(0, len(fiverr_press_links) - 1)

    fiverr_mouse_move_to_position(
        random.randint(fiverr_press_links[link]['width']['start'], fiverr_press_links[link]['width']['end']),
        random.randint(fiverr_press_links[link]['height']['start'], fiverr_press_links[link]['height']['end'])
    )
    if link > 2:
        sub_link = random.randint(0, len(fiverr_press_links[link]['sub_menu']) - 1)
        fiverr_mouse_move_to_position(
            random.randint(
                fiverr_press_links[link]['sub_menu'][sub_link]['width']['start'],
                fiverr_press_links[link]['sub_menu'][sub_link]['width']['end']
            ),
            random.randint(
                fiverr_press_links[link]['sub_menu'][sub_link]['height']['start'],
                fiverr_press_links[link]['sub_menu'][sub_link]['height']['end']
            )
        )
    fiverr_mouse_sleep()


def fiverr_mouse_move_to_position(width, height):
    print('--------------------------Mouse Move To Position------------------------------')
    pyautogui.moveTo(width, height, random.uniform(0.6, 2.7), getattr(pyautogui, random.choice(mouse_movement_type)))
    time.sleep(random.uniform(0.6, 1))
    pyautogui.click()

    time.sleep(random.uniform(0.6, 1))
