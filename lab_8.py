import cv2
import numpy as np

# Otwórz plik wideo
video = cv2.VideoCapture('video.mp4')

# Pobierz szerokość i wysokość klatki
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Otwórz plik do zapisu nowego wideo
output_video = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

# Pętla przez klatki wideo
while video.isOpened():
    # Pobierz następną klatkę
    ret, frame = video.read()
    if not ret:
        break

    # Konwertuj klatkę na przestrzeń kolorów HSV (skali odcienia, nasycenia, jasności)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Ustaw zakresy kolorów czerwonego i niebieskiego (użyj funkcji cv2.inRange, aby znaleźć obszary zawierające te kolory)
    lower_red = np.array([159, 50, 70])
    upper_red = np.array([180, 255, 255])
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Zastosuj maski do klatki obrazu (użyj funkcji cv2.bitwise_and, aby zachować tylko obszary zawierające czerwony lub niebieski kolor)
    frame_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    frame_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

    # Połącz klatki czerwoną i niebieską (użyj funkcji cv2.add)
    frame_combined = cv2.add(frame_red, frame_blue)

    # Zapisz nową klatkę do pliku wideo wyjściowego
    output_video.write(frame_combined)
    output_video.release()
    video.release()

