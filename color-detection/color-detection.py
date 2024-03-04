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

  cv2.imshow('camara', mask)
  if cv2.waitKey(40) & 0xFF == ord('q'):
    break

webcam.release()
cv2.destroyAllWindows()