import pyautogui
import win32gui
import time
import os

import locate_image
import script



# Obtient le handle de la fenêtre du jeu (remplacez "NomDuJeu" par le nom de la fenêtre du jeu)
game_window = win32gui.FindWindow(None, "Waven")

# Vérifie si la souris est à l'intérieur de la fenêtre du jeu
rect = win32gui.GetWindowRect(game_window)

# Fonction pour déplacer la souris sur une image et effectuer un clic avec la touche F6
def move_mouse_to_image(image_path):
    # Tente de localiser l'image sur l'écran
    location = pyautogui.locateOnScreen(image_path, confidence=0.8, minSearchTime=2)

    if location is not None:
        # Récupère les coordonnées du centre de l'image
        x, y, width, height = location
        center_x = x + width // 2
        center_y = y + height // 2

        # Déplace la souris sur le centre de l'image
        pyautogui.click(center_x, center_y, clicks=3)

        time.sleep(2)

        script.simple_click()
        return True
    else:
        print(f"Image {image_path} non trouvée.")
        return False

def sort_6pa(directory_path, clic_x, clic_y):
    image_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path)]
    game_window_coordinates = locate_image.get_game_window_coordinates("Waven")
    
    if not game_window_coordinates[0]:  # check if the first value is None
        print("Fenêtre de jeu non trouvée.")
        return False

    detected_image_info = locate_image.detection_images(image_paths, (497, 813, 615, 117), game_window_coordinates)

    if detected_image_info:
        image, location = detected_image_info
        center_x, center_y, width, height = location.left + location.width // 2, location.top + location.height // 2, location.width, location.height

        pyautogui.moveTo(center_x, center_y)
        time.sleep(0.5)
        script.simple_click()
        time.sleep(0.5)
        script.simple_click()

        # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
        pyautogui.moveTo(x=game_window_coordinates[0] + clic_x[0], y=game_window_coordinates[1] + clic_x[1],)
        time.sleep(0.5)
        script.simple_click()

        # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
        pyautogui.moveTo(x=game_window_coordinates[0] + clic_y[0], y=game_window_coordinates[1] + clic_y[1],)
        time.sleep(0.5)
        script.simple_click()

        return True

    else:
        #print("Aucune image détectée.")
        return False

def sort(directory_path, clic_x, clic_y):
    image_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path)]
    game_window_coordinates = locate_image.get_game_window_coordinates("Waven")
    
    if not game_window_coordinates[0]:  # check if the first value is None
        print("Fenêtre de jeu non trouvée.")
        return False

    detected_image_info = locate_image.detection_images(image_paths, (497, 813, 615, 117), game_window_coordinates)

    if detected_image_info:
        image, location = detected_image_info
        center_x, center_y, width, height = location.left + location.width // 2, location.top + location.height // 2, location.width, location.height

        pyautogui.moveTo(center_x, center_y)
        time.sleep(0.5)
        script.simple_click()
        time.sleep(0.5)
        script.simple_click()

        # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
        pyautogui.moveTo(x=game_window_coordinates[0] + clic_x, y=game_window_coordinates[1] + clic_y,)
        time.sleep(0.5)
        script.simple_click()

        return True

    else:
        #print("Aucune image détectée.")
        return False

def sort_single(image_paths, clic_x, clic_y):
    game_window_coordinates = locate_image.get_game_window_coordinates("Waven")
    
    if not game_window_coordinates[0]:  # check if the first value is None
        print("Fenêtre de jeu non trouvée.")
        return False

    detected_image_info = locate_image.detection_images_single(image_paths, (497, 813, 615, 117), game_window_coordinates)

    if detected_image_info:
        image, location = detected_image_info
        center_x, center_y, width, height = location.left + location.width // 2, location.top + location.height // 2, location.width, location.height

        pyautogui.moveTo(center_x, center_y)
        time.sleep(0.5)
        script.simple_click()
        time.sleep(0.5)
        script.simple_click()

        # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
        pyautogui.moveTo(x=game_window_coordinates[0] + clic_x, y=game_window_coordinates[1] + clic_y,)
        time.sleep(0.5)
        script.simple_click()

        return True

    else:
        #print("Aucune image détectée.")
        return False

def deplacement(start_x, start_y, end_x, end_y):
    """Effectue un déplacement lent de la souris d'un point de départ à un point de fin."""

    # Durée du clic en secondes
    clic_duration = 5.0  # par exemple, 2 secondes

    # Nombre d'étapes de déplacement
    num_steps = 15 # Augmentez ce nombre pour un déplacement plus lent

    # Calcule le délai entre chaque étape de déplacement
    step_delay = clic_duration / num_steps
    
    # Déplace la souris à la position de départ
    pyautogui.moveTo(x=rect[0] + start_x, y=rect[1] + start_y,)

    # Effectue le déplacement lent vers la position de fin
    for step in range(num_steps):
        # Calcule les nouvelles coordonnées intermédiaires
        x = int(start_x + (end_x - start_x) * (step / num_steps))
        y = int(start_y + (end_y - start_y) * (step / num_steps))

        script.hold_click(5000)
        # Déplace la souris à la nouvelle coordonnée
        pyautogui.moveTo(x + rect[0], y + rect[1])
    
        # Attendez le délai entre les étapes de déplacement
    time.sleep(step_delay)
    
    # Déplacez la souris à la position de fin
    pyautogui.moveTo(x=rect[0] + end_x, y=rect[1] + end_y,tween=pyautogui.easeInOutQuad)

    # Relâche le clic gauche
    pyautogui.mouseUp()

def deplacement_2step(start_x, start_y, end_x, end_y, mid_x=None, mid_y=None):
    """Effectue un déplacement lent de la souris d'un point de départ à un point intermédiaire (si fourni) puis à un point de fin."""
    
    # Durée du clic en secondes
    clic_duration = 3.0

    # Nombre d'étapes de déplacement
    num_steps = 10

    # Calcule le délai entre chaque étape de déplacement
    step_delay = clic_duration / num_steps

    # Si aucune position intermédiaire n'est fournie, utilisez la position finale comme position intermédiaire
    if mid_x is None or mid_y is None:
        mid_x, mid_y = end_x, end_y

    # Liste des points par lesquels la souris va passer
    waypoints = [(start_x, start_y), (mid_x, mid_y), (end_x, end_y)]

    # Effectue le déplacement lent pour chaque paire de points consécutifs dans waypoints
    for i in range(len(waypoints) - 1):
        sx, sy = waypoints[i]
        ex, ey = waypoints[i+1]
        for step in range(num_steps):
            x = int(sx + (ex - sx) * (step / num_steps))
            y = int(sy + (ey - sy) * (step / num_steps))
            
            script.hold_click(9000)

            pyautogui.moveTo(x + rect[0], y + rect[1])
            time.sleep(step_delay)

    # Relâche le clic gauche
    pyautogui.mouseUp()

def click_coor(clic_x, clic_y):

        if (0 <= clic_x < rect[2] - rect[0]) and (0 <= clic_y < rect[3] - rect[1]):
            # Attend un court délai avant le clic
            time.sleep(0.5)  # ajustez la valeur du délai au besoin
                
            # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
            pyautogui.click(x=rect[0] + clic_x, y=rect[1] + clic_y,)
            
            script.simple_click()

def abandonner():
    click_coor(32, 902)
    click_coor(177, 817)
    click_coor(745, 508)
