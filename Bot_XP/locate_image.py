import pyautogui
import win32gui
import os

from typing import List, Tuple, Union

def get_game_window_coordinates(window_title: str) -> Tuple[int, int, int, int]:
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        return win32gui.GetWindowRect(hwnd)
    else:
        return None, None, None, None

def detection_images(image_paths: List[str], region: Tuple[int, int, int, int], game_window_coordinates) -> Union[None, Tuple[str, Tuple[int, int, int, int]]]:
    absolute_region = (
        game_window_coordinates[0] + region[0],
        game_window_coordinates[1] + region[1],
        region[2],
        region[3]
    )

    for image_path in image_paths:
        location = pyautogui.locateOnScreen(image_path, step=5, region=absolute_region, confidence=0.6, minSearchTime=2)
        #print(f"Location for {image_path}:", location)
        if location is not None:
            print(f"Image {image_path} trouvée.{location}")
            return image_path, location  # Retournez l'image et sa localisation
            
    #print("Aucune image détectée.")
    return None  # Renvoyez None si aucune image n'est trouvée


def detection_images_single(image_path: List[str], region: Tuple[int, int, int, int], game_window_coordinates) -> Union[None, Tuple[str, Tuple[int, int, int, int]]]:
    absolute_region = (
        game_window_coordinates[0] + region[0],
        game_window_coordinates[1] + region[1],
        region[2],
        region[3]
    )
    location = pyautogui.locateOnScreen(image_path, step=5, region=absolute_region, confidence=0.6, minSearchTime=2)
    #print(f"Location for {image_path}:", location)
    if location is not None:
        #print(f"Image {image_path} trouvée.")
        return image_path, location  # Retournez l'image et sa localisation
    #print("Aucune image détectée.")
    return None  # Renvoyez None si aucune image n'est trouvée


