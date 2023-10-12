import cv2
import numpy as np
import pyautogui
import time

def find_image_on_screen(target_image_path):
    # Prend une capture d'écran
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot) 
    screen_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    
    # Charge l'image cible en niveaux de gris
    target_image = cv2.imread(target_image_path, cv2.IMREAD_GRAYSCALE)
    w, h = target_image.shape[::-1]

    # Recherche l'image cible dans la capture d'écran
    res = cv2.matchTemplate(screen_gray, target_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        return pt[0], pt[1], w, h

    return None

def sort(image_path, clic_x, clic_y):
    location = find_image_on_screen(image_path)

    if location is not None:
        x, y, width, height = location
        center_x = x + width // 2
        center_y = y + height // 2

        # Déplace la souris sur le centre de l'image
        pyautogui.moveTo(center_x, center_y)
        time.sleep(2)
        simple_click()
        time.sleep(1)
        simple_click()

        # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
        pyautogui.moveTo(x=clic_x, y=clic_y)
        time.sleep(1)
        simple_click()

        return True
    else:
        print(f"Image {image_path} non trouvée.")
        return False

def simple_click():
    pyautogui.click()

if __name__ == "__main__":
    sort("path_to_your_image.png", 100, 200)
