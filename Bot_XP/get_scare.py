import win32gui
import pyautogui
import win32api

# Obtient le handle de la fenêtre du jeu (remplacez "Waven" par le nom de la fenêtre du jeu)
game_window = win32gui.FindWindow(None, "Waven")

start_position = None
is_dragging = False

print("Cliquez et faites glisser pour délimiter une zone dans la fenêtre du jeu.")

while True:
    left_click = win32api.GetKeyState(0x01)  # 0x01 est le code pour le bouton gauche de la souris

    # Obtient la position actuelle de la souris à l'écran
    x, y = pyautogui.position()

    # Convertit les coordonnées en coordonnées relatives à la fenêtre du jeu
    rect = win32gui.GetWindowRect(game_window)
    x_rel = x - rect[0]
    y_rel = y - rect[1]

    # Vérifie si la souris est à l'intérieur de la fenêtre du jeu
    if (0 <= x_rel < rect[2] - rect[0]) and (0 <= y_rel < rect[3] - rect[1]):
        # Si le bouton gauche est enfoncé
        if left_click == -127 or left_click == -128:
            if not start_position:
                start_position = (x_rel, y_rel)
            is_dragging = True
        elif is_dragging:  # Si le bouton gauche est relâché après avoir été enfoncé
            width = x_rel - start_position[0]
            height = y_rel - start_position[1]
            print(f"Zone délimitée : Debut ({start_position[0]}, {start_position[1]}) - Largeur: {width}, Hauteur: {height}")
            start_position = None
            is_dragging = False
