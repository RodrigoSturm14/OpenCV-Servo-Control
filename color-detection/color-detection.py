import cv2
import numpy as np
import serial
from getHSVcolor import get_limits

# ser = serial.Serial(
#   port=0
# )

# BGR_COLOR = [0, 255, 0]
# lowerLimit, upperLimit = get_limits(BGR_COLOR)

# limites color verde en hsv
lowerLimit = np.array([36, 50, 70])
upperLimit = np.array([89, 255, 255])


# leer camara
webcam = cv2.VideoCapture(0)
position = ''
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
      #cv2.drawContours(frameF, c, -1, (255, 0, 0), 3)

      M = cv2.moments(c)
      if M["m00"] == 0:
        M["m00"] = 1
      # obtener centro del area
      x = int(M["m10"] / M["m00"])
      y = int(M["m01"] / M["m00"])
      
      if(0 < x < 214):
        position = 'Left'
        print(position)
      
      elif(214 < x < 428):
        position = 'Center'
        print(position)
      
      elif(428 < x < 640):
        position = 'Right'
        print(position)
      
      # marcar centro
      cv2.circle(frameF, (x, y), 8, (183, 183, 22), -1)
      # dibujar el contorno convexHull
      new_contour = cv2.convexHull(c)
      cv2.drawContours(frameF, [new_contour], 0, (255, 0, 0), 3)

      # bibujar coordenadas (x, y) y posicion
      cv2.putText(frameF, 'x: {}; y: {}'.format(x, y), (x + 15, y + 5), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 144, 255), 3)
      cv2.putText(frameF, '{}'.format(position), (x + 40, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 3)


  cv2.imshow('camara', frameF)
  if cv2.waitKey(40) & 0xFF == ord('q'):
    print(frameF.shape)
    break

webcam.release()
cv2.destroyAllWindows()