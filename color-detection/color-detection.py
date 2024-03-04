import cv2
# leer camara
webcam = cv2.VideoCapture(0)
# ver camara
ret = True
while ret:
  ret, frame = webcam.read()
  frameF = cv2.flip(frame, 1)

  cv2.imshow('camara', frameF)
  if cv2.waitKey(40) & 0xFF == ord('q'):
    break

webcam.release()
cv2.destroyAllWindows()