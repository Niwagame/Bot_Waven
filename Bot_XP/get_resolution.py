import win32gui
import pyautogui
import win32api

# Obtient le handle de la fenêtre du jeu (remplacez "Waven" par le nom de la fenêtre du jeu)
game_window = win32gui.FindWindow(None, "Waven")

print("Cliquez pour obtenir les coordonnées dans la fenêtre du jeu.")

previous_left_click = win32api.GetKeyState(0x01)  # État initial du bouton gauche

while True:
    left_click = win32api.GetKeyState(0x01)  # 0x01 est le code pour le bouton gauche de la souris

    # Vérification de l'événement de clic (changement d'état du bouton)
    if previous_left_click != left_click:  # Si l'état du bouton gauche a changé
        previous_left_click = left_click
        
        # Si le bouton gauche est relâché
        if left_click >= 0:
            # Obtient la position actuelle de la souris à l'écran
            x, y = pyautogui.position()

            # Convertit les coordonnées en coordonnées relatives à la fenêtre du jeu
            rect = win32gui.GetWindowRect(game_window)
            x_rel = x - rect[0]
            y_rel = y - rect[1]

            # Vérifie si la souris est à l'intérieur de la fenêtre du jeu
            if (0 <= x_rel < rect[2] - rect[0]) and (0 <= y_rel < rect[3] - rect[1]):
                print(f"Position (x, y) dans la fenêtre du jeu : ({x_rel}, {y_rel})")
