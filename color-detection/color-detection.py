import cv2
from getHSVcolor import get_limits
# leer camara
webcam = cv2.VideoCapture(0)

BGR_COLOR = [0, 255, 0]
lowerLimit, upperLimit = get_limits(BGR_COLOR)

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
  cv2.drawContours(frameF, contours, -1, (0, 255, 0), 3)

  cv2.imshow('camara', frameF)
  if cv2.waitKey(40) & 0xFF == ord('q'):
    break

webcam.release()
cv2.destroyAllWindows()