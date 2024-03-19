import cv2
import numpy as np
import serial
import throttle
from getHSVcolor import get_limits

# COM5 es correcto; CERRAR ARDUINO SERIAL MONITOR Y CONECTAR ESP32 ANTES DE INICIAR PROGRAMA --> VA A TIRAR 
# ERROR DE PERMISOS 
ser = serial.Serial(
  port= "COM8",
  baudrate= 9600
)

def get_contour_center(contour) -> int:
  M = cv2.moments(contour)
  if M["m00"] == 0:
    M["m00"] = 1
  # obtener centro del area
  x = int(M["m10"] / M["m00"])
  y = int(M["m01"] / M["m00"])

  return x, y

@throttle.wrap(0.200, 1)
def send_position(x: int) -> str:
  position = ''
  if(0 < x < 214):
    position = 'Left'
    print(position)
    ser.write(b'left\n')
  
  elif(214 < x < 428):
    position = 'Center'
    print(position)
    ser.write(b'center\n')
  
  elif(428 < x < 640):
    position = 'Right'
    print(position)
    ser.write(b'right\n')
  
  return position

def plot_frame(frame, contour, x: int, y: int):
  # marcar centro
  cv2.circle(frame, (x, y), 8, (183, 183, 22), -1)
  # dibujar el contorno convexHull
  new_contour = cv2.convexHull(contour)
  cv2.drawContours(frame, [new_contour], 0, (255, 0, 0), 3)
  # dibujar coordenadas (x, y) y posicion
  cv2.putText(frame, 'x: {}; y: {}'.format(x, y), 
              (x + 15, y + 5), 
              cv2.FONT_HERSHEY_SIMPLEX, 
              1.1, (0, 144, 255), 3)
  # cv2.putText(frameF, '{}'.format(position), (x + 40, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 3)

  return frame


# BGR_COLOR = [0, 255, 0]
# lowerLimit, upperLimit = get_limits(BGR_COLOR)

# limites color verde en hsv
lowerLimit = np.array([36, 50, 70])
upperLimit = np.array([89, 255, 255])

def main() -> None:
  # leer camara
  webcam = cv2.VideoCapture(0)
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

    # dibujar divisiones de la pantalla (left, center, right)
    # cv2.line(frameF, (214, 0), (214, 480), (0, 255, 0), 5)
    # cv2.line(frameF, (428, 0), (428, 480), (0, 255, 0), 5)

    for c in contours:
      
      area = cv2.contourArea(c)
      if area > 6000:
        # dibujar contornos de areas mayores a 6000
        #cv2.drawContours(frameF, c, -1, (255, 0, 0), 3)
        x, y = get_contour_center(c)
        # throttle estos if
        send_position(x)
        
        frameF = plot_frame(frameF, c, x, y)

    cv2.imshow('camara', frameF)
    if cv2.waitKey(40) & 0xFF == ord('q'):
      ser.close()
      break

  webcam.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()