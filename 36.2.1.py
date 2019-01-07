import RoboPiLib as RPL
import setup

while True:
  x = RPL.analogRead(4)
  print('this is the sensor',x)
  automatic_braking.brake()
