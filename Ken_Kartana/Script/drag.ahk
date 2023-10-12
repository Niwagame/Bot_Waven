#Persistent
Duration := %1% ; Récupère la durée depuis les arguments.
MouseClick, left, , , , , D ; Maintient le bouton gauche enfoncé.
Sleep, Duration ; Attend pendant la durée spécifiée.
MouseClick, left, , , , , U ; Relâche le bouton gauche.
ExitApp ; Termine le script.
