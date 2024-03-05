import cv2
import numpy as np
from getHSVcolor import get_limits
# leer camara
webcam = cv2.VideoCapture(0)

BGR_COLOR = [0, 255, 0]
# limites color verde en hsv
lowerLimit = np.array([36, 50, 70])
upperLimit = np.array([89, 255, 255])
# lowerLimit, upperLimit = get_limits(BGR_COLOR)

# ver camara
ret = True
while ret:
  ret, frame = webcam.read()
  # flipear frame horizontalmente
  frameF = cv2.flip(frame, 1)
  
  hsvFrame = cv2.cvtColor(frameF, cv2.COLOR_BGR2HSV)
  # crear mascara
  mask = cv2.inRange(hsvFrame, lowerLimit, upperLimit)
  # extraer contornos (puntos limites de las areas blancas) de la mascara --> la imagen q 
  # se usa tiene q estar en binario
  contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
  for c in contours:
    area = cv2.contourArea(c)
    if area > 6000:
      # dibujar contornos de areas mayores a 6000
      cv2.drawContours(frameF, c, -1, (255, 0, 0), 3)

      M = cv2.moments(c)
      if M["m00"] == 0:
        M["m00"] = 1
      # obtener centro del area
      x = int(M["m10"] / M["m00"])
      y = int(M["m01"] / M["m00"])

      # marcar centro
      cv2.circle(frameF, (x, y), 8, (255, 0, 0), -1)
      # bibujar coordenadas (x, y)
      cv2.putText(frameF, 'x: {}, y: {}'.format(x, y), (x + 5, y + 5), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
      # dibujar el contorno convexHull
      new_contour = cv2.convexHull(c)
      cv2.drawContours(frameF, [new_contour], 0, (255, 0, 0), 3)

  cv2.imshow('camara', frameF)
  if cv2.waitKey(40) & 0xFF == ord('q'):
    break

webcam.release()
cv2.destroyAllWindows()