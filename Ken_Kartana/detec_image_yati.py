from typing import Tuple, List
import pyautogui
import win32gui
import time
import numpy as np
from ahk import AHK

def get_game_window_coordinates(window_title: str) -> Tuple[int, int, int, int]:
    # Obtient le handle de la fenêtre
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        return win32gui.GetWindowRect(hwnd)
    else:
        return None, None, None, None

def detection_images(image_paths: List[str], region: Tuple[int, int, int, int], game_window_coordinates)-> List[str]:
    #Liste vide qui le sera quand les images sont détectées
    detected_images = []
    # Convertit les coordonnées de la région relative à la fenêtre en coordonnées absolues
    absolute_region = (
        game_window_coordinates[0] + region[0],
        game_window_coordinates[1] + region[1],
        region[2],
        region[3]
    )

    for image_path in image_paths:
        location = pyautogui.locateOnScreen(image_path, step=5, region=absolute_region, confidence=0.6, minSearchTime=2)

        if location is not None:
            detected_images.append(image_path)
            print(f"Image {image_path} trouvée.")
        else:
            print(f"Image {image_path} non trouvée.")

    return detected_images

def show_region(region: Tuple[int, int, int, int], game_window_coordinates):
    absolute_region = (
        game_window_coordinates[0] + region[0],
        game_window_coordinates[1] + region[1],
        region[2],
        region[3]
    )
    screenshot = pyautogui.screenshot(region=absolute_region)
    screenshot.show()

window_title = "Waven"
game_window_coordinates = get_game_window_coordinates(window_title)

if None not in game_window_coordinates:
    # Active la fenêtre au premier plan
    win32gui.SetForegroundWindow(win32gui.FindWindow(None, window_title))

    #image_test_path = "images/sorts/Ether/coutreduit2pa/teleportpiku5pa.png"

    #detection_images(image_test_path, region=(550, 800, 550, 125), game_window_coordinates=game_window_coordinates)
    #show_region((650, 450, 150, 150), game_window_coordinates=game_window_coordinates)
    #show_region((815, 454, 90, 100), game_window_coordinates=game_window_coordinates)
    images_to_check = [
    "Images/mob.png",
]

    #detected = detection_images(images_to_check, (550, 800, 550, 125), game_window_coordinates)
    detected = detection_images(images_to_check, (810, 455, 100, 110), game_window_coordinates)
    print(f"Images détectées : {detected}")

    #detection_images(image_mob_path, region=(920, 380, 100, 100), game_window_coordinates=game_window_coordinates)
    #show_region((920, 380, 100, 100), game_window_coordinates=game_window_coordinates)
else:
    print("Fenêtre de jeu non trouvée.")